Monthly Sales Report Generator

This Python script generates a CSV report simulating monthly sales data for various items. It uses the following libraries:

csv: For reading and writing CSV files.
random: For generating random numbers (used for simulated sales).
datetime: For obtaining the current date.
pandas (optional): For more efficient CSV creation and data manipulation (if installed).
How it Works

Import Libraries: The script starts by importing the necessary modules.
generate_sales Function:
This function takes an initial inventory level as input.
It generates random sales values between 0 and the current inventory for four weeks.
Each sale amount is subtracted from the inventory for the next week.
The function returns a list of weekly sales figures.
create_csv Function:
Takes two file paths: categories_file (containing item data) and output_file (where the report will be saved).
Gets today's date in a formatted string.
Opens both files using a context manager (with open) for proper resource management.
Creates a CSV reader and writer object for working with the files.
Writes header rows:
Period information with the current date.
Column headers: Item Name, Category, Weekly Sales (Week #1 to #4).
Skips the first row of the categories_file (assuming it contains headers).
Iterates through each item row in the categories_file:
Extracts item name, category (handles missing categories with an empty string).
Generates random initial inventory (between 10 and 50).
Calls the generate_sales function to simulate weekly sales based on the inventory.
Writes a row to the output CSV: item name, category, followed by the weekly sales list.
Main Execution Block (if __name__ == "__main__":):
Sets default file paths:
categories_file: Replace with the actual path to your CSV file containing item data (two columns: Item Name and Category, optional header row).
output_file: Generates a filename with today's date in YYYY-MM-DD format.
Calls the create_csv function with the defined file paths.
Prints a confirmation message with the generated CSV filename.
Optionally (if pandas is installed), reads the created CSV using pd.read_csv and prints the DataFrame representation (useful for previewing the data).
Running the Script

Make sure you have Python and the required libraries (csv, random, datetime, pandas - optional) installed.
Save the script content as a Python file (e.g., monthly_sales_report.py).
In your terminal or command prompt, navigate to the directory where you saved the file.
Run the script using the python command: python monthly_sales_report.py
This will generate a new CSV file named Monthly Sales Report - YYYY-MM-DD.csv (where YYYY-MM-DD is the current date) in the same directory. The file will contain simulated sales data for the items listed in your categories.csv file.

Notes:

You'll need to replace categories_file with the actual path to your CSV file containing item data.
This script assumes a specific format for the categories.csv file (two columns: Item Name and Category). You might need to adjust the code if your file format differs.
The pandas library is used optionally for a more convenient preview of the generated data. If you don't have pandas installed, remove the last line in the if __name__ == "__main__": block.

share


more_vert
