import json
import os
import datetime

def load_expenses():
    expenses=[]
    if os.path.exists("expenses.json"):
        with open('expenses.json','r') as file:
            expenses=json.load(file)
    return expenses
        
def show(expenses):
    if expenses:
        for expense in expenses:
            for key, value in expense.items():
                print(f"{key}: {value}")

    else:
        print('No expenses recorded yet')
        

def save_expenses(expenses):
    with open('expenses.json','w') as file:
        json.dump(expenses,file,indent=4)

def add_expense():
    expenses=load_expenses()
    while True:
        try:
            amount=float(input("Enter the amount of expense: "))
            break
        except:
            print("Invalid amount. Please enter a valid number")
    description= input("Enter the description of expense: ")
    category=input("Enter the category: ")
    date=datetime.datetime.now().strftime('%d-%m-%y')
    expense={'amount':amount,'description':description,'category':category,'date':date}
    expenses.append(expense)
    save_expenses(expenses)
    print('Expense saved succesfully.\n')

def month_wise(expenses):
    month_wise_expenses={}
    for expense in expenses:
        month=expense['date'].split('-')[1]
        if month not in month_wise_expenses:
            month_wise_expenses[month]=0
        month_wise_expenses[month]+=expense['amount']
    for month,total in month_wise_expenses.items():
        print(f"Month:{month}  Expenses:${total}")

def category_wise(expenses):
    category_wise_expenses={}
    for expense in expenses:
        category=expense['category']
        if category not in category_wise_expenses:
            category_wise_expenses[category]=0
        category_wise_expenses[category]+=expense['amount']
    for category,total in category_wise_expenses.items():
        print(f"Category:{category}  Expenses:${total}")



def __main__():
    
    
    while True:
        expenses=load_expenses()
        print("1.Add Expense")
        print('2.View Expense')
        print('3.Monthly Expense')
        print('4.Caterogry Expenditure')
        print('5.Exit')
        choice=int(input("Enter your choice : "))
        if choice==1:
            add_expense()
        elif choice==2:
            show(expenses)
        elif choice==3:
            month_wise(expenses)
        elif choice==4:
            category_wise(expenses)
        elif choice==5:
            print('Exited')
            break
    

if __name__=='__main__':
    __main__()




