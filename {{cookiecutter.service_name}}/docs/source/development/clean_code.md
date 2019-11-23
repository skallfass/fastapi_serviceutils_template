# Clean code

The development of this service tries to follow clean code style as good as
possible.

To achieve this we:

* write [PEP8](/references#pep8) valid code.
  To achieve this we use [black](/references#black) in combination with
  [codespell](/references#codespell), [pycodestyle](/references#pydocstyle),
  [pylint](/references#pylint) and [flake8](/references#flake8).
* write docstrings with meaningful description of the function, method, class
  we want to describe.
  These docstrings are written in [Markdown](/references#markdown).
  To increase the ability for the user to understand as fast as possible the
  input and output of functions, methods and classes we also use [Type
  Annotations](/references#type-annotations).
* write meaningful tests using [Pytest](/references#pytest).
* use meanigful variable-, function- method- and class-names
* use [semantic versioning style](/references#semantic-versioning-semver)
* use a fixed [git-workflow](../git_workflow)
* try to use `pure functions` if possible.
