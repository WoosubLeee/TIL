# Packaging Python projects

이 문서에서 등록할 Python project 구조는 다음과 같다:

```
packaging_tutorial/
└── src/
    └── example_package/
        ├── __init__.py
        └── example.py
```

- `__init__.py` : required to import the directory as a package, and should be empty.

- `example.py` : an example of a module within the package that could contain the logic (functions, classes, constants, etc.) of your package. Open that file and enter the following content:

  ```python
  def add_one(number):
      return number + 1
  ```



## Creating the package files

You will now add files that are used to prepare the project for distribution. When you’re done, the project structure will look like this:

```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

- `LICENSE` : It’s important for every package uploaded to the Python Package Index to include a license. This tells users who install your package the terms under which they can use your package.

- `pyproject.toml` : build tools what is required to build your project. This tutorial uses `setuptools`.

  ```
  [build-system]
  requires = ["setuptools>=42"]
  build-backend = "setuptools.build_meta"
  ```

- Configuring metadata

  - `setup.cfg` : Static metadata, guaranteed to be the same every time. This is simpler, easier to read, and avoids many common errors, like encoding errors.
  - `setup.py` : Dynamic metadata, possibly non-deterministic. Any items that are dynamic or determined at install-time.

  Static metadata (`setup.cfg`) should be preferred.

  `setup.cfg` is the configuration file for `setuptools`. It tells `setuptools` about your package (such as the name and version) as well as which code files to include.

  ```
  [metadata]
  name = example-package-YOUR-USERNAME-HERE
  version = 0.0.1
  author = Example Author
  author_email = author@example.com
  description = A small example package
  long_description = file: README.md
  long_description_content_type = text/markdown
  url = https://github.com/pypa/sampleproject
  project_urls =
      Bug Tracker = https://github.com/pypa/sampleproject/issues
  classifiers =
      Programming Language :: Python :: 3
      License :: OSI Approved :: MIT License
      Operating System :: OS Independent
  
  [options]
  package_dir =
      = src
  packages = find:
  python_requires = >=3.6
  
  [options.packages.find]
  where = src
  ```

  - `meatdata`
    - `version` : see [PEP 440](https://www.python.org/dev/peps/pep-0440) for more details on versions.
  	- `project_urls` : any number of extra links to show on PyPI.
  	- `classifiers` : additional metadata about your package.
  - `options`
    - `package_dir` : a mapping of package names and directories. An empty package name represents the “root package” — the directory in the project that contains all Python source files for the package — so in this case the `src` directory is designated the root package.
    - `packages` : a list of all Python import packages that should be included in the distribution package. Instead of listing each package manually, we can use the `find:` directive to automatically discover all packages and subpackages and `options.packages.find` to specify the `package_dir` to use. In this case, the list of packages will be `example_package` as that’s the only package present.
    - `python_requires` : the Python version supported by your project.
    - `install_requires` : its core dependencies, without which it won’t be able to run. `setuptools` support automatically download and install these dependencies when the package is installed.

- `tests` : a placeholder for test files. Leave it empty for now.



## Generating distribution archives

```bash
$ python3 -m pip install --upgrade build
```

Now run this command from the same directory where `pyproject.toml` is located:

```bash
$ python3 -m build
```

This command should generate two files in the `dist` directory:

```
dist/
  example-package-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
  example-package-YOUR-USERNAME-HERE-0.0.1.tar.gz
```

The `tar.gz` file is a [source archive](https://packaging.python.org/en/latest/glossary/#term-Source-Archive) whereas the `.whl` file is a [built distribution](https://packaging.python.org/en/latest/glossary/#term-Built-Distribution).



## Uploading the distribution archives

우선 TestPyPI에 가입한다. 그리고

```bash
$ python3 -m pip install --upgrade twine
```

Once installed, run Twine to upload all of the archives under `dist`:

```bash
$ twine upload --repository testpypi dist/*
```

성공한다면 TestPyPI에 package가 업로드된다.

이제는 진짜 PyPI에 업로드해보자. PyPI에도 가입한 후 아래 코드를 작성하면 된다.

```bash
$ twine upload dist/*
```



## References

https://packaging.python.org/en/latest/tutorials/packaging-projects/