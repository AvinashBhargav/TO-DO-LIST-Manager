import mysql.connector

# Establish database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="todo_list"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Function to add a task to the todo list
def add_task():
    task = input("Enter task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    # SQL query to insert a new task into the table
    sql = "INSERT INTO tasks (task, due_date, status) VALUES (%s, %s, %s)"
    values = (task, due_date, "Incomplete")
    cursor.execute(sql, values)
    db.commit()
    print("Task added successfully!")

# Function to view all tasks in the todo list
def view_tasks():
    # SQL query to fetch all tasks from the table
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task[0]}\tTask: {task[1]}\tDue Date: {task[2]}\tStatus: {task[3]}")

# Function to update the status of a task
def update_task_status():
    task_id = input("Enter task ID: ")
    new_status = input("Enter new status (e.g., Complete, Incomplete): ")

    # SQL query to update the status of a task
    sql = "UPDATE tasks SET status = %s WHERE id = %s"
    values = (new_status, task_id)
    cursor.execute(sql, values)
    db.commit()
    print("Task status updated successfully!")

# Function to delete a task from the list
def delete_task():
    task_id = input("Enter task ID: ")

    # SQL query to delete a task from the table
    sql = "DELETE FROM tasks WHERE id = %s"
    values = (task_id,)
    cursor.execute(sql, values)
    db.commit()
    print("Task deleted successfully!")

# Main menu
def main():
    while True:
        print("\n---- Todo List Manager ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    cursor.close()
    db.close()
    print("Thank you for using the Todo List Manager!")

# Run the main function
if __name__ == "__main__":
    main()
