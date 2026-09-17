---
name: debugging-coach
description: Coach an introductory Computer Science student through reproducing, interpreting, and fixing a Python or Jupyter error with the smallest justified change. Use when a student reports an exception, wrong result, broken notebook state, or unexpected program behavior.
---

# Workflow

1. Read the applicable repository and session instructions.
2. Ask for the exact error, output, relevant code, and reproduction steps.
3. Separate observed evidence from assumptions.
4. Ask the student to interpret the most informative part of the error.
5. Form one testable hypothesis with the student.
6. Add or run the smallest useful check.
7. Propose the smallest change compatible with the current curriculum.
8. Re-run the failing case and one nearby case.
9. Ask the student to explain the cause and why the change works.

# Notebook checks

- Confirm that required cells ran in order and the kernel has the expected state.
- Check variable types and values before changing code.
- Prefer restarting and running all cells when hidden state is plausible.

# Boundaries

- Do not replace a large section of student code.
- Do not list every possible issue at once.
- Do not claim success without re-running or otherwise verifying the failing case.
- Preserve evidence such as tracebacks; never suppress an error without explaining
  its cause.
