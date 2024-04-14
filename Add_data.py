from mysql.connector import connect
my_conn = connect(
    host = "localhost",
    user = "root",
    password = "annu",
    database = "Employee"
)

def add_record():
    cursor = my_conn.cursor()
    sql_query = "INSERT employee_details values(%s,%s,%s,%s,%s,%s)"

    id = int(input("Enter the id of the employee: "))
    name = input("Enter the name of the employee: ")
    contact = input("Enter the contact number of the employee: ")
    address = input("Enter the address of the employee: ")
    salary = float(input("Enter the salary of the employee: "))
    dept = input("Enter the department of the employee: ")

    values = (id,name,contact,address,salary,dept)
    
    cursor.execute(sql_query,values)
    my_conn.commit()

    my_conn.close()
    cursor.close()

    print("All details inserted!")