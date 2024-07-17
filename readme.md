<div align="center">
    <h1>
        <br>
        🐵
        <br>
        importmonkey
        <br>
    </h1>
    <br>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12.0-blue?logo=python&logoColor=white"/></a>
    &nbsp;
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Dependencies-None-blue"/></a>
    &nbsp;
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/Style-Ruff-261230"/></a>
    &nbsp;
    <a href="https://choosealicense.com/licenses/unlicense/"><img src="https://img.shields.io/badge/Licence-The_Unlicence-purple"/></a>
    &nbsp;
    <a href="https://en.wikipedia.org/wiki/Finland"><img src="https://img.shields.io/badge/Made_with_%E2%9D%A4%20in-Finland-blue"/></a>
    <br>
    <br>
    An utility for adding new import paths to make your relative <code>import</code> work without hassle.
    <br>
    <br>
    <pre>pip install <a href="https://github.com/hirsimaki-markus/importmonkey">importmonkey</a></pre>
    <br>
</div>




## What does it do?
**Here is your repository:**
```
├─ src
│   └─ project
│       ├─ __init__.py
│       └─ module.py
└─ test
    └─ test.py
```

**test.py can't find module.py:**
```python
ModuleNotFoundError: No module named 'module'
ImportError: attempted relative import with no known parent package
SystemError: Parent module '' not loaded, cannot perform relative import
```

**importmonkey will fix that:**
```python
import importmonkey  # In test.py
importmonkey.add_path("../src")
import project
```




### Documentation / Licensing / Dev stuff
<details><summary>Expand</summary>


### Documentation
`help(importmonkey.add_path)  # Or look at the source.`

### Licensing
To protest the copyright landscape, I chose The Unlicense. If you need a different license, just ask.

### Dev stuff
* Install for dev stuff: `importmonkey$ pip install -e ".[dev]"  # In a venv`
* Linting: `importmonkey$ python -m ruff check .`
* Testing: `importmonkey$ python test/run_test_suite.py`
* Releasing:
```bash
# Remember: increment __version__ in __init__.py
# Remember: .pypirc file is needed.
# Remember: run tests
# Remember: run ruff
importmonkey$ python -m build --wheel
importmonkey$ rm -rf build/ && rm -rf src/importmonkey.egg-info/
importmonkey$ python -m twine check dist/*
importmonkey$ python -m twine upload dist/*
importmonkey$ rm -rf dist/
```
