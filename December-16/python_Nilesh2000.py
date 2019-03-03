import requests
api_address ='http://api.openweathermap.org/data/2.5/weather?appid=71ebadb9a97ad010c0248b72657635c5&q='
city1 = input("Enter City 1 Name : ")
city2 = input("Enter City 2 Name : ")
url1 = api_address + city1
url2 = api_address + city2
json_data1 = requests.get(url1).json()
json_data2 = requests.get(url2).json()
data1 = json_data1['main']['temp']
data2 = json_data2['main']['temp']
print("The differece in temperatures is : ")
print(data1 - data2)