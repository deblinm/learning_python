from expense_details import Expense
from tracker import Tracker

def main():
    trial = Expense(category="food",expense_type= "variable",amount= 15.0, description="lunch",expense_date= "02/10/2025")
    trial2 = Expense(category="music", expense_type="fixed", amount=20, description="ukulele",
                    expense_date="02/05/2025")
    trial3 = Expense(category="food", expense_type="variable", amount=25.0, description="dinner",
                     expense_date="02/10/2025")
    trial4 = Expense(category="food", expense_type="variable", amount=25.0, description="dinner",
                     expense_date="03/10/2025")
    trial5 = Expense(category="music", expense_type="fixed", amount=25.0, description="ukulele",
                     expense_date="03/12/2025")
    trial6 = Expense(category="music", expense_type="fixed", amount=35.0, description="guitar",
                     expense_date="03/12/2025")
    tracker = Tracker()
    tracker.addExpense(trial)
    tracker.addExpense(trial2)
    tracker.addExpense(trial3)
    tracker.addExpense(trial4)
    tracker.addExpense(trial5)
    tracker.addExpense(trial6)
    tracker.show_all()
    tracker.total_spent()
    tracker.filter_by_category("food")
    tracker.filter_by_category("tution")
    tracker.monthly_summary()
    tracker.min_max_expense()
    tracker.save_to_csv()
    tracker.load_from_csv()

if __name__ == "__main__":
    main()