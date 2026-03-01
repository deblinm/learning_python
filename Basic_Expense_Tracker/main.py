import sys
from datetime import datetime

from expense_details import Expense
from tracker import Tracker

def take_user_choice():
    user_choice = input("\n\nDo you want to go back to the main menu? Press Y for yes : ")
    if user_choice not in ('Y', 'y'):
        print("Thank You for using our expense tracker. \n\n")
        sys.exit(0)

def main():
    tracker_obj = Tracker()
    while True:
        print("==============================")
        print("     EXPENSE TRACKER MENU     ")
        print("==============================")
        try:
            user_input = int(input("\n Please enter your choice from the below menu:\n"
                                       "Enter 1 if you want to Add a new expense\n"
                               "Enter 2 if you want to view all expenses\n"
                               "Enter 3 if you want check your total expense\n"
                               "Enter 4 if you want to see expenses by category\n"
                               "Enter 5 if you want to view your monthly expense summary\n"
                               "Enter 6 if you want to view your maximum or minimum expense for a month\n"
                               "Enter 7 if you want to save your expenses to a file\n"
                               "Enter 8 if you want to load your expenses from the saved file\n"
                               "Enter 9 if you want to Exit\n"))

            if user_input == 9:
                print("Thank You For using our expense tracker")
                break
            elif user_input == 1:
                while True:
                    category_ip = input ("\nPlease enter your expense category : ")
                    expense_type_ip = input("\nPlease enter your expense type : ")
                    while True:
                        try:
                            amount_ip = float(input("\n Please enter your expense amount : "))
                            break
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                    description_ip = input("\n Please enter your expense description : ")
                    while True:
                        try:
                            expense_date_ip = input("\n Please enter your expense date : ")
                            date_obj = datetime.strptime(expense_date_ip, '%m/%d/%Y')
                            break
                        except ValueError:
                            print("Invalid date. Please use MM/DD/YYYY format.")
                    expense_obj = Expense(category=category_ip, expense_type=expense_type_ip, amount=amount_ip,
                                          description=description_ip,expense_date=date_obj)
                    tracker_obj.addExpense(expense_obj)
                    print ("Your expense was successfully added")
                    take_user_choice()
            elif user_input == 2:
                tracker_obj.show_all()
                take_user_choice()
            elif user_input == 3:
                tracker_obj.total_spent()
                take_user_choice()
            elif user_input == 4:
                category_ip = input("Enter category to filter by: ")
                tracker_obj.filter_by_category(category_ip)
                take_user_choice()
            elif user_input == 5:
                tracker_obj.monthly_summary()
                take_user_choice()
            elif user_input == 6:
                tracker_obj.min_max_expense()
                take_user_choice()
            elif user_input == 7:
                tracker_obj.save_to_csv()
                take_user_choice()
            elif user_input == 8:
                tracker_obj.load_from_csv()
                take_user_choice()
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue



if __name__ == "__main__":
    main()