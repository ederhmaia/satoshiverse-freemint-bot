from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

browserOptions = Options()
browserOptions.add_argument("--headless")
browserOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=browserOptions)

EMAIL_PREFIX = 'blablabla'
EMAIL_SUFIX = '@gmail.com'
LINE_COUNTER = 0
print("+-----------------------------------------------------------")
print("| Satoshiverse BOT by @ederhmaia / @edermxf")
print("| Set your email in the script ")
print("| Set the Address List on 'AddressList.txt'")
print("+-----------------------------------------------------------")

print("[!] Starting...")
with open('AddressList.txt') as FILE:
    for LINE in FILE:
        LINE_COUNTER += 1
        driver.get("https://www.satoshiverse.io/btc2022")
        time.sleep(2)
        TwitterInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "twitter_address")))
        TwitterInput.send_keys("@ederhmaia")

        EmailInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email")))
        EmailInput.send_keys(f"{EMAIL_PREFIX}+{LINE_COUNTER}{EMAIL_SUFIX}")

        EthAddress = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "eth_address")))
        EthAddress.send_keys(LINE)

        Checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkmark")))
        Checkbox.click()

        Submit = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Submit']")))
        Submit.click()

        print(
            f"[-] Using -> {LINE.strip()} | With -> {EMAIL_PREFIX}+{LINE_COUNTER}{EMAIL_SUFIX}")
        time.sleep(2)
print("[!] Finished!")
