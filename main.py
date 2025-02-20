import sqlite3
import datetime

conn=sqlite3.connect("expenses.db")
cur=conn.cursor()


while True:
    print("select an option:")
    print("1.Enter new expense")
    print("2.View expense summary")

    choice =int(input())

    if choice==1:
        date=input("Enter the date of the expense (yyyy-mm-dd): ")
        description=input("Enter the description of the expense: ")
        cur.execute("SELECT DISTINCT  category FROM expenses")


        categories=cur.fetchall()

        print("Select a category by number: ")
        for idx,category in enumerate(categories):

            print(f"{idx + 1}.{category[0]}")
        print(f"{len(categories)+ 1}.Create a new category")

        category_choice=int(input())
        if category_choice ==len(categories) +1:
            category=input("Enter the new category name: ")
        else:
            category=categories[category_choice-1][0]

        price=input("Enter the price of the expense:")

        cur.execute("INSERT INTO expenses(Date,description,category,price)VALUES (?,?,?,?)",(date,description,category,price))
        conn.commit()

    if choice ==2:
        print("Select an expense :")
        print("1.View all expenses ")
        print("2.View monthly expense by category")

        view_choice=int(input())
        if view_choice==1:
            cur.execute("SELECT * FROM expenses")
            expenses=cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice==2:
            month=input("Enter the month(mm): ")
            year=input("Enter the year(yyyy): ")
            cur.execute("SELECT category,SUM(price) FROM expenses WHERE strftime('%m',Date)=? AND  strftime('%y',Date)=?GRUO BY category,(month,year) " )
            expenses=cur.fetchall()
            for expense in expenses:
                print(f"Category:{expense[0]},Total:{expense[1]}")

        else:
            exit()

    else:exit()

    repeat=input("Would you like to do something else(y/n)?\n")
    if repeat.lower() !="y":
         break

    
    conn.close()



        

