from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text

# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"{price_dollar}.{price_cents}")


# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)



# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time

upcoming_events = {}
# for n in range(5):
#     events_date = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n+1}]/time').text
#     events_name = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n+1}]/a').text
#     upcoming_events[n] = {
#             "time": events_date,
#             "name": events_name,
#         }

event_dates = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget li a")
for n in range(len(event_dates)):
    upcoming_events[n] = {
            "time": event_dates[n].text,
            "name": event_names[n].text,
        }
print(upcoming_events)

input("Press Enter to close the browser...")