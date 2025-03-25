"""
import time
i = 2
while i > 1:
    print(i)
    time.sleep(100)

"""

"""
import tkinter as tk
from tkinter import messagebox
import time

i = 2

while i > 1:

    # Function to close the window
    def close_window(window):
        window.destroy()

    # Create the main window
    root = tk.Tk()
    root.title("Close Button Window")

    # Set the window size
    root.geometry("300x150")

    # Create a close button
    close_button = tk.Button(root, text="Close", command=lambda: close_window(root))
    close_button.pack(pady=20)

    # Function to automatically close the window after 2 minutes
    def auto_close():
        time.sleep(120)  # Wait for 2 minutes (120 seconds)
        close_window(root)

    # Run the auto close function in the background
    root.after(100, auto_close)

    # Start the Tkinter event loop
    root.mainloop()

    print(i)
    
"""
import webbrowser
import time
import os
import signal

i = 2

while i > 1:
    # Open the website
    url = "https://oakstreethealthprod.service-now.com/"
    webbrowser.open(url)

    # Wait for 2 minutes (120 seconds)
    time.sleep(120)

    # Closing the Chrome browser (Windows-specific)
    # This will kill all Chrome processes. Be careful when using this as it closes all Chrome windows.
    os.system("taskkill /f /im chrome.exe")

    i = i + 1
    print(i)