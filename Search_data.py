from mysql.connector import connect
my_conn = connect(
    host = "localhost",
    user = "root",
    password = "annu",
    database = "Employee"
)
def search_record():
    cursor = my_conn.cursor()
    print("Press 1 to search speicfic record\nPress 2 to search all records.")
    search_choice = int(input("Enter the choice: "))
    if search_choice == 1:
        print("You are going to select the data related to given id.")
        choice = input("Enter the id of the employee: ")
        list = []
        cursor.execute("SELECT id FROM employee_details")
        Result = cursor.fetchall()
        for x in str(Result):
            list.append(x)
        if choice in list:
            sql_query = "SELECT * FROM employee_details where id = %s"
            values = (choice,)
            cursor.execute(sql_query,values)
            rs = cursor.fetchall()
            print("id       name        address         contact         salary          dept")
            for i in rs:
                print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
        elif choice not in list:
            print("Given id is not present in the database.")
    elif search_choice == 2:
        print("You are going to select all the data from the table.")
        sql_query = "SELECT * FROM employee_details"
        cursor.execute(sql_query)
        rs = cursor.fetchall()
        print("id   name    address     contact     salary      dept")
        for i in rs:
            print(i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],"\t\t",i[4],"\t\t",i[5])
        print("Congratulations! You had selected successfully.")
    try:
        cursor.close()
    except Exception as e:
        print("Cursor have more data and can not able to close right now...!")
    my_conn.close()

