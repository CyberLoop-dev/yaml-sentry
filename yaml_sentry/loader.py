"""Safe YAML inspection with duplicate-key locations."""
from pathlib import Path
import yaml

class DuplicateKeyLoader(yaml.SafeLoader):
    def __init__(self, stream):
        super().__init__(stream)
        self.issues = []

    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in mapping
            except TypeError:
                self.issues.append({"line": key_node.start_mark.line + 1,
                                    "column": key_node.start_mark.column + 1,
                                    "message": "unhashable mapping key"})
                continue
            if duplicate:
                self.issues.append({"line": key_node.start_mark.line + 1,
                                    "column": key_node.start_mark.column + 1,
                                    "message": f"duplicate key {key!r}"})
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping

def inspect_yaml(path: Path) -> list[dict]:
    loader = DuplicateKeyLoader(path.read_text(encoding="utf-8"))
    try:
        loader.get_single_data()
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        loader.issues.append({
            "line": mark.line + 1 if mark else 0,
            "column": mark.column + 1 if mark else 0,
            "message": getattr(exc, "problem", None) or str(exc).splitlines()[0],
        })
    finally:
        loader.dispose()
    return [{"file": str(path), **issue} for issue in loader.issues]
