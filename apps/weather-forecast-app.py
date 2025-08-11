# DSC 510_Introduction_To_Programming_Winter_2022
# This is Final Term Project (Week 9 through 12)
# Date Created (Ver1): 2/8/2023
# Author: Sayali Nage

# Change#:1
# Change Requested by: Michael Eller_ Term Project 12.1
# Change(s) Made: Changes for Term Project 12.1 added
# Date of Change: 2/14/2023
# Author: Sayali Nage
# Date Moved to Production: 3/3/2023

# Term Project Requirement and Notes(lines 14-62)
# BASIC
# Use Python 3
# Your program must include a header as in previous weeks.
# Your program must have a properly defined main method and a properly defined call to main.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
# Use comments within the application where appropriate in order to document what the program is doing.
# Comments should add value to the program and describe important elements of the program.
# Be creative.  This assignment is a real-world program.
# Use it as an opportunity to improve your knowledge and showcase what you’ve learned.

# INPUT
# You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
# Create a Python Application which asks the user for their zip code or city
# (Your program must perform both a city and a zip lookup).
# Your program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.
# You must ask the user which they want to perform with each iteration of the program.
# Make sure that your program allows a user to do a zip code weather lookup and a city/state lookup.
# You must give them the option and I will test both.
# For city, you should ask the user to enter a state,
# otherwise there’s no way to distinguish between Omaha TX, Omaha AR, and Omaha NE.
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user.
# Your program should never crash with bad user input.

# REQUEST, GET, FUNCTIONS
# Use the Requests library in order to request data from the webservice.
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
# You MUST do a GEO Lookup first then do a weather lookup using the latitude and longitude.
# This will require you to do 2 API calls.
# One call will be to obtain the LAT and LON and the other will be to get the weather using the LAT and LON.
# READ all the OpenWeather GEOCode and Weather Lookup API documentation.
# Most of the questions you have can be answered by the API documentation.
# Use functions including a main function and a properly defined call to main. You should have multiple functions.

# ERROR HANDLING
# Use try blocks when establishing connections to the webservice.
# Use Try blocks to ensure that your request was successful.
# If the connection was not successful display a message to the user.
# You must print a message to the user indicating whether or not the connection was successful.
# Make sure that your try blocks are solid.  Don’t include huge blocks of code in the try blocks.
# Don’t use generic exceptions.
# Take a look at the request documentation on the various exceptions you can catch for HTTP connections.
# You should have specific exceptions with meaningful messages for the end user to make adjustments.
# Make sure you have request specific exceptions.  Your code should not throw any unhandled exceptions.

# OUTPUT
# Your program must display the weather information in a READABLE format to the user.
# Display the weather forecast in a readable format to the user.
# Do not display the weather data in Kelvin, since this is not readable to the average person.


import datetime
import requests

API_KEY = '0828b29abd27cf984a1083f0103fc2c2'

US_STATES_DICT = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AZ': 'Arizona', 'CA': 'California',
                  'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware',
                  'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois',
                  'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts',
                  'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri',
                  'MS': 'Mississippi', 'MT': 'Montana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska',
                  'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York',
                  'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island',
                  'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
                  'VA': 'Virginia', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia',
                  'WY': 'Wyoming'}

RED_COLOR = '\033[31m'
END_COLOR = '\033[m'
GREEN_COLOR = '\033[32m'


def get_request(url, url_name):
    # Requests data from webservice, takes care of HTTP Errors
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"\n{RED_COLOR}An HTTP Error has occurred for {url_name}{END_COLOR}")
    except requests.exceptions.ConnectionError:
        print(f"\n{RED_COLOR}Connection Unsuccessful for {url_name}{END_COLOR}")
    except requests.RequestException:
        print(f"\n{RED_COLOR}An Error has occurred for {url_name}{END_COLOR}")
    else:
        return response
    finally:
        print(f"\nHTTP request for {url_name} is complete")


def zipcode_lookup(zipcode):
    # Returns latitude and longitude from user input: zipcode
    url = 'http://api.openweathermap.org/geo/1.0/zip?zip=' + str(zipcode) + ',US' + '&appid=' + API_KEY
    zipcode_res = get_request(url, 'Zipcode-lookup')
    if zipcode_res is not None:
        print(f"{GREEN_COLOR}Zipcode-lookup is Successful{END_COLOR}")
        return {"lat": zipcode_res.json()['lat'], "lon": zipcode_res.json()['lon']}
    else:
        print(f"{RED_COLOR}Zipcode Not found{END_COLOR}")


def city_lookup(city, state):
    # Returns latitude and longitude from user input: city & state
    url = 'http://api.openweathermap.org/geo/1.0/direct?q=' + city + ',' + state + ',US&limit=1' + '&appid=' + API_KEY
    response = get_request(url, 'City-lookup')
    if response is not None:
        geo_res = response.json()
        # This condition is needed because the api will try to do partial search on city and will return multiple
        # results with different combination of city and state.
        if len(geo_res) > 0 and city.lower() == str(geo_res[0]['name']).lower() and \
                str(US_STATES_DICT[state]).lower() == str(geo_res[0]['state']).lower():
            print(f"{GREEN_COLOR}City-lookup is Successful{END_COLOR}")
            return {"lat": geo_res[0]['lat'], "lon": geo_res[0]['lon']}
        else:
            print(f'{RED_COLOR}City & State combination not found{END_COLOR}')
    else:
        print(f'{RED_COLOR}City & State combination not found{END_COLOR}')


def weather_lookup(lat, lon, unit):
    # Returns weather data from latitude & longitude with specified temperature units
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + \
          '&appid=' + API_KEY + '&units=' + unit
    response = get_request(url, 'Weather-lookup')
    if response is not None:
        print(f"{GREEN_COLOR}Weather-lookup is Successful{END_COLOR}")
        return response.json()
    else:
        print(f"{RED_COLOR}Weather not found{END_COLOR}")


def pretty_print(weather, temp_unit, zipcode, statecode):
    # Nicely displays output weather data in a readable format
    city_name = weather['name']
    current_temp = weather['main']['temp']
    local_date = datetime.datetime.utcfromtimestamp(weather['dt'] + weather['timezone']).strftime('%A, %b. %d, %Y')
    local_time = datetime.datetime.utcfromtimestamp(weather['dt'] + weather['timezone']).strftime('%I:%M %p')
    weather_main = weather['weather'][0]['main']
    sunrise_time = datetime.datetime.utcfromtimestamp(weather['sys']['sunrise'] + weather['timezone']).strftime(
        '%I:%M %p')
    sunset_time = datetime.datetime.utcfromtimestamp(weather['sys']['sunset'] + weather['timezone']).strftime(
        '%I:%M %p')
    weather_description = weather['weather'][0]['description'].capitalize()
    feels_like = weather['main']['feels_like']
    max_temp = weather['main']['temp_max']
    min_temp = weather['main']['temp_min']
    humidity = weather['main']['humidity']
    wind_speed = weather['wind']['speed']
    visibility = weather['visibility']
    pressure = weather['main']['pressure']
    location_str = '\n\nShowing weather for ' + city_name + ', '
    if zipcode is not None:
        location_str += zipcode
    if statecode is not None and len(US_STATES_DICT[statecode]) > 0:
        location_str += US_STATES_DICT[statecode]
    location_str += ', USA'
    print(location_str)
    temperature_unit = get_temperature_unit(temp_unit)

    print(f'\nCurrent temperature in {city_name} is {current_temp}{temperature_unit}')
    print(f'Local Date\t: {local_date}')
    print(f'Local Time\t: {local_time}')
    print(f'Weather\t\t: {weather_main}')
    print(f'Sunrise\t\t: {sunrise_time}')
    print(f'Sunset\t\t: {sunset_time}')
    if feels_like < current_temp:
        print(f'\nFeels like {feels_like}{temperature_unit} Wind is making it feel cooler')
    elif feels_like == current_temp:
        print(f'\nFeels like {feels_like}{temperature_unit} Similar to the actual temperature')
    else:
        print(f'\nFeels like {feels_like}{temperature_unit}')
    print(f'Description\t: {weather_description}')
    print(f'Max temp\t: {max_temp}{temperature_unit} \nMin temp\t: {min_temp}{temperature_unit}')
    speed_unit = 'meter/sec'
    if temp_unit == 'imperial':
        speed_unit = 'miles/hour'
    print(f'Humidity\t: {humidity}%')
    print(f'Wind Speed\t: {wind_speed} {speed_unit}')
    print(f'Visibility\t: {visibility} meter')
    print(f'Pressure\t: {pressure} hPa')


def print_state_list():
    # Nicely prints list of states
    state_cnt = 0
    padding = 25
    for item in US_STATES_DICT:
        option = item + ':' + US_STATES_DICT[item]
        print(option.ljust(padding, ' '), end='')
        state_cnt += 1
        if state_cnt % 7 == 0:
            print()


def geo_weather_lookup(geo_res, unit, zipcode, state):
    # Refactored function used by zipcode and city lookup functions
    if geo_res is not None:
        weather_res = weather_lookup(geo_res['lat'], geo_res['lon'], unit)
        if weather_res is not None:
            pretty_print(weather_res, unit, zipcode, state)


def get_temperature_unit(unit):
    # Returns selected temperature input to be shown as text on console
    if unit == 'imperial':
        temperature_unit = '°F'
    elif unit == 'metric':
        temperature_unit = '°C'
    else:
        temperature_unit = '°K'
    return temperature_unit


def main():
    # This is main body of program which includes user controls and loops to call respective functions in code
    print("*** Welcome to 'Weather Today' Application! ***")
    print('A quick weather lookup for all US locations online...')
    print("The 'Weather Today' application provide a nationwide local weather forecast for cities "
          'from the most accurate weather forecasting technology featuring weather reports.')
    while True:
        try:
            temperature_input = input("\nEnter 'C' to view temperature in °Celsius, 'F' to view temperature in "
                                      "°Fahrenheit,"
                                      " 'K' to view temperature in Kelvin, \n'T' to terminate the program "
                                      "(Default temperature will be in °Fahrenheit) : ")

            if temperature_input.upper() == 'F':
                temperature_input = 'imperial'
            elif temperature_input.upper() == 'C':
                temperature_input = 'metric'
            elif temperature_input.upper() == 'K':
                temperature_input = 'standard'
            elif temperature_input.upper() == 'T':
                print('Good bye!')
                break
            else:
                print('Invalid input for temperature unit detected, showing temperature in °F')
                temperature_input = 'imperial'
            geocode_option = input('Please enter ("A: ZipCode, B: City, T: Terminate)"): ')

            if geocode_option.upper() == 'A':
                zipcode_input = input('Enter Zip code: ')
                zipcode_res = zipcode_lookup(zipcode_input)
                geo_weather_lookup(zipcode_res, temperature_input, zipcode_input, None)

            elif geocode_option.upper() == 'B':
                city_input = input('Enter city: ')
                print_state_list()
                while True:
                    state_input = input('\nEnter State Code from the above list: ').upper()
                    try:
                        if state_input.upper() == 'R':
                            break
                        if len(US_STATES_DICT[state_input]) >= 0:
                            city_res = city_lookup(city_input, state_input)
                            geo_weather_lookup(city_res, temperature_input, None, state_input)
                            break
                    except KeyError:
                        print(f'{RED_COLOR}Invalid State Code.{END_COLOR}')

            elif geocode_option.upper() == 'T':
                print('Good bye!')
                break
            else:
                print(f'{RED_COLOR}Invalid Input{END_COLOR}')
        except ValueError:
            print(f'\n{RED_COLOR}Invalid Input Entered! Please try again{END_COLOR}')


if __name__ == '__main__':                          # Call to main
    main()
