import unittest
from selenium import webdriver
from time import sleep, time
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome(executable_path='')  # SET YOUR OWN PATH
driver.maximize_window()
driver.get('https://tinder.com/')

def log_in(user, password):
    #cookies_button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button/span'))).click()
    # login_button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span'))).click()
    # sleep(3)
    # facebook_login_button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label, "Facebook")]/span[contains(text(), "Facebook")]'))).click()
    # driver.find_element_by_xpath('').click()


    # Wait until the new window appear
    handles_before = driver.window_handles
    WebDriverWait(driver, 30).until(lambda driver: len(handles_before) != len(driver.window_handles))
    handles_after = driver.window_handles
    driver.switch_to.window(handles_after[1])

    facebook_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    facebook_email.clear()
    facebook_email.send_keys(user)
    facebook_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    facebook_password.send_keys(password)
    # facebook_login_button
    driver.find_element_by_name('login').click()

    driver.switch_to.window(handles_after[0])

def swipe_rigth(swiping_time):
    # location_button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span'))).click()
    # no_notifications_button
    no_notifications_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span'))).click()

    tinder_advice = '//button[@type="button"][2]/span[starts-with(@class, "Pos(r) Z(1)")]' # Gold or Super Like

    # no_gold_add_button
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, tinder_advice))).click()


    stop = swiping_time + time.time()  
    while time.time() <= stop:
        try:
            driver.find_element_by_xpath(tinder_advice).click()
        except:
            driver.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
            continue

def run():
    user = input('Enter your Facebook user: ')
    password = input('Enter your Facebook password: ')
    time_to_swipe = int(input('Set (in seconds) how long you want to swipe right: '))
    log_in(user, password)
    swipe_rigth(time_to_swipe)

run()



driver.quit()
