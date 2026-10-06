import pandas as pd 
import requests 

data = {
    'name': ['A', 'B', 'C'],
    'age': [30, 20, 20],
    'address': ['Pune', 'Mumbai', 'CSN']
}

print('Student Details')
df = pd.DataFrame(data)
print(df)

print('API data')
response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())