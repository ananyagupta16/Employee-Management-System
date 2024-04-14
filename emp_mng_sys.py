from Add_data import add_record
from Delete_data import delete_record
from Update_data import update_record
from Search_data import search_record

def main():
    print("-------------------------------------")
    print("     Employee Management System      ")
    print("-------------------------------------")
    while True:
        print("Press 1 to inesrt records\nPress 2 to update the records\nPress 3 to delete the record\nPress 4 to search the record")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_record()
        elif choice == 2:
            print("You can update your details here - id, name, contact,address, salary,department.")
            update_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            search_record()
        else:
            print("Invalid choice! Please enter a valid option.")
            continue
        choice = input("\nDo you want to continue(yes/no): ")
        if choice != "yes":
            print("Until next time!")
            exit
main()