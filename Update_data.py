from mysql.connector import connect
my_conn = connect(
    host = "localhost",
    user = "root",
    password = "annu",
    database = "Employee"
)

def update_record():
    while True:
        choice  = input("Enter the id of the employee: ")
        cursor = my_conn.cursor()
        list = []
        cursor.execute("SELECT id FROM employee_details")
        Result = cursor.fetchall()
        for x in str(Result):
            list.append(x)
        if choice in list:
            print("Press 1 to update id\nPress 2 to update name\nPress 3 to update address\n"
            "Press 4 to update contact\nPress 5 to update salary\nPress 6 to update department.")
        update_choice = int(input("Enter ypur choice: "))
        if update_choice == 1:
            id = int(input("Enter the new id of the employee: "))
            sql_query = f"UPDATE employee_details SET id = %s where id = {choice}"
            values = (id,)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif update_choice == 2:
            name = input("Enter the new name of the employee: ")
            sql_query = f"UPDATE employee_details SET name = %s where id = {choice}"
            values = (name,)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif update_choice == 3:
            id = input("Enter the new address of the employee: ")
            sql_query = f"UPDATE employee_details SET address = %s where id = {choice}"
            values = (address,)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif update_choice == 4:
            id = input("Enter the new contact of the employee: ")
            sql_query = f"UPDATE employee_details SET contact = %s where id = {choice}"
            values = (contact,)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif update_choice == 5:
            id = input("Enter the new salary of the employee: ")
            sql_query = f"UPDATE employee_details SET salary = %s where id = {choice}"
            values = (salary,)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif update_choice == 6:
            id = input("Enter the new department of the employee: ")
            sql_query = f"UPDATE employee_details SET dept = %s where id = {choice}"
            values = (dept,)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif update_choice == 7:
            id = int(input("Enter the new id of the employee: "))
            name = input("Enter the new name of the employee: ")
            contact = input("Enter the new contact number of the employee: ")
            address = input("Enter the new address of the employee: ")
            salary = float(input("Enter the new salary of the employee: "))
            dept = input("Enter the new department of the employee: ")
            sql_query = f"UPDATE employee_details SET id = %s, name = %s, address = %s, contact = %s, salary = %s, dept = %s where id = {choice}"
            values = (id,name,contact,address,salary,dept)
            cursor.execute(sql_query,values)
            my_conn.commit()
            print("Congratulations! You had successfully updated.")
        elif choice not in list:
            print("Sorry!\nThis Employee ID doesn't exist in the database.")
        choice = input("\nDo you want to update anything else ? \n(yes/no): ")
        if choice == "no":
            print("Have a good day!")
        break