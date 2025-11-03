## Reflection

1. Which issues were the easiest to fix, and which were the hardest? Why?
- Issues like formatting code, missing docstrings or unused imports were easy to fix since fixing
them was straight-forward and did not require further testing.
- Issues like code security and design changes were harder to fix since they require refactoring
of code and further testing.

2. Did the static analysis tools report any false positives? If so, describe one example.
- The tools did not produce any false positives for the given inventory system code as it was limited
to the scope and simple.

3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
- Local development:
    - Run pylint, flake8, and bandit before committing code.
    - Use pre-commit hooks to automatically check code quality.

- Continuous Integration (CI):
    - Integrate static analysis tools in CI pipelines (e.g., GitHub Actions, GitLab CI).
    - Fail the build if critical issues or security risks are detected.
    - Generate reports to track code quality over time

4. What tangible improvements did you observe in the code quality, readability, or potential robustness
after applying the fixes
- The tools suggested changes that made the code look more uniform. This helps in readability and
allows code to be handled by more than one person in the team.
- The tools also suggested removal of unused imports and variables that improved code quality and
performance.
- Tools like bandit flagged issues regarding the security of the code which improved the robustness
of the code.
