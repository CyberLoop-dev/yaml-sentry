#!/usr/bin/env python3
"""Read-only YAML duplicate-key and syntax checker."""
import argparse
import json
from pathlib import Path
from yaml_sentry.loader import inspect_yaml

def main() -> int:
    parser = argparse.ArgumentParser(description="Find duplicate keys and YAML syntax errors.")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    results = []
    for path in args.files:
        if not path.is_file():
            results.append({"file": str(path), "line": 0, "column": 0, "message": "file not found"})
        else:
            results.extend(inspect_yaml(path))
    if args.as_json:
        print(json.dumps(results, indent=2))
    else:
        for item in results:
            print(f"{item['file']}:{item['line']}:{item['column']}: {item['message']}")
        print(f"{len(results)} issue(s) found.")
    return 1 if args.strict and results else 0

if __name__ == "__main__":
    raise SystemExit(main())
