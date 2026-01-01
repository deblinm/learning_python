import os
def calculation(inp1, inp2, operand):
    if operand == "+":
        return inp1 + inp2
    elif operand == "-":
        return inp1 - inp2
    elif operand == "*":
        return inp1 * inp2
    elif operand == "/":
        if inp2 == 0:
            print("You can't divide by zero")
            return None
        else:
            return inp1 / inp2

def file_operation(text,operation):
    if operation == "write":
        with open('../Files/operations.txt', "a") as file:
            file.write(text+'\n')
    elif operation == "read":
        with open('../Files/operations.txt', "r") as file:
            content=file.read()
        return content
    elif operation == "delete":
        if os.path.exists('../Files/operations.txt'):
            with open('operations.txt', 'w') as file:
                pass
            print("Operations memory cleared")
        else:
            print("Nothing to delete")

def choice():
    user_input=input("Do you want to continue(y/n)? " ).strip().lower()
    if user_input == "y":
        user_choice=True
    else:
        user_choice=False
    return user_choice

user_choice=True
print("Simple calculator performs the below operations:\n")
while True:

    if user_choice:
        print("1. Type 1 for Addition")
        print("2. Type 2 for Subtraction")
        print("3. Type 3 for Division")
        print("4. Type 4 for Multiplication")
        print("5. Type 5 for View History")
        print("6. Type 6 for Clear History")
        print("7. Type 7 for Exit")
        operation=int(input("\nPlease select the operation you want to perform from the list: ").strip().lower())

    if not (1 <= operation < 8) or not operation:
            print("\n Please enter a valid operation from the list only. As of now simple calculator only supports these 4 options \n")
            user_choice=True
            continue
    elif 1 <= operation < 5:
            first_input = int(input("Enter the first number: "))
            second_input = int(input("Enter the second number: "))
            if operation == 1:
                sum=calculation(first_input, second_input,"+")
                file_operation(f"{first_input}+{second_input}={sum}","write")
                print(f"The sum of {first_input} and {second_input} is {sum}")
                choice()
            elif operation == 2:
                sub=calculation(first_input, second_input,"-")
                file_operation(f"{first_input}-{second_input}={sub}","write")
                print(f"The difference of {first_input} and {second_input} is {sub}")
                choice()
            elif operation == 3:
                div=calculation(first_input, second_input,"/")
                file_operation(f"{first_input}/{second_input}={div}","write")
                print(f"The division of {first_input} and {second_input} is {div}")
                choice()
            elif operation == 4:
                mul=calculation(first_input, second_input,"*")
                file_operation(f"{first_input}*{second_input}={mul}","write")
                print(f"The multiplication of {first_input} and {second_input} is {mul}")
                choice()
    elif operation==5:
            file_content=file_operation("","read")
            print(file_content)
            choice()
    elif operation==6:
            file_operation("","delete")
            choice()
    elif operation==7:
            print("\nThank you for using SimpleCalculator. See you soon!")
            choice=False
            break



