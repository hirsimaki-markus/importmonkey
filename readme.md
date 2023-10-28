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
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12.0-blue?logo=python&logoColor=white" alt="Python ver: 3+"/></a>
    &nbsp;
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Dependencies-None-blue" alt="Dependencies: None"/></a>
    &nbsp;
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/Style-black-000000" alt="Style: Black"/></a>
    &nbsp;
    <a href="https://choosealicense.com/licenses/unlicense/"><img src="https://img.shields.io/badge/Licence-The_Unlicence-purple" alt="Licence: The Unlicence"/></a>
    &nbsp;
    <a href="https://en.wikipedia.org/wiki/Finland"><img src="https://img.shields.io/badge/Made_with_%E2%9D%A4%20in-Finland-blue" alt="Made with love in: Finland"/></a>
    <br>
    <br>
    Makes your relative <code>import</code> work without hassle.
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
<br>
<br>

## Why?
Sometimes you want a specific repo structure to test and build a package from the same
files so you need a relative / sibling / parent import.

<br>
<br>
<br>

## Development details
<details><summary>Show details</summary>

  **Linting**
  ```bash
  importmonkey$ black .
  importmonkey$ flake8 src/ test/
  ```

  **Testing**
  ```bash
  importmonkey$ python test/run_test_suite.py
  ```

  **Building**
  ```
  coming soon
  ```

  **Releasing**
  ```
  coming soon
  ```

</details>
