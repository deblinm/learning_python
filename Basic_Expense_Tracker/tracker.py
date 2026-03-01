from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List
from expense_details import Expense
import csv

@dataclass
class Tracker :
    expenses: List[Expense]= field(default_factory=list)

    def addExpense(self,expense):
        self.expenses.append(expense)

    def show_all(self):
        if not self.expenses:
            print ("No expense Added, nothing to show. Thank You")
        else:
            for expense in self.expenses:
                print(expense)


    def total_spent (self):
        if not self.expenses:
            print ("No expense Added, nothing to show. Thank You")
        else:
            total = sum(item.amount for item in self.expenses)
            print(f"total expense is {total}")

    def filter_by_category(self,category):
        if not self.expenses:
            print("No expense Added, nothing to show. Thank You")
        else:
            total = 0
            for item in self.expenses:
                if item.category == category:
                    total += item.amount

            if total == 0:
                print(f"Your category {category} is not found in the list")
            else:
                print(f"Category : {category}, had a total expense of {total}")



    def monthly_summary(self):
        if not self.expenses:
            print("No expense Added, nothing to show. Thank You")
        else:
            summary = {}
            for item in self.expenses:
                date_obj = datetime.strptime(item.expense_date, '%m/%d/%Y').date()
                month_year = date_obj.strftime('%B')+'-'+ date_obj.strftime('%Y')

                if month_year not in summary:
                    summary[month_year] = {}

                summary[month_year][item.category] = (summary[month_year].get(item.category, 0)
                                                      + item.amount)

            for month, categories in summary.items():
                print(f"\nMonth: {month}")
                for category, amount in categories.items():
                    print(f"  {category} : {amount}")
            return summary



    def min_max_expense(self):
        if not self.expenses:
            print("No expense Added, nothing to show. Thank You")
        else:
            item_list = self.monthly_summary()
            for month, categories in item_list.items():
                min_val = float('inf')
                min_item = None
                max_val = 0
                max_item = None
                for category, amount in categories.items():
                    if amount < min_val:
                        min_val = amount
                        min_item = category
                    if  amount >   max_val:
                        max_val = amount
                        max_item = category
                print(f"Minimum expense for the month of {month} was for  {min_item} :  {min_val}")
                print(f"Maximum expense for the month of {month} was for  {max_item} :  {max_val}")



    def save_to_csv(self):
        if not self.expenses:
            print("No expense Added, nothing to save. Thank You")
        else:
            field_names=['id','category','expense_type','amount','description','expense_date']
            output_file = 'C:\\Users\\debli\\python_practice\\TargetData\\My_Expense_Report.csv'

            with open (output_file,'w',newline='') as op_file:
                writer = csv.DictWriter(op_file, fieldnames=field_names)
                writer.writeheader()
                expenses_list = [asdict(expense) for expense in self.expenses]
                writer.writerows(expenses_list)
            print("expenses saved successfully")

    def load_from_csv(self):
        input_file = 'C:\\Users\\debli\\python_practice\\TargetData\\My_Expense_Report.csv'
        data_list = []
        with open (input_file,'r',newline='') as ip_file:
            reader = csv.DictReader(ip_file)
            for row in reader:
                data_obj = Expense (
                    id = (row["id"]),
                    category = row["category"],
                    expense_type = row["expense_type"],
                    amount  = float(row["amount"]),
                    description = row["description"],
                    expense_date = row["expense_date"]
                )

                data_list.append(data_obj)
            self.expenses = data_list

            print(f"Reading Data from your saved file")
            for items in data_list:
                print (items)




