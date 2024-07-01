import csv
import Yaml

def convert():
    with open("monthly_sales_report.csv","r") as infile:
        readfile=csv.DictReader(infile)

    data =list(readfile)
        
    with open("monthly_sales_report.yaml","w") as outfile:
        Yaml.dump(data,outfile)

convert()