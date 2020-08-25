from selenium import webdriver
import time

Account_Username = input("Enter your Instagram account's Username:")
Account_Password = input("Enter your Instagram account's Password:")



class instagram:
    def follow(self):

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
        time.sleep(2)
        for i in range(2):
            time.sleep(3)
            for j in range(1):
                time.sleep(3)
                follow1 = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
                follow1.click()
                time.sleep(1)

                follow2 = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button')
                follow2.click()
                time.sleep(1)

                follow3 = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button')
                follow3.click()
                time.sleep(1)

                follow4 = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[4]/div[3]/button'
                )
                follow4.click()
                time.sleep(1)

                follow5 = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[5]/div[3]/button'
                )
                follow5.click()
                time.sleep(1)

            driver.refresh()
        driver.close()
