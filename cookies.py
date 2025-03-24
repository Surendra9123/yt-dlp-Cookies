import os
import time

package_name = 'selenium'
try:
  os.system(f'pip install {package_name}')
except Exception as e:
  print(e)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.binary_location = "/usr/bin/brave-browser"

options.add_argument(f"user-data-dir={os.getcwd()}/fixbrave")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
options.add_argument("no-sandbox")
options.add_argument('window-size=1280,720')
options.add_argument('disable-infobars')
options.add_argument("--autoplay-policy=no-user-gesture-required")
prefs = {'exit_type': 'Normal'}
options.add_experimental_option("prefs", {'profile': prefs})
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation detection
options.add_experimental_option("useAutomationExtension", False)

options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-background-networking")
options.add_argument("--disable-component-update")
options.add_argument("--disable-features=BraveRewards,Shields")
options.add_argument("--process-per-site")
options.add_argument("--enable-low-end-device-mode")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-sync")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)

driver.get("https://accounts.google.com/signin")

def save_cookies_to_netscape_file(cookies, output_file):
    with open(output_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# This is a generated file! Do not edit.\n\n")
        f.write("# domain  include_subdomains  path  secure  expiration_date  name  value\n") 
        for cookie in cookies:
            expiry = cookie.get('expiry') or cookie.get('expires') or 0  
            f.write(f"{cookie['domain']}\t")
            f.write("TRUE\t")
            f.write(f"{cookie['path']}\t")
            f.write("TRUE\t" if cookie.get('secure') else "FALSE\t")
            f.write(f"{int(expiry)}\t")
            f.write(f"{cookie['name']}\t{cookie['value']}\n")
    return f"Cookies have been saved to {output_file}"

while True:
 user_input = input("[First Login Gmail] enter a name for your cookies file: ")
 driver.get("https://youtu.be/watch?v=i-AIcwllkRU")
 for sec in range(10, 0, -1):
   print(f"Wait {sec}...", end="\r")
   time.sleep(1)
 if not user_input:
   user_input = "cookies.txt"
 output_file = f"{user_input}.txt"
 break

if "youtube.com" in driver.current_url:
  pass
else:
  print("The current website is not YouTube cookies file maybe not work...")

cookies = driver.get_cookies()
output_file = f"{os.getcwd()}/{output_file}"
save_cookies_to_netscape_file(cookies, output_file)
print("Cookies saved to:",output_file)


driver.quit()
