from database import get_connection

class Employee:
    def __init__(self, name, department, email):
        self.name = name
        self.department = department
        self.email = email


def add_employee(employee):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, department, email) VALUES (?, ?, ?)",
        (employee.name, employee.department, employee.email)
    )
    conn.commit()
    conn.close()


def list_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No employees found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Department: {row[2]} | Email: {row[3]}")


def delete_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (int(employee_id),)
    )
    conn.commit()
    conn.close()
