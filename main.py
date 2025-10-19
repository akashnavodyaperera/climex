import tkinter as tk
from tkinter import messagebox, ttk
import requests
from datetime import datetime

class ClimexWeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Climex Weather App")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # API key
        self.API_KEY = "e6aa859e1350f9925cdcc0099e2a2668"
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
        
        # Configure colors
        self.bg_color = "#2C3E50"
        self.fg_color = "#ECF0F1"
        self.accent_color = "#3498DB"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="🌤️ Climex Weather",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=20)
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg=self.bg_color)
        search_frame.pack(pady=10)
        
        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            width=25,
            relief=tk.FLAT,
            bg="#34495E",
            fg=self.fg_color,
            insertbackground=self.fg_color
        )
        self.city_entry.pack(side=tk.LEFT, padx=5, ipady=8)
        self.city_entry.bind('<Return>', lambda e: self.get_weather())
        
        search_btn = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg=self.accent_color,
            fg=self.fg_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.get_weather,
            width=10
        )
        search_btn.pack(side=tk.LEFT, padx=5, ipady=5)
        
        # Weather Display Frame
        self.weather_frame = tk.Frame(self.root, bg=self.bg_color)
        self.weather_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Info label
        info_label = tk.Label(
            self.root,
            text="Enter a city name and press Search",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#95A5A6"
        )
        info_label.pack(side=tk.BOTTOM, pady=10)
    
    def get_weather(self):
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        if self.API_KEY == "e6aa859e1350f9925cdcc0099e2a2668":
            messagebox.showerror(
                "API Key Error",
                "Please replace 'e6aa859e1350f9925cdcc0099e2a2668' with your actual OpenWeatherMap API key!"
            )
            return
        
        # Show loading
        self.clear_weather_display()
        loading_label = tk.Label(
            self.weather_frame,
            text="Loading...",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.fg_color
        )
        loading_label.pack(pady=50)
        self.root.update()
        
        try:
            # Make API request
            params = {
                'q': city,
                'appid': self.API_KEY,
                'units': 'metric'  # Use 'imperial' for Fahrenheit
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 404:
                self.show_error("City not found! Please check the spelling.")
            elif response.status_code == 401:
                self.show_error("Invalid API key! Please check your configuration.")
            else:
                self.show_error(f"Error: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            self.show_error("No internet connection!")
        except requests.exceptions.Timeout:
            self.show_error("Request timed out. Please try again.")
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")
    
    def display_weather(self, data):
        self.clear_weather_display()
        
        # City name and country
        city_label = tk.Label(
            self.weather_frame,
            text=f"{data['name']}, {data['sys']['country']}",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        city_label.pack(pady=10)
        
        # Current time
        time_label = tk.Label(
            self.weather_frame,
            text=datetime.now().strftime("%A, %I:%M %p"),
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#95A5A6"
        )
        time_label.pack()
        
        # Temperature
        temp = data['main']['temp']
        temp_label = tk.Label(
            self.weather_frame,
            text=f"{temp:.1f}°C",
            font=("Arial", 48, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        temp_label.pack(pady=10)
        
        # Weather description
        description = data['weather'][0]['description'].title()
        desc_label = tk.Label(
            self.weather_frame,
            text=description,
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.accent_color
        )
        desc_label.pack()
        
        # Details Frame
        details_frame = tk.Frame(self.weather_frame, bg=self.bg_color)
        details_frame.pack(pady=20)
        
        # Create detail boxes
        details = [
            ("Feels Like", f"{data['main']['feels_like']:.1f}°C"),
            ("Humidity", f"{data['main']['humidity']}%"),
            ("Wind Speed", f"{data['wind']['speed']} m/s"),
            ("Pressure", f"{data['main']['pressure']} hPa")
        ]
        
        for i, (label, value) in enumerate(details):
            detail_box = tk.Frame(details_frame, bg="#34495E", relief=tk.FLAT)
            detail_box.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")
            
            tk.Label(
                detail_box,
                text=label,
                font=("Arial", 10),
                bg="#34495E",
                fg="#95A5A6"
            ).pack(pady=(10, 0))
            
            tk.Label(
                detail_box,
                text=value,
                font=("Arial", 14, "bold"),
                bg="#34495E",
                fg=self.fg_color
            ).pack(pady=(0, 10), padx=20)
    
    def clear_weather_display(self):
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
    
    def show_error(self, message):
        self.clear_weather_display()
        error_label = tk.Label(
            self.weather_frame,
            text=f"❌ {message}",
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#E74C3C",
            wraplength=400
        )
        error_label.pack(pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClimexWeatherApp(root)
    root.mainloop()