# Your code goes here
import csv

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleanme-clean.csv', 'w')
 
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()

for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['city'] = row['city'].replace('&nbsp;',' ')
    row['zip'] = row['zip'].zfill(5)
    if float(row['amount']) > 1000.0:
        print row
        writer.writerow(row)