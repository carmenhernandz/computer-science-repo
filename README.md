# EDEM Computer Science Course

Private student workspace for in-class follow-alongs and practice activities.
Create one private repository per student from this template.

## First setup

1. Download this repository as a ZIP file. 
2. Unzip it and open the folder in VS Code.
3. Open the repository folder in VS Code.
4. Create and activate a virtual environment.
5. Install the course dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Run the repository check:

   ```bash
   python scripts/validate_workspace.py
   ```

7. (Recommended) Create a new repository on GitHub and push your local repository to it.

## Class routine

1. Download the session bundle from the course website.
2. Extract it under `workspace/unit-02/` or `workspace/unit-04/`.
3. Work only in your session folder.
4. Review your changes with `git status` and `git diff`.
5. Commit and push your work.

Recommended folder names:

```text
workspace/
├── unit-02/
│   └── session-08-loops-lists-matplotlib/
└── unit-04/
    └── session-17-functions/
```

Never place credentials, personal data, or private URLs in this repository.

## AI support

The root `AGENTS.md` and the nearest session `AGENTS.md` govern AI assistance.
The available workflows are:

- `$socratic-tutor`
- `$debugging-coach`
- `$solution-reviewer`

AI guidance supports learning but cannot guarantee compliance or replace assessment
controls.
