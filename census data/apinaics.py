import csv
import requests

url = 'https://api.census.gov/data/2021/cbp?get=NAICS2017_LABEL,EMP,ESTAB,PAYANN,NAME&for=county:*&in=state:36&NAICS2017=541490&NAICS2017=424320&NAICS2017=424330&NAICS2017=423940&NAICS2017=423220&NAICS2017=313&NAICS2017=314&NAICS2017=424310&NAICS2017=315&NAICS2017=316&NAICS2017=339914&NAICS2017=339993&&key=bbc2089798cdeb0b6f002ab391bbbb9194c5120b'
headers = {'Accept': 'text/csv'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    csv_data = response.text

    with open('thecounty_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in csv_data.split('\n'):
            writer.writerow(row.split(','))
else:
    print(f'Request failed with status code {response.status_code}')
