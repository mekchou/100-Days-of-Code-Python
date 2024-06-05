from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time




def max_affordable(money, store):
    money_on_hand = int(money.text.replace(",",""))
    for item in store[-2::-1]:
        # print(money_on_hand)
        # print(int(item.text.split(" - ")[1].replace(",","")))
        if money_on_hand >= int(item.text.split(" - ")[1].replace(",","")):
            # print(item.text.split(" - ")[0])
            return item.text.split(" - ")[0]
            # break 
        # print(item.text)
        # else:
    return False

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")    


    cookie = driver.find_element(By.ID, value="cookie")
    money = driver.find_element(By.ID, value="money")
    
    timeout = time.time()+5
    five_min = time.time() + 60*5  # 5 minutes
    # print(store[0].text)    
    while True:
        store = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        if time.time() >= timeout:
            # print(money.text)
            buy_item = max_affordable(money, store)
            # print(buy_item)
            if buy_item is not False:
                item_button = driver.find_element(By.ID, value=f"buy{buy_item}")
                # print(item_button)
                item_button.click()
            # cookie.click()
            timeout = time.time() +5
        else:
            cookie.click()
            # print(money.text)
        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, value="cps")
            print(cookie_per_s.text)
            break






if __name__ == "__main__":
    main()
    # print(time.time())
    input("Press Enter to close the browser...")







