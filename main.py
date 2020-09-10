from selenium import webdriver
import time

Account_Username = input("Enter your Instagram account's Username:")
Account_Password = input("Enter your Instagram account's Password:")



def follow():

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    username = driver.find_element_by_css_selector("[name='username']")
    username.send_keys(Account_Username)
    password = driver.find_element_by_css_selector("[name='password']")
    password.send_keys(Account_Password)
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    time.sleep(3)
    SaveInfo = driver.find_element_by_class_name('cmbtv')
    SaveInfo.click()
    time.sleep(2)
    PostNotification = driver.find_element_by_class_name('mt3GC')
    PostNotification.click()
    time.sleep(5)
    for i in range(3):
        for j in range(6):
            follow = driver.find_element_by_xpath("//button[text()='Follow']")
            follow.click()
            time.sleep(2)
            driver.refresh()
    driver.close()
    
follow()
