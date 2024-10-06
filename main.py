#LIBRARIES
import random


def generate_quote():
  quotes = [
    "Believe you can and you're halfway there. \n - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. \n - Sam Levenson",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.  \n- Christian D. Larson",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. \n - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. \n- Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. \n- Eleanor Roosevelt",
    "You are never too old to set another goal or to dream a new dream. \n- C.S. Lewis",
    "The only way to do great work is to love what you do. \n- Steve Jobs",
    "The future starts today, not tomorrow. \n - Pope John Paul II",
    "The best way to predict the future is to create it. \n- Peter Drucker"
  ]

  return random.choice(quotes)


print(generate_quote())

#LIBRARIES
import matplotlib.pyplot as plt
import pandas as pd


def display_tasks(tasks):
  df = pd.DataFrame(tasks, columns=['Task', 'Status'])
  print(df)


def mark_complete(tasks, task_index):
  if task_index >= 0 and task_index < len(tasks):
    tasks[task_index][1] = 'Complete'
  else:
    print("Invalid task index!")


def calculate_completion_percentage(tasks):
  total_tasks = len(tasks)
  completed_tasks = sum(task[1] == 'Complete' for task in tasks)
  return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0


def generate_graph(tasks):
  completed_tasks = sum(task[1] == 'Complete' for task in tasks)
  remaining_tasks = len(tasks) - completed_tasks
  labels = ['Completed', 'Remaining']
  values = [completed_tasks, remaining_tasks]
  plt.pie(values, labels=labels, autopct='%1.1f%%')
  plt.axis('equal')
  plt.show()


def main():
  tasks = []

  while True:
    print("\n==== To-Do List ====")
    print("1. Add task")
    print("2. Mark task as complete")
    print("3. Show completion percentage")
    print("4. Show completed vs remaining tasks graph")
    print("5. Display tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
      print("How many tasks do you have to complete?")
      n = int(input("Enter the number of tasks :"))  
      for i in range(0,n):
         task = input("Enter the tasks :")
         tasks.append([task, 'Incomplete'])
      print("Tasks added successfully!")
    elif choice == '2':
      task_index = int(input("Enter task index to mark as complete: "))
      mark_complete(tasks, task_index)
    elif choice == '3':
      percentage = calculate_completion_percentage(tasks)
      print("Completion Percentage: {:.2f}%".format(percentage))
    elif choice == '4':
      generate_graph(tasks)
    elif choice == '5':
      display_tasks(tasks)
    elif choice == '6':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == '__main__':
  main()
