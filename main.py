import csv

# Open the CSV file
with open('kandydaci_utf8.csv', newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile, delimiter=';')

    # Iterate over each row in the CSV file
    for row in reader:
        # Print each row
        print(row)
        break
    print('-------------------')
    for row in reader:
    # Print each row
        print(row)
        break