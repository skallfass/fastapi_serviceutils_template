# Clean code

The development of this service tries to follow clean code style as good as
possible.

To achieve this we:

* write [PEP8](../../references/index.html#pep8) valid code.
  To achieve this we use [black](../../references/index.html#black) in combination
  with [codespell](../../references/index.html#codespell),
  [pycodestyle](../../references/index.html#pydocstyle),
  [pylint](../../references/index.html#pylint) and
  [flake8](../../references/index.html#flake8).
* write docstrings with meaningful description of the function, method, class
  we want to describe.
  These docstrings are written in [Markdown](../../references/index.html#markdown).
  To increase the ability for the user to understand as fast as possible the
  input and output of functions, methods and classes we also use [Type
  Annotations](../../references/index.html#type-annotations).
* write meaningful tests using [Pytest](../../references/index.html#pytest).
* use meanigful variable-, function- method- and class-names
* use [semantic versioning style](../../references/index.html#semantic-versioning-semver)
* use a fixed [git-workflow](../git_workflow/index.html)
* try to use `pure functions` if possible.
