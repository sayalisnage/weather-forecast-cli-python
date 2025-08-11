# Weather Forecast Application

A robust command-line application built in Python that provides local weather forecasts for any location in the United States. Users can search by either a ZIP code or a city and state combination, and choose their preferred temperature unit (Fahrenheit, Celsius, or Kelvin). The program is designed with a modular structure and includes comprehensive error handling to ensure a stable and user-friendly experience.

---

## Features
- Command-Line Interface: A console-based application that prompts the user for input and displays the weather forecast directly in the terminal.
- Flexible Location Search: Supports weather lookups by both a 5-digit ZIP code and a city/state combination.
- Multi-Unit Temperature Display: Allows users to choose between Fahrenheit, Celsius, and Kelvin for temperature readings.
- OpenWeatherMap API Integration: Fetches real-time weather data by performing a two-step API call: first for geolocation, and then for the weather forecast using the obtained latitude and longitude.
- Robust Error Handling: Uses try-except blocks to handle various HTTP errors (e.g., connection errors, bad requests) and invalid user input, preventing the program from crashing.
- Continuous Operation: The application runs in a loop, allowing the user to perform multiple weather lookups without restarting the program.
- Readable Output: Presents the weather forecast in a clean, human-readable format, including details like temperature, weather description, sunrise/sunset times, wind speed, and humidity.

---

## Installation and Usage
To run this program, you will need Python 3 and the requests library.

### Prerequisites
Install the required library using pip:
```bash
pip install requests
```
### Running the Program
1. Clone this repository or download the `weather_app.py` file.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the application with the following command:
```bash
python weather_app.py
```
5. Follow the on-screen prompts to enter your desired temperature unit and location (either by ZIP code or city/state).

---

## Code Structure
The application is structured into several modular functions to improve readability and maintainability:
- `main()`: The main loop that handles user interaction and calls other functions based on user input.
- `get_request(url, url_name)`: A generic function to handle API calls and perform robust HTTP error checking.
- `zipcode_lookup(zipcode)`: Performs the geolocation API call using a user-provided ZIP code.
- `city_lookup(city, state)`: Performs the geolocation API call using a user-provided city and state.
- `weather_lookup(lat, lon, unit)`: Fetches the weather data from the API using latitude, longitude, and the specified temperature unit.
- `pretty_print(weather, temp_unit, zipcode, statecode)`: Formats and prints the weather data to the console in a user-friendly format.

---

## Contact
For questions or collaboration, please reach out via [E-mail](mailto:sayalinage@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/sayali-nage-34303b136/).

---
