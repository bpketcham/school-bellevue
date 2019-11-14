###Define functions for printing output
def zip_print():
	zip = int(location)
	print("Zip = " + str(zip))
	zip_full = str(location +',US')
	qstring1 = "appid=" + api_key + "&zip=" + zip_full
	city_url = base_url + qstring1
	response = requests.get(city_url)
	print(json.dumps(response.json(), indent = 2))	
	
def city_print():
	city = str(location)
	print("City = " + city)
	city_full = str(city+',US')
	qstring1 = "appid=" + api_key + "&q=" + city_full
	city_url = base_url + qstring1
	response = requests.get(city_url)
	print(json.dumps(response.json(), indent = 2))		
		
###Define function to check if input is an invalid search location
def no_city():
	city = str(location)
	city_full = str(city+',US')
	qstring1 = "appid=" + api_key + "&q=" + city_full
	city_url = base_url + qstring1
	response = requests.get(city_url)
	if str(response.json()['cod']) == "404":
		return '404'
		
###Print welcome message
print("Welcome to the Weather Program")

zip = ''
city = ''

###Import modules to be used later
import requests
import json

###Set up base URL and API key to use in API call
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = '27ece24804599dfe618ea9348f381f6f'

while True:

	###Request location to search on
	location = input("\nPlease enter a city or ZIP code: ")
	
	###Check to make sure user entered something
	if location == '':
		print("You didn't enter anything. Please try again.")
		continue
	
	else:
		
		###Will use zip function if input is int, else will use city
		try:
			zip_print()
			
		except:
			###Prints message if status code comes back 404
			if no_city() == '404':
				print("\nSorry, that city/zip is not recognized")
			else:
				city_print()
			
		###Prompts the user to go again or exit program
		again = input("\nWould you like to search again (y/n)?")
		if again == "n":
			print("\nThank you for using the Weather Program! Goodbye")
			break
