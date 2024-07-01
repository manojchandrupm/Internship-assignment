## Assignment 1:
  #### Tittle: Randomized sample data (assignment_1.py)
### Description :
   This Python script generates a monthly sales report in CSV format, simulating random weekly sales for each product listed in a provided "categories.csv" file.It incorporates functions for:

- Generating random weekly sales values within the initial inventory limit.
- Creating a new CSV file named monthly_sales_report .csv.
- Writing a header row with the report period, product details, and weekly sales columns.
- Iterating through each product in the "categories.csv" and generating a row with initial inventory and random weekly sales.

### Usage
#### Prerequisites:

- Python 3.x (ensure you have it installed)
- csv module (comes pre-installed with Python 3)
- random module (comes pre-installed with Python 3)
- datetime module (comes pre-installed with Python 3)
#### Running the Script:

- Save the code as a Python file (e.g., monthly_sales_report_generator.py).
- Open a terminal or command prompt and navigate to the directory where you saved the file.
- Execute the script using the python command:
#### Output:
- The script will create a new CSV file named monthly_sales_report -(today date).csv in the same directory.
- This CSV file will contain the simulated sales report for the current month.
#### Input File
- The script expects a CSV file named "categories.csv" in the same directory.
- which is provided in the Internship_assignment repository.


### Documentation
### 1. Imports:
- random: Used for generating random sales values.
- csv: Used for reading and writing CSV files.
- from datetime import date: Used for getting the current date.

### 2. Functions:
#### random_value(inventory):
- Takes the initial inventory level as input.
- Creates an empty list sales to store weekly sales.

- Iterates 4 times (representing 4 weeks):
- Generates a random sale value between 0 and the current inventory using random.randint().
- Subtracts the sale value from the inventory (inventory -= sale).
- Appends the sale value to the sales list.
- Returns the list of weekly sales.
#### create_csv():
- Gets the current date in "%d/%m/%Y" format using date.today().strftime("%d/%m/%Y").
- Opens two CSV files:
 "categories.csv" in read mode ('r').
  A new file named "monthly_sales_report - {date}.csv" (formatted using today's date) in write mode ('w').
- Creates CSV reader and writer objects.
- Skips the header row of the "categories.csv" using next(reader).
- Writes the report header to the new CSV file:
 "Period: {start_date} - {end_date}" (using the current date).
 "No", "Productname", "categories", "Initialinventory", "week #1", "week #2", "week #3", "week #4".
- Iterates through each row in the "categories.csv" file:
- Extracts product details: No, Productname, categories, Initialinventory.
- Converts Initialinventory to an integer.
- Generates weekly sales using random_value(inventory).
- Writes a new row to the report CSV combining product information and weekly sales.
- Closes the CSV files.
### 3. Report Generation and Printing:

- Opens the newly created report CSV file in read mode.
- Reads the entire contents of the file using line.read().
- Prints the report contents (likely for verification purposes).

## Assignment 2:
  #### Title: Monthly Sales Report and Inventory Restock Automation (assignment_2.py)

### Description:

- This Python script automates the creation of a new CSV file named "inventory_restock.csv" based on data from an existing "monthly_sales_report.csv" file. It calculates total sales for each product, updates current inventory levels, and suggests a restock quantity based on the total sales.

### Features:

- Reads sales data from "monthly_sales_report.csv".
- Calculates total sales per product for the month.
- Updates current inventory by subtracting total sales.
- Recommends a restock quantity equal to the total sales (adjustable).
- Creates a new "inventory_restock.csv" file with the following columns:
- Date (automatically set to the current date)
- No ,Productname ,Categories ,Initialinventory
- Week #1 ,Week #2 ,Week #3 ,Week #4 (copied from "monthly_sales_report.csv")
- Total_sales (calculated)
- Current_inventory (calculated)
- Restock_inventory (recommended restock quantity)




