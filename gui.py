import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import threading
import time

class FridayGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Friday 3.0")
        self.root.geometry("800x600")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Friday 3.0",
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Status frame
        self.status_frame = ctk.CTkFrame(self.main_frame)
        self.status_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Status: Ready",
            font=("Helvetica", 14)
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Microphone button
        self.is_listening = False
        self.mic_button = ctk.CTkButton(
            self.status_frame,
            text="Start Listening",
            command=self.toggle_listening,
            width=120
        )
        self.mic_button.pack(side=tk.RIGHT, padx=10)
        
        # Last command frame
        self.command_frame = ctk.CTkFrame(self.main_frame)
        self.command_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.command_label = ctk.CTkLabel(
            self.command_frame,
            text="Last Command: None",
            font=("Helvetica", 12)
        )
        self.command_label.pack(pady=10)
        
        # Features frame
        self.features_frame = ctk.CTkFrame(self.main_frame)
        self.features_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create feature buttons
        self.create_feature_buttons()
        
        # Volume control
        self.volume_frame = ctk.CTkFrame(self.main_frame)
        self.volume_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.volume_label = ctk.CTkLabel(
            self.volume_frame,
            text="Volume:",
            font=("Helvetica", 12)
        )
        self.volume_label.pack(side=tk.LEFT, padx=10)
        
        self.volume_slider = ctk.CTkSlider(
            self.volume_frame,
            from_=0,
            to=100,
            command=self.update_volume
        )
        self.volume_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        self.volume_slider.set(50)
        
        # Initialize features dictionary
        self.features = {
            "Time & Date": self.show_time,
            "YouTube": self.open_youtube,
            "Google Search": self.google_search,
            "System Control": self.system_control,
            "Webcam": self.toggle_webcam,
            "Screenshot": self.take_screenshot,
            "Notes": self.open_notes,
            "Weather": self.show_weather
        }

    def create_feature_buttons(self):
        features = [
            "Time & Date", "YouTube", "Google Search",
            "System Control", "Webcam", "Screenshot",
            "Notes", "Weather"
        ]
        
        for i, feature in enumerate(features):
            row = i // 4
            col = i % 4
            
            button = ctk.CTkButton(
                self.features_frame,
                text=feature,
                command=lambda f=feature: self.handle_feature(f),
                width=120
            )
            button.grid(row=row, column=col, padx=10, pady=10)

    def handle_feature(self, feature):
        if feature in self.features:
            self.features[feature]()
            self.update_command(f"Activated {feature}")

    def toggle_listening(self):
        self.is_listening = not self.is_listening
        if self.is_listening:
            self.mic_button.configure(text="Stop Listening")
            self.status_label.configure(text="Status: Listening...")
            # Start listening thread here
            threading.Thread(target=self.listening_thread, daemon=True).start()
        else:
            self.mic_button.configure(text="Start Listening")
            self.status_label.configure(text="Status: Ready")

    def update_command(self, command):
        self.command_label.configure(text=f"Last Command: {command}")

    def update_volume(self, value):
        # Add your volume control logic here
        pass

    def listening_thread(self):
        while self.is_listening:
            # Add your speech recognition logic here
            time.sleep(0.1)

    # Feature methods
    def show_time(self):
        # Implement time display
        pass

    def open_youtube(self):
        # Implement YouTube functionality
        pass

    def google_search(self):
        # Implement Google search
        pass

    def system_control(self):
        # Implement system controls
        pass

    def toggle_webcam(self):
        # Implement webcam toggle
        pass

    def take_screenshot(self):
        # Implement screenshot
        pass

    def open_notes(self):
        # Implement notes
        pass

    def show_weather(self):
        # Implement weather display
        pass

def main():
    root = tk.Tk()
    app = FridayGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()