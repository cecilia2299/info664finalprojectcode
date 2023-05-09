import csv

# Open input CSV file
with open('GarmentDistrict.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)

    # Skip header row
    header = next(csv_reader)

    # Create dictionary to store counts
    count_dict = {}

    # Loop through rows and count values in specified column
    for row in csv_reader:
        overalltype = row[12] # Replace 0 with index of first grouping column
        naics = row[11] # Replace 1 with index of second grouping column
        value = row[11] # Replace 2 with index of column to summarize
        key = (overalltype, naics)
        if key in count_dict:
            if value in count_dict[key]:
                count_dict[key][value] += 1
            else:
                count_dict[key][value] = 1
        else:
            count_dict[key] = {value: 1}

# Open output CSV file and write counts
with open('naics.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)

    # Write header row
    csv_writer.writerow(['Overall Category', 'Primary NAICs Description ', 'Value', 'Count'])

    # Loop through counts and write to output file
    for (group1, group2), counts in count_dict.items():
        for value, count in counts.items():
            csv_writer.writerow([group1, group2, value, count])