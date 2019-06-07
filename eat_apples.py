from selenium import webdriver
import time
import re

driver = webdriver.Chrome()
driver.get("http://game.hg0355.com/game/xpg/?from=timeline&isappinstalled=0")
time.sleep(0.5)
ready =  driver.find_element_by_id("ready-btn")
ready.click()

while True:

    try:
        score_button = driver.find_elements_by_xpath("//div[(contains(@class, 't1') or contains(@class, 't2') or contains(@class, 't3') or contains(@class, 't4') or contains(@class, 't5')) and not(contains(@class, 'tt'))]")
        for i in range(len(score_button)):
            i = 0
            max_index = 0
            max_location = 0
            for x in score_button:
                if x.location['y'] > max_location:
                    max_location = x.location['y']
                    max_index = i
                i+=1
            score_button[max_index].click()
            score_button.pop(max_index)
            #webdriver.ActionChains(driver).move_to_element(score_button[max_index]).click().perform()
    except Exception as e:
        print (e)
        pass