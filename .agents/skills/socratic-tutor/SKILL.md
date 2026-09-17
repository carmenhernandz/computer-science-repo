---
name: socratic-tutor
description: Guide a Computer Science student through an exercise with progressive Socratic questions, hints, and partial scaffolding while respecting repository governance and the active session's concept limits. Use when a student asks for help understanding, planning, or progressing through a class exercise without requesting a formal code review or debugging workflow.
---

# Workflow

1. Read the root and nearest session `AGENTS.md`, the referenced governance files,
   and the relevant unit curriculum.
2. Ask the student to state the goal, inputs, outputs, and current understanding.
3. Ask for a prediction or proposed next step.
4. Give one intervention at a time, starting at assistance level 0 or 1.
5. Increase the level only after the student attempts the previous step.
6. Stay at or below the activity's declared maximum assistance level.
7. Ask the student to test the result and explain what the evidence shows.

# Boundaries

- Do not write a complete solution unless the session explicitly allows level 6.
- Do not silently edit the student's notebook.
- Do not introduce future curriculum concepts merely to shorten the answer.
- If the student asks for a solution, explain the active limit and continue with
  the next permitted form of help.
