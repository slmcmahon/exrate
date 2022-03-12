from bs4 import BeautifulSoup
import requests
import sys 

# Check if a currency is provided and default to USD if not
base_rate = sys.argv[1] if len(sys.argv) > 1 else 'USD'

# Line formatter for each exchange record being printed
def print_row(cols, sep):
    print("{0: <25} {1: >15}".format(cols[0], cols[1]))
    print(sep * 41)

# Load the web page that contains these rates and find the table
# that is defined with a css class with both 'tablesorter' and 
# 'ratesTable'.  Each TR in this table represents an exchange rate.
sd = requests.get("https://www.x-rates.com/table/?from={0}&amount=1".format(base_rate))
sp = BeautifulSoup(sd.content, 'html.parser')
table = sp.find('table', {"class": "tablesorter ratesTable"})
rows = table.findChildren('tr')

print('\r\n')
print_row(['Currency', 'Rate'], '=')

for row in rows:
    cells = row.findChildren('td')
    if len(cells) > 0:
        country = cells[0].text
        usd = cells[1].text
        print_row([country,usd], '-')
