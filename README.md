Climex Weather App

A cross-platform desktop weather application built with Python and Tkinter. This project demonstrates Python fundamentals, API integration, and GUI development.
Objective
Learn Python basics and API integration by building a functional weather application that retrieves real-time weather data.
Technologies
Language: Python 3.x
Libraries:

tkinter (GUI framework)
requests (HTTP API calls)
datetime (time handling)

API: OpenWeatherMap API
Features

Real-time weather data for any city worldwide
Current temperature, humidity, wind speed, and atmospheric pressure
Clean and intuitive user interface
Cross-platform support (Windows, macOS, Linux)
Error handling for invalid cities and network issues

Prerequisites

Python 3.8 or higher
pip package manager
OpenWeatherMap API key (free tier available)

Installation

Clone the repository:

bashgit clone https://github.com/yourusername/climex.git
cd climex

Install dependencies:

bashpip install -r requirements.txt

Get your API key:

Sign up at https://openweathermap.org/api
Navigate to API keys section
Copy your API key


Configure API key:

Open main.py
Replace YOUR_API_KEY_HERE with your actual API key:



python   self.API_KEY = "your_actual_api_key_here"
Usage
Run the application:
bashpython main.py
Enter a city name in the search box and click "Search" or press Enter to view weather information.
Building Executables
Create standalone executables for distribution:
Install PyInstaller:
bashpip install pyinstaller
Build for your platform:
bashpython -m PyInstaller --name=Climex --onefile --windowed main.py
Output location:

Windows: dist\Climex.exe
macOS: dist/Climex.app
Linux: dist/Climex

  
Free tier limits:

1,000 API calls per day
Current weather data access
Global coverage

Data units: Metric (Celsius, meters/second)
Learning Outcomes

Python GUI development with Tkinter
REST API integration with requests library
Error handling and user input validation
Cross-platform application development
Application packaging and distribution
