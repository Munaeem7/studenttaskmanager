# Student Task Manager

A small Python console application to manage student tasks. Built as a Git and GitHub workflow assignment.

Project status: Planning

## Features

- Add tasks with input validation
- Show all tasks with their completion state
- Mark one or more tasks as completed
- Delete tasks by ID
- Tasks are saved in a local `tasks.json` file

## Setup

1. Install Python 3.8 or newer
2. Clone the repository:
   ```
   git clone https://github.com/Munaeem7/studenttaskmanager.git
   cd studenttaskmanager
   ```
3. No extra packages are needed

## Usage

Run the app:

```
python main.py
```

Choose an option from the menu:

| Option | Action |
|--------|--------|
| 1 | Add a task |
| 2 | Show tasks |
| 3 | Complete task(s), e.g. `1` or `1,3` |
| 4 | Delete a task by ID |
| 5 | Exit |

## License

This project is licensed under the MIT License.