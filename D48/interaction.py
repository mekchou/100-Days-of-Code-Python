from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Mek")
last_name.send_keys("Chou")
email.send_keys("mek.chou@gmail.com")

# sign_up = driver.find_element(By.CLASS_NAME, value="btn")
sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up.click()
# print(sign_up.text)



input("Press Enter to close the browser...")