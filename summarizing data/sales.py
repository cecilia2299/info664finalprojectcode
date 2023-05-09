import csv


with open('GarmentDistrict.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)

   
    count_dict = {}

  
    for row in csv_reader:
        sales = row[15] 
        value = row[12] 
        key = (sales)
        if key in count_dict:
            if value in count_dict[key]:
                count_dict[key][value] += 1
            else:
                count_dict[key][value] = 1
        else:
            count_dict[key] = {value: 1}


with open('sales.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)


    csv_writer.writerow([ 'Location Sales Volume Range', 'Type of Business', 'Count'])


    for (sales), counts in count_dict.items():
        for value, count in counts.items():
            csv_writer.writerow([sales, value, count])