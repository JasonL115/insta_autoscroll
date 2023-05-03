import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# open the webpage
driver.get("http://www.instagram.com")

# target username
username = WebDriverWait(
	driver, 10).until(EC.element_to_be_clickable(
		(By.CSS_SELECTOR, "input[name='username']")))

# target Password
password = WebDriverWait(
	driver, 10).until(EC.element_to_be_clickable(
		(By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys("acnh_daydream")
password.clear()
password.send_keys("1195Quocdat")

# target the login button and click it
button = WebDriverWait(
	driver, 2).until(EC.element_to_be_clickable(
		(By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)

# Scroll till Followers list is there
driver.get("https://www.instagram.com/acnh_daydream/followers/")

pop_up_window_followers = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH,
     "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")))


s=0

while s<5:
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window_followers)
    s+=1

    time.sleep(5)

# Scroll till Followering list is there
driver.get("https://www.instagram.com/acnh_daydream/following/")


pop_up_window = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH,
     "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))

while True:
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window)
    time.sleep(3)
    
time.sleep(20)
driver.quit()
