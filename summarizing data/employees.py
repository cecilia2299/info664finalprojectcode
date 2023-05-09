import csv


with open('GarmentDistrict.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)

   
    count_dict = {}

  
    for row in csv_reader:
        employees = row[13] 
        value = row[12] 
        key = (employees)
        if key in count_dict:
            if value in count_dict[key]:
                count_dict[key][value] += 1
            else:
                count_dict[key][value] = 1
        else:
            count_dict[key] = {value: 1}


with open('employees.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)


    csv_writer.writerow([ 'Employees', 'Type of Business', 'Count'])


    for (employees), counts in count_dict.items():
        for value, count in counts.items():
            csv_writer.writerow([employees, value, count])