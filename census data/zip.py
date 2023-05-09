import requests
import csv

url = 'https://api.census.gov/data/2021/cbp?get=NAICS2017_LABEL,EMP,NAME&for=zipcode:*&in=state:36%20county:005&NAICS2017=54&NAICS2017=62&key=bbc2089798cdeb0b6f002ab391bbbb9194c5120b'
headers = {'Accept': 'text/csv'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    csv_data = response.text
    with open('zipcode_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in csv_data.split('\n'):
            writer.writerow(row.split(','))
else:
    print(f'Request failed with status code {response.status_code}')
