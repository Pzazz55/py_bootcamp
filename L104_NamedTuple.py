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