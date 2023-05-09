import csv

naics = {}

with open('CombinedData.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        category = row[12] 
        naic = row[11]
        new_category = row[10] 
        if category not in naics:
            naics[category] = {}
        if new_category not in naics[category]: 
            naics[category][new_category] = {}
        if naic not in naics[category][new_category]:
            naics[category][new_category][naic] = {}
        zip_code = row[7] 
        if zip_code not in naics[category][new_category][naic]:
            naics[category][new_category][naic][zip_code] = 0
        naics[category][new_category][naic][zip_code] += 1

with open('thenaicscount.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Overall Category', 'NAICs Category', 'NAICs', 'Zip Code', 'Count']) 
    for category, new_categories in naics.items():
        for new_category, naic_counts in new_categories.items():
            for naic, zip_code_counts in naic_counts.items():
                for zip_code, count in zip_code_counts.items():
                    writer.writerow([category, new_category, naic, zip_code, count])
