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
    Just the tool to make <code>import</code> work without hassle.
    <br>
    <br>
    <pre>pip install <a href="https://github.com/hirsimaki-markus/importmonkey">importmonkey</a></pre>
    <br>
    <br>
</div>





# What does it do?
**Assume your project looks like this because you are building a new package for pip**
```
yourproject
├── src
│   ├── yourproject
│   │   └── __init__.py
│   └── pyproject.toml
└── test
    └── test_yourproject.py
```

**But now your tests can't import the project because of the structure; you always get one of**
```python
ModuleNotFoundError: No module named 'myproject'
ImportError: attempted relative import with no known parent package
SystemError: Parent module '' not loaded, cannot perform relative import
```

**importmonkey will fix that**

```python
>>> # In test_yourproject.py
>>> from importmonkey import add_path
>>> add_path("../src")
>>> import yourproject
```

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
