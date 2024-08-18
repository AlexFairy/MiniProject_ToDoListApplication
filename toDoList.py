task_box = []

while True:
  selections_offered = input("Please select: [A]dd a task, [V]iew tasks, [M]ark as complete, [D]elete a task, [Q]uit: ")
  try:
    if selections_offered.lower() == 'a':
      add_tasks = int(input("How many tasks you want to add: "))
      print() 
      for x in range(add_tasks):
        task = input("Enter the activity: ")
        task_box.append({"task": task, "done": False})
        print("...task has been uploaded into the database.")
  except ValueError:
    print("Please type an integer and not a string! Try again!")   
  
  try:
    if selections_offered.lower() == 'v':
      for index, task in enumerate(task_box):
        updated_status = "Task Status: Complete" if task["done"] else "Task Status: Incomplete"
        print(f"{index + 0}. {task['task']} - {updated_status}")
  except ValueError:
    print("Please type 'v' ")
  try:
    if selections_offered.lower() == 'm':
      task_index = int(input("Enter the task number to mark as done: "))
      if 1 <= task_index <= len(task_box):
        task_box[task_index]['done'] = True
        print("Task status uploaded as complete!")
      else:
        print("Incorrect entry.")
  except Exception:
    print("Entry missing or not in datalist. If so, please add!")
  try:
    if selections_offered.lower() == 'd':
      delete_task = int(input("Which task do you want to deleter from the database: "))
      if delete_task < len(task_box):
        task_box.pop(delete_task)
        print("Task has been deleted!")
      else:
        print(f"Task {delete_task} was not found!")
  except Exception:
    print("Empty")
  try:
    if selections_offered.lower() == 'q':
      print("Exiting database!")
      break
  except Exception:
    print("Empty")
  finally:
    print("Thank You for using the application!!")