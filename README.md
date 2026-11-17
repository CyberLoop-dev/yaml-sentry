<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%2322c55e&height=170&section=header&text=YAML%20SENTRY&fontSize=40&fontColor=ffffff" alt="YAML Sentry banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=22&pause=1000&color=22C55E&center=true&vCenter=true&width=650&lines=Catch+duplicate+YAML+keys+before+they+become+bugs" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/yaml-sentry"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/yaml-sentry"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/yaml-sentry"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/yaml-sentry"/></p>
<p align="center"><img src="assets/overview.svg" alt="YAML Sentry illustration" width="92%"/></p>

## 🧭 Overview
YAML Sentry checks local YAML files for duplicate mapping keys and syntax errors. It reports problems without rewriting configuration files.

## ✨ Features
- 🔎 Detects duplicate mapping keys, including nested mappings.
- 📍 Reports file, line, and column locations.
- 📦 Supports human-readable and JSON output for scripts.
- 🛡️ Uses a safe YAML loader and never executes custom constructors.

## 🎬 Demo
```text
$ python main.py examples/duplicate.yaml
examples/duplicate.yaml:4:3: duplicate key 'port'
1 issue(s) found.
```
The example runs locally; no upload or hosted service is involved.

## 🚀 Quick Start
```bash
python -m pip install -r requirements.txt
python main.py examples/duplicate.yaml
```
Add `--json` for machine-readable output or `--strict` to exit with status 1 when issues are found.

## 🧰 Tech Stack
- Python 3.10+
- PyYAML safe parsing
- unittest regression tests

## 🗂️ Folder Structure
```text
main.py
yaml_sentry/loader.py
tests/test_loader.py
examples/duplicate.yaml
assets/overview.svg
requirements.txt
```

## 🗺️ Roadmap
- [x] Duplicate-key detection
- [x] Syntax-error locations
- [ ] Optional config-specific rule packs

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for bug fixes and keep the checker read-only.

## 📄 License
Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%2322c55e&height=110&section=footer" alt="Animated footer"/></p>
