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
    <a href="https://en.wikipedia.org/wiki/Finland/"><img src="https://img.shields.io/badge/Made_with_%E2%9D%A4%20in-Finland-blue" alt="Made with love in: Finland"/></a>
    <br>
    <br>
    Make relative <code>import</code> work without hassle.
    <br>
    <br>
    <pre>pip install <a href="https://github.com/hirsimaki-markus/importmonkey">importmonkey</a></pre>
    <br>
    <br>
    <br>
    <br>
</div>





# What does it do?
**Here is your repository:**
```
yourproject
├── source
│   └── yourproject
│       ├── __init__.py
│       └── yourmodule.py
└── test
    └── test.py
```

**test.py can't find yourmodule.py; one of these happens on import:**
```python
ModuleNotFoundError: No module named 'yourmodule'
ImportError: attempted relative import with no known parent package
SystemError: Parent module '' not loaded, cannot perform relative import
```

**importmonkey will fix that:**

```python
# In test.py
from importmonkey import add_path
add_path("../source")
import yourproject
```

# Why?
Sometimes you need a specific structure to, for example, test and build a package from the same source. So one must make
a relative import, or a sibling import, or a parent import, or an absolute import.


# Development details
<details><summary>Show details</summary>

   **Linting**
   ```
   asd
   ```

   **Testing**
   ```
   asd
   ```

   **Building**
   ```
   asd
   ```

   **Releasing**
   ```
   asd
   ```

</details>
