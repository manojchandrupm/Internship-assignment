import csv
import yaml

with open("monthly_sales_report.csv","r") as infile:
    readfile=csv.reader(infile)

    data =[]
    for row in readfile:
        data.append(row)
        
with open("monthly_sales_report.yaml","w") as outfile:
    yaml.dump(data,outfile)