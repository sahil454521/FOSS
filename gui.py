import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import threading
import time
from datetime import datetime

class ModernFridayGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Friday 3.0")
        self.root.geometry("1000x700")
        
        # Set theme and colors
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Main container
        self.container = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )
        self.container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Header section with glass effect
        self.header = ctk.CTkFrame(
            self.container,
            fg_color="#2B2B2B",
            corner_radius=15
        )
        self.header.pack(fill=tk.X, pady=(0, 20))
        
        # Title with modern font
        self.title_label = ctk.CTkLabel(
            self.header,
            text="FRIDAY 3.0",
            font=("Helvetica", 32, "bold"),
            text_color="#00BFFF"
        )
        self.title_label.pack(pady=20)
        
        # Time display
        self.time_label = ctk.CTkLabel(
            self.header,
            text="",
            font=("Helvetica", 14)
        )
        self.time_label.pack(pady=(0, 20))
        self.update_time()
        
        # Status section with animation
        self.status_frame = ctk.CTkFrame(
            self.container,
            fg_color="#2B2B2B",
            corner_radius=15
        )
        self.status_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Animated status indicator
        self.status_canvas = tk.Canvas(
            self.status_frame,
            width=20,
            height=20,
            bg='#2B2B2B',
            highlightthickness=0
        )
        self.status_canvas.pack(side=tk.LEFT, padx=20, pady=15)
        self.status_indicator = self.status_canvas.create_oval(5, 5, 15, 15, fill="#00FF00")
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Ready",
            font=("Helvetica", 14)
        )
        self.status_label.pack(side=tk.LEFT, pady=15)
        
        # Modern microphone button
        self.is_listening = False
        self.mic_button = ctk.CTkButton(
            self.status_frame,
            text="Start Listening",
            font=("Helvetica", 14, "bold"),
            width=150,
            height=40,
            corner_radius=20,
            command=self.toggle_listening,
            fg_color="#1E90FF",
            hover_color="#187BCD"
        )
        self.mic_button.pack(side=tk.RIGHT, padx=20, pady=15)
        
        # Command display
        self.command_frame = ctk.CTkFrame(
            self.container,
            fg_color="#2B2B2B",
            corner_radius=15
        )
        self.command_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.command_label = ctk.CTkLabel(
            self.command_frame,
            text="Awaiting your command...",
            font=("Helvetica", 14),
            text_color="#B0B0B0"
        )
        self.command_label.pack(pady=15)
        
        # Features grid
        self.features_frame = ctk.CTkFrame(
            self.container,
            fg_color="#2B2B2B",
            corner_radius=15
        )
        self.features_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.create_feature_buttons()
        
        # Volume control
        self.volume_frame = ctk.CTkFrame(
            self.container,
            fg_color="#2B2B2B",
            corner_radius=15
        )
        self.volume_frame.pack(fill=tk.X)
        
        self.volume_label = ctk.CTkLabel(
            self.volume_frame,
            text="Volume",
            font=("Helvetica", 14)
        )
        self.volume_label.pack(side=tk.LEFT, padx=20, pady=15)
        
        self.volume_slider = ctk.CTkSlider(
            self.volume_frame,
            from_=0,
            to=100,
            command=self.update_volume,
            progress_color="#1E90FF",
            button_color="#1E90FF",
            button_hover_color="#187BCD"
        )
        self.volume_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=20, pady=15)
        self.volume_slider.set(50)
        
        # Start animation
        self.animate_status()

    def create_feature_buttons(self):
        features = [
            ("Time & Date", "🕒"), ("YouTube", "▶️"), 
            ("Google Search", "🔍"), ("System Control", "⚙️"),
            ("Webcam", "📷"), ("Screenshot", "📸"),
            ("Notes", "📝"), ("Weather", "☁️")
        ]
        
        for i, (feature, emoji) in enumerate(features):
            row = i // 4
            col = i % 4
            
            button = ctk.CTkButton(
                self.features_frame,
                text=f"{emoji} {feature}",
                font=("Helvetica", 14, "bold"),
                width=200,
                height=80,
                corner_radius=15,
                fg_color="#1E90FF",
                hover_color="#187BCD",
                command=lambda f=feature: self.handle_feature(f)
            )
            button.grid(row=row, column=col, padx=10, pady=10)
            
        # Configure grid weights for better spacing
        self.features_frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.features_frame.grid_rowconfigure((0,1), weight=1)

    def animate_status(self):
        if self.is_listening:
            current_color = self.status_canvas.itemcget(self.status_indicator, "fill")
            new_color = "#FF0000" if current_color == "#00FF00" else "#00FF00"
            self.status_canvas.itemconfig(self.status_indicator, fill=new_color)
        else:
            self.status_canvas.itemconfig(self.status_indicator, fill="#00FF00")
        self.root.after(500, self.animate_status)

    def update_time(self):
        current_time = datetime.now().strftime("%I:%M:%S %p - %B %d, %Y")
        self.time_label.configure(text=current_time)
        self.root.after(1000, self.update_time)

    def toggle_listening(self):
        self.is_listening = not self.is_listening
        if self.is_listening:
            self.mic_button.configure(text="Stop Listening", fg_color="#FF4444", hover_color="#CC3333")
            self.status_label.configure(text="Listening...")
            threading.Thread(target=self.listening_thread, daemon=True).start()
        else:
            self.mic_button.configure(text="Start Listening", fg_color="#1E90FF", hover_color="#187BCD")
            self.status_label.configure(text="Ready")

    def handle_feature(self, feature):
        self.command_label.configure(text=f"Activated: {feature}")

    def update_volume(self, value):
        # Add volume control logic here
        pass

    def listening_thread(self):
        while self.is_listening:
            # Add speech recognition logic here
            time.sleep(0.1)

def main():
    root = tk.Tk()
    app = ModernFridayGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()