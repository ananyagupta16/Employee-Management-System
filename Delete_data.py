from mysql.connector import connect
my_conn = connect(
    host = "localhost",
    user = "root",
    password = "annu",
    database = "Employee"
)

def delete_record():
    cursor = my_conn.cursor()
    print("Press 1 to delete speicfic record\nPress 2 to delete all records.")
    del_choice = int(input("Enter the choice: "))
    if del_choice == 1:
        print("You are going to delete the data related to gien id.")
        choice = input("Enter the id of the employee: ")
        list = []
        cursor.execute("SELECT id FROM employee_details")
        Result = cursor.fetchall()
        for x in str(Result):
            list.append(x)
        if choice in list:
            sql_query = f"DELETE FROM employee_details where id = %s"
            values = (choice,)
            cursor.execute(sql_query,values)
            my_conn.commit()
        elif choice not in list:
            print("Given id is not present in the database.")
    elif del_choice == 2:
        print("You are going to delete all the data from the table.")
        sql_query = f"DELETE FROM employee_details"
        cursor.execute(sql_query)
        my_conn.commit()

    cursor.close()
    my_conn.close()


    print("Congratulations! You had deleted successfully.")


