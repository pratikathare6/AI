import os
from helpers import calculate_total,format_currency

print('current directory:',os.getcwd())

data = calculate_total(20,200)
print(data)

data_path = 'Data/sales.csv'

if os.path.exists(data_path):
    print(f'found {data_path}')
else:
    print(f'not found {data_path}')
    print('make sure you are running from sales-analysis folder!')