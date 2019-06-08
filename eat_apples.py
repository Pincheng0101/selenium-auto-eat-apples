from selenium import webdriver
import numpy
import time

driver = webdriver.Chrome()
driver.get("http://game.hg0355.com/game/xpg/?from=timeline&isappinstalled=0")
time.sleep(0.5)
ready = driver.find_element_by_id("ready-btn")
ready.click()

while True:
    try:
        score_button = driver.find_elements_by_xpath("//div[(contains(@class, 't1') or contains(@class, 't2') or contains(@class, 't3') or contains(@class, 't4') or contains(@class, 't5')) and not(contains(@class, 'tt'))]")
        locations = [i.location['y'] for i in score_button]
        location_index = numpy.argsort(locations)[::-1]

        for i in location_index:
            if (score_button[i].is_enabled() and score_button[i].is_displayed()):
                score_button[i].click()
            else:
                continue
            #webdriver.ActionChains(driver).move_to_element(score_button[max_index]).click().perform()
    except Exception as e:
        print (e)
        pass
