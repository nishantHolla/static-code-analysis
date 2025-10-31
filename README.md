# static-code-analysis

Software Engineering lab for static code analysis using tools like pylint, bandit and flake8.

## Known Issues

| Issue     | Type      | Line      | Description | Fix Approach |
|-----------|-----------|-----------|-------------|--------------|
| Missing module docstring | Documentation | 1 | The module lacks a top-level docstring describing its purpose. | Add a short description at the top of the file explaining what the module does. |
| Missing function docstring | Documentation | 9, 16, 25, 29, 36, 42, 48, 56 | Several functions lack docstrings. | Add brief docstrings explaining what each function does, its parameters, and return values. |
| Invalid function naming (e.g. `addItem`) | Style | 9, 16, 25, 29, 36, 42, 48 | Function names don’t follow Python’s `snake_case` naming convention. | Rename functions to follow `snake_case` (e.g., `add_item`, `remove_item`). |
| Dangerous default value (`[]`) | Bug | 9 | A mutable default argument can lead to shared state between calls. | Use `None` as default and initialize inside the function (e.g., `def f(arg=None): arg = arg or []`). |
| Should use f-string | Style | 13 | Regular string formatting used instead of modern f-strings. | Replace string concatenation or `%` formatting with f-strings for clarity. |
| Bare except block | Safety | 21 | Catching all exceptions without specifying type hides real errors. | Catch specific exceptions (e.g., `except ValueError:`) or re-raise unexpected ones. |
| File opened without encoding | Safety | 30, 37 | `open()` used without specifying encoding, which may cause cross-platform issues. | Use `open(filename, "r", encoding="utf-8")` or similar. |
| Use of `global` keyword | Design | 31 | Global variables can cause side effects and hard-to-track bugs. | Avoid `global`; use return values, parameters, or encapsulate state in a class. |
| Use of `eval()` | Security | 67 | Using `eval()` can execute arbitrary code and is unsafe. | Replace with `ast.literal_eval()` or safer parsing methods like `json.loads()`. |
| File not closed properly | Best Practice | 30, 37 | File opened without using `with` statement for automatic closure. | Use `with open(...) as f:` to handle file operations safely. |
 Unused import `logging` | Cleanup | 2 | The `logging` module is imported but not used. | Remove the unused import statement. |

