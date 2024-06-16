import csv
csv_file = "C:/Users/PRABHA/Downloads/automobile.csv.csv"
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
