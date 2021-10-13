# Build and publish to PyPI

*This action aims to quickly publish releases for a Python package.*

## Usage

Use the following command to publish a package located in current folder as user toto on PyPI.
Package version is retrieved automatically from the name of the tag created by your release on github.

```yaml
- uses: sylvanld/actions/release-pypi@main
  with:
    context: .
    username: toto
    password: p@ssword1234
```

**with:**

|parameter|description|optional|default|
|-|-|-|-|
|**context**|Path to the `setup.py` file for the package to be distributed|yes|.|
|**username**|Name of the user that will own the package in PyPI|no|-|
|**password**|Password or token of the user that will own the package in PyPI|no|-|
