import csv

file1 = []
file2 = []
with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        file1.append(row)
with open("unit_converted_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        file2.append(row)
headers_1 = file1[0]
planet_data_1 = file1[1:]

headers_2 = file2[0]
planet_data_2 = file2[1:]
headers = headers_1 + headers_2
planet_data = []

for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
