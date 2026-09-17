"""Validate the minimum structure of a student course workspace."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / "workspace"
UNIT_NAMES = {"unit-02", "unit-04"}


def validate_notebook(path: Path) -> list[str]:
    """Return structural errors found in a Jupyter notebook."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path.relative_to(ROOT)}: invalid JSON ({exc})"]

    errors: list[str] = []
    if data.get("nbformat") != 4:
        errors.append(f"{path.relative_to(ROOT)}: expected notebook format 4")
    if not isinstance(data.get("cells"), list):
        errors.append(f"{path.relative_to(ROOT)}: missing cells list")
    return errors


def main() -> int:
    errors: list[str] = []
    for unit in sorted(WORKSPACE.iterdir()):
        if not unit.is_dir():
            continue
        if unit.name not in UNIT_NAMES:
            errors.append(f"Unexpected workspace unit: {unit.relative_to(ROOT)}")
            continue
        for session in sorted(unit.iterdir()):
            if not session.is_dir():
                continue
            if not session.name.startswith("session-"):
                errors.append(
                    f"{session.relative_to(ROOT)}: folder must start with 'session-'"
                )
            if not (session / "AGENTS.md").is_file():
                errors.append(
                    f"{session.relative_to(ROOT)}: missing session-level AGENTS.md"
                )
            for notebook in session.rglob("*.ipynb"):
                errors.extend(validate_notebook(notebook))

    if errors:
        print("Workspace validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Workspace validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
