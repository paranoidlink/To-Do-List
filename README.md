# To-Do List

A command-line to-do list application written in Python.

The program allows users to create tasks, assign priorities, mark tasks as complete, sort the list, and save the data to a CSV file.

## Features

- Add tasks
- Add task descriptions
- Assign low, medium, or high priority
- Mark tasks as complete
- Sort tasks by description, priority, or completion status
- View the current task list
- Save tasks to `todo.csv`
- Load an existing task list when the program starts
- Input validation

## Usage

Run `to_do_list.py` and use the available commands:

- `add` - Add a new task
- `complete` - Mark a task as complete
- `sort` - Sort the task list
- `print` - Display the current task list
- `exit` - Exit and save the data

## CSV Format

Tasks are stored with the following fields:

| Field | Description |
|---|---|
| Task | Task name |
| Description | Task description |
| Priority | Low, medium, or high |
| Complete? | Whether the task is complete |

## Technologies

- Python
- CSV file handling

## Learning Focus

This project provided practice with functions, lists, validation, sorting, file handling, and maintaining application state across multiple user actions.