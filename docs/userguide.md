# User Guide

## Start the app
Open a terminal in the project folder and run `python main.py`.

## Menu options
- **1 Add task:** type a title. Empty titles are rejected.
- **2 Show tasks:** lists all tasks. `[x]` means completed, `[ ]` means pending.
- **3 Complete task:** enter one ID, or several separated by commas, like `1,3`.
- **4 Delete task:** enter a valid task ID.
- **5 Exit:** closes the app.

## Common messages
- "Task title cannot be empty." means you pressed Enter without typing a title.
- "Task title must be 100 characters or less." means the title is too long.
- "Task N is already completed." means that task was already marked done.
- "Skipped 'x': not a valid ID." means the input was not a number.
- "No task found with ID N." means that ID does not exist.

## Where tasks are saved
Tasks are stored in `tasks.json` in the project folder, so they remain after you close the app.