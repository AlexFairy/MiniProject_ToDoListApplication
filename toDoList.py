task_box = []

def adding_tasks():
  try:
    add_tasks = int(input("How many tasks you want to add: "))
    for x in range(add_tasks):
      task = input("Enter the activity: ")
      task_box.append({"task": task, "done": False})
      print(x)
      print("...task has been uploaded into the database.")
  except ValueError:
    print("Please type an integer and not a string! Try again!")

def viewing_tasks():
  try:
    for index, task in enumerate(task_box):
      updated_status = "Task Status: Complete" if task["done"] else "Task Status: Incomplete"
      print(f"{index + 0}. {task['task']} - {updated_status}")
  except ValueError:
    print("Please type 'v' ")

def marked_tasks():
  try:
    task_index = int(input("Enter the task number to mark as done: "))
    if 1 <= task_index <= len(task_box):
      task_box[task_index]['done'] = True
      print("Task status uploaded as complete!")
    else:
      print("Incorrect entry.")
  except Exception:
    print("Entry missing or not in datalist. If so, please add!")

def delete_tasks():
  try:
    delete_task = int(input("Which task do you want to delete from the database: (type the number that pertains to the task) "))
    if delete_task < len(task_box):
      task_box.pop(delete_task)
      print("Task has been deleted!")
    else:
      print(f"Task {delete_task} was not found!")
  except Exception:
    print("")

def main():

  while True:
    selections_offered = input("Please select: [A]dd a task, [V]iew tasks, [M]ark as complete, [D]elete a task, [Q]uit: ")

    if selections_offered.lower() == 'a':
      adding_tasks()
    elif selections_offered.lower() == 'v':
      viewing_tasks()
    elif selections_offered.lower() == 'm':
      marked_tasks()
    elif selections_offered.lower() == 'd':
      delete_tasks()
    elif selections_offered.lower() == 'q':
      print("Thanks for using the program!")
      break

if __name__ == "__main__":
  main()
