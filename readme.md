<div align="center">
    <h1>
        <br>
        🐵
        <br>
        importmonkey
        <br>
        <br>
    </h1>
    <br>
    <br>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12.0-blue?logo=python&logoColor=white"/></a>
    &nbsp;
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Dependencies-None-blue"/></a>
    &nbsp;
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/Style-black-000000"/></a>
    &nbsp;
    <a href="https://choosealicense.com/licenses/unlicense/"><img src="https://img.shields.io/badge/Licence-The_Unlicence-purple"/></a>
    &nbsp;
    <a href="https://en.wikipedia.org/wiki/Finland"><img src="https://img.shields.io/badge/Made_with_%E2%9D%A4%20in-Finland-blue"/></a>
    <br>
    <br>
    An utility for adding new import paths to
    <br>
    make your relative <code>import</code> work without hassle.
    <br>
    <br>
    <pre>pip install <a href="https://github.com/hirsimaki-markus/importmonkey">importmonkey</a></pre>
    <br>
    <br>
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
from importmonkey import add_path  # In test.py
add_path("../src")
import project
```


<br>


## Why?
<details><summary>Show details</summary>

Sometimes you want a specific repo structure to test and build a package from the same
files so you need a relative / sibling / parent import.

</details>


<br>


## Documentation
<details><summary>Show details</summary>

```python
>>> import importmonkey
>>> help(importmonkey.add_path)
>>> # Or take a look at the well documented source.
```

</details>


<br>


## Development details
<details><summary>Show details</summary>

  **Linting**
  ```bash
  importmonkey$ python -m black .
  importmonkey$ python -m flake8 src/ test/
  ```

  **Testing**
  ```bash
  importmonkey$ python test/run_test_suite.py
  ```

  **Building & releasing**
  ```bash
  # Remember to increment __version__ in __init__.py
  # Also, remember to create .pypirc file in home directory
  importmonkey$ python -m build --wheel && rm -rf build/ && rm -rf src/importmonkey.egg-info/
  importmonkey$ python -m twine check dist/*
  importmonkey$ python -m twine upload dist/*
  importmonkey$ rm -rf dist/
  ```

</details>


<br>


## Additional licensing
<details><summary>Show details</summary>

This software is licensed under The Unlicense as the author's protest towards
the modern copyright landscape. If you need a different lisence for legal or
compability reasons, just ask.

</details>