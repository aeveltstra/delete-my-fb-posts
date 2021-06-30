from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

email_address = "my email address for facebook"
password = "my facebook password"
profile_name = "name of my facebook profile"
profile_page_title = "title of the page after loading my facebook profile"

with webdriver.Firefox() as driver:
    driver.implicitly_wait(10)
    driver.get("https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2F{}".format(profile_name))
    element = driver.find_element_by_id("m_login_email")
    element.send_keys(email_address)
    element = driver.find_element_by_id("m_login_password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(conditions.title_is(profile_page_title))
    xpathEllipses = "//div[contains(@class, '_5s61 _2pis')]/div[1]"
    xpathRemovalButton = "//a[contains(@data-sigil,'removeStoryButton enabled_action')][1]"
    xpathConfirmDeleteButton = "//div[contains(@class, '_4g34')]/a[@title='Supprimer'][contains(@href, '/trust/afro/direct_action_execute?')][1]"
    counter = 0
    max_repeats = 5
    repeat = 0
    while repeat < max_repeats:
        try:
            repeat = repeat + 1
            ellipses = driver.find_elements(By.XPATH, xpathEllipses)
            #print(ellipses)
            for ellipse in ellipses:
                # print(ellipse)
                if ellipse.is_displayed():
                    ellipse.click()
                    WebDriverWait(driver, 10)
                    buttons = driver.find_elements(By.XPATH, xpathRemovalButton)
                    for button in buttons: 
                        if button.is_displayed():
                            # print(button)
                            button.click()
                            WebDriverWait(driver, 5)
                            anchors = driver.find_elements(By.XPATH, xpathConfirmDeleteButton)
                            WebDriverWait(driver, 5)
                            for anchor in anchors:
                                if anchor.is_displayed():
                                    # print(anchor)
                                    anchor.click()
                                    WebDriverWait(driver, 15)
                                    counter = counter + 1
        except StaleElementReferenceException as e:
            driver.refresh()
    driver.close()
    driver.quit()

print("Pressed delete this many times: {}.".format(counter))
