import random 
import csv
import datetime
today = datetime.date.today()
def create_csv():
    
     with open("monthly_sales_report.csv", 'r') as csvfile,open("inventory_restock.csv", 'w', newline='') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)
        next(reader)
        next(reader)
        writer.writerow([f"Date:{today}"])
        writer.writerow(["No","Productname","categories","Initialinventory","week #1","week #2","week #3","week #4","Total_sales","current_inventory","Restock_inventory"])
        for row in reader:
            total_sales = sum(int(val) for val in row[4:])
            current_inventory = int(row[3])-total_sales
            
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],total_sales,current_inventory,total_sales])
create_csv()
line = open("inventory_restock.csv")
print(line.read())