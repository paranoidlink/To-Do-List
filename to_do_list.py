import csv
from operator import itemgetter
import sys
import os

def read_file(todo_list):
    with open("todo.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            todo_list.append(row)
        return todo_list
    
def save_file(todo_list):
    with open("todo.csv", "w") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Task", "Description", "Priority", "Complete?"])
        
        writer.writerows(todo_list)

def task_and_description_validator(criteria):
    while criteria == "":
        print("Please enter a valid value")
        criteria = input()
    return criteria

def priority_validator(priority):
    while priority.lower() not in ["low", "medium", "high"]:
        print("Please enter a valid priority for this task valid options are either \'low\' \'medium\' or \'high\'")
        priority = input()
    return priority

def completion_validator(completion_status):
    while completion_status.lower() not in ["true", "false"]:
        print("Please enter a valid completion status either \'true\' or \'false\'")
        complete_status = input()
    return completion_status

def criteria_validator(criteria):
    while criteria.lower() not in ["description", "priority", "status"]:
        print("Please enter a valid search criteria either \'description\' \'priority\' or \'status\'")
        criteria = input()
    return criteria

def empty_list_check(todo_list):
    if todo_list == []:
        print("Empty list error please populate the list before running this function")
        return True
    return False

def main_menu_validator(response):
    while response.lower() not in ["add", "complete", "sort", "print", "exit"]:
        print("Please enter a valid command of either \'add\' \'complete\' \'sort\'  \'print\' or \'exit\'")
        response = input()
    return response

def add_task(todo_list, task, description, priority, completion_status):
    task = task_and_description_validator(task)
    description = task_and_description_validator(description)
    priority = priority_validator(priority)
    completion_status = completion_validator(completion_status)

    task_data = [task.capitalize(), description.capitalize(), priority.capitalize(), completion_status]
    todo_list.append(task_data)
    return todo_list
    
def complete_task(todo_list, task):
    if empty_list_check(todo_list) == True:
        return todo_list
    for item in todo_list:
        if task.capitalize() in item[0]:
            item[3] = "True"
            print(task + " has been succesfully marked as complete")
            return todo_list
    print("Task could not be found please check your spelling and try again")
    return todo_list

def sorter(todo_list, sort_criteria):
    if empty_list_check(todo_list) == True:
        return todo_list
    criteria_validator(sort_criteria)
    if sort_criteria.lower() == "description":
        todo_list = sorted(todo_list, key=itemgetter(1))
        return todo_list
    elif sort_criteria.lower() == "priority":
        todo_list = sorted(todo_list, key=itemgetter(2))
        return todo_list
    elif sort_criteria.lower() == "status":
        todo_list = sorted(todo_list, key=itemgetter(3))
        return todo_list
    
def get_input(script):
    if script == 1:
        print("Please enter the name of the task you'd like to add")
        task = input()
        print("Please enter a short description for this task")
        description = input()
        print("Please enter a priority of \'low\' \'medium\' or \'high\' for this task")
        priorty = input()
        print("Please enter if this task is complete either \'True\' or \'False\'")
        complete_status = input()
        return task,description,priorty,complete_status
    elif script == 2:
        print("Please enter the name of the task you'd like to complete")
        task = input()
        return task
    elif script == 3:
        print("Please enter the category you'd like to search by either \'description\' \'priority\' or \'status\'")
        sort_criteria = input()
        return sort_criteria

todo_list = []
if os.path.exists("todo.csv"):
    todo_list = read_file(todo_list)
    print("Existing todo list imported succesfully!")
print("Hello welcome to the todo list, to add a task type \'add\' to mark a task as complete type \'complete\' to sort the list type \'sort\' to view the current list type \'print\' to exit the program type \'exit\'")
response = input()
response = main_menu_validator(response)
while True:
    if response == "add":
        task,description,priority,complete_status = get_input(1)
        todo_list = add_task(todo_list, task, description, priority, complete_status)
        save_file(todo_list)
        print("New entry added and saved succesfully")
    elif response == "complete":
        task = get_input(2)
        todo_list = complete_task(todo_list, task)
        save_file(todo_list)
        print("Task updated as completed and saved")
    elif response == "sort":
        sort_criteria = get_input(3)
        todo_list = sorter(todo_list, sort_criteria)
        save_file(todo_list)
        print("list sorted you may view this by either using the print option or viewing the file directly")
    elif response == "print":
        print(str(todo_list))
    elif response == "exit":
        sys.exit("Exiting program your progress has been saved")
    print("Please enter the next command either \'add\' \'complete\' \'sort\' \'print\' or \'exit\'")
    response = main_menu_validator(input())

