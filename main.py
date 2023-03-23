import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os


chrome_driver_path = "C:\\Program Files\\Development\\chromedriver"
s = Service(chrome_driver_path)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=options)

#<---------------------------------------------- TINDER MENU START --------------------------------------------------------->#


driver.get("https://tinder.com/")
driver.maximize_window()

login_tinder = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_tinder.click()

time.sleep(1)

login_facebook = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_facebook.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(2)

#<---------------------------------------------- FACEBOOK POPUP --------------------------------------------------------->#

agreement_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]")
agreement_btn.click()

time.sleep(1)

fb_email_input = driver.find_element(By.ID, "email")
fb_email_input.send_keys(os.environ["FB_LOGIN"])

fb_password_input = driver.find_element(By.ID, "pass")
fb_password_input.send_keys(os.environ["FB_PASSWORD"])

fb_login_button = driver.find_element(By.ID, "loginbutton")
fb_login_button.click()

#<---------------------------------------------- TINDER MAIN PROGRAM --------------------------------------------------------->#

time.sleep(10)

driver.switch_to.window(base_window)

time.sleep(3)

annoying_popup = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]")
annoying_popup.click()

try:
    use_tinder_btn = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
except selenium.common.exceptions.NoSuchElementException:
    pass
else:
    use_tinder_btn.click()

try:
    turn_on = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
except selenium.common.exceptions.NoSuchElementException:
    pass
else:
    turn_on.click()


time.sleep(3)

maybe_later_btn = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[3]/button[2]/span")
maybe_later_btn.click()

reject_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]")
reject_btn.click()

time.sleep(3)

go_right_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span")

while True:
    try:
        popup_again = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]")
    except selenium.common.exceptions.NoSuchElementException:
        try:
            another_popup = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[3]/button[2]/span")
        except selenium.common.exceptions.NoSuchElementException:
            go_right_btn.click()
        else:
            another_popup.click()
    else:
        popup_again.click()
    time.sleep(2)

