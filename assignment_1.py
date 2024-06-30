import random 
import csv
from datetime import date

def random_value(inventory):
    sales=[]
    for i in range(4):
        sale=random.randint(0,inventory)
        inventory -= sale
        sales.append(sale)
    return sales
    
def create_csv():
     today = date.today().strftime("%d/%m/%Y")
     with open("categories.csv", 'r') as csvfile,open(f"monthly_sales_report - {date.today().strftime('%Y-%m-%d')}.csv", 'w', newline='') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)
        next(reader)
        writer.writerow([f"Period: {today} - {today}"])
        writer.writerow(["No","Productname","categories","Initialinventory","week #1","week #2","week #3","week #4"])
        for row in reader:
            No = row[0]
            Productname = row[1]
            categories = row[2]
            Initialinventory = row[3] 
            inventory=int(Initialinventory)
            sales = random_value(inventory)
            writer.writerow([No,Productname,categories,Initialinventory] + sales)
create_csv()
line = open(f"monthly_sales_report - {date.today().strftime('%Y-%m-%d')}.csv")
print(line.read())