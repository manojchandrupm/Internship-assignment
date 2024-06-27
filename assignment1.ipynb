{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV file created: Monthly Sales Report - 2024-06-27.csv\n",
      "                                                                       Period: 27/06/2024 - 27/06/2024\n",
      "Item Name Category           Week #1 Sales Week #2 Sales Week #3 Sales                   Week #4 Sales\n",
      "1         Ballpoint Pens     19            1             7                                           0\n",
      "2         Gel Pens           6             2             1                                           1\n",
      "3         Fountain Pens      22            12            2                                           3\n",
      "4         Mechanical Pencils 18            0             1                                           1\n",
      "...                                                                                                ...\n",
      "96        Fax Paper Rolls    14            20            10                                          5\n",
      "97        Business Envelopes 2             5             1                                           2\n",
      "98        A4 Paper           10            9             6                                           0\n",
      "99        Legal Pads         23            0             1                                           0\n",
      "100       Report Covers      9             24            0                                           6\n",
      "\n",
      "[101 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "import csv # This module is used for reading and writing data in CSV format.\n",
    "import random # This module provides functions for generating random numbers, which are used to simulate sales data in this case.\n",
    "from datetime import date # This imports the date function from the datetime module. It's used to get the current date for the report.\n",
    "import pandas as pd # This imports the pandas library as pd. Pandas is a powerful library for data manipulation and analysis. It's used here to create a DataFrame from the generated data and write it to the CSV file more efficiently.\n",
    "\n",
    "def generate_sales(inventory):\n",
    "  \n",
    "  sales = []\n",
    "  for _ in range(4):\n",
    "    # Generate random sales between 0 and current inventory\n",
    "    sale = random.randint(0, inventory)\n",
    "    # Reduce inventory by the sales for the next week\n",
    "    inventory -= sale\n",
    "    sales.append(sale)\n",
    "  return sales\n",
    "\n",
    "def create_csv(categories_file, output_file):\n",
    "  \n",
    "  # Get today's date\n",
    "  today = date.today().strftime(\"%d/%m/%Y\")\n",
    "\n",
    "  with open(categories_file, 'r') as csvfile, open(output_file, 'w', newline='') as outfile:\n",
    "    reader = csv.reader(csvfile)\n",
    "    writer = csv.writer(outfile)\n",
    "\n",
    "    # Write header rows\n",
    "    writer.writerow([f\"Period: {today} - {today}\"])\n",
    "    writer.writerow([\"Item Name\", \"Category\", \"Week #1 Sales\", \"Week #2 Sales\", \"Week #3 Sales\", \"Week #4 Sales\"])\n",
    "    next(reader)\n",
    "\n",
    "    # Read item data and generate sales\n",
    "    for row in reader:\n",
    "      # Handle potential extra columns by assigning remaining values to a list\n",
    "      item_name = row[0]  \n",
    "      category = row[1] if len(row) > 1 else '' # Handle cases with missing category\n",
    "      inventory = random.randint(10, 50)  # Random initial inventory\n",
    "      sales = generate_sales(inventory)\n",
    "      writer.writerow([item_name, category] + sales)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "  categories_file = \"categories.csv\"  # Replace with your actual file path\n",
    "  output_file = f\"Monthly Sales Report - {date.today().strftime('%Y-%m-%d')}.csv\"\n",
    "  create_csv(categories_file, output_file)\n",
    "  print(f\"CSV file created: {output_file}\")\n",
    "  print(pd.read_csv(output_file))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
