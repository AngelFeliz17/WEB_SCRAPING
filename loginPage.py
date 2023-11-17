from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import yaml

from captchaSolver import solveCaptcha
from sendEmail import sendEmail

open with("login_page_info.yaml", "r") as content :
   data = yaml.safe_load_all(content)
   url = data["LOGIN_PAGE_INFO"]["URL"]
   email = data["LOGIN_PAGE_INFO"]["EMAIL"]
   password = data["LOGIN_PAGE_INFO"]["PASSWORD"]

driver = webdriver.Chrome()
attempts = 5

def loginPage() :
    global attempts
    driver.get(url)

    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_input.send_keys(password)

    captcha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img")))
    src = captcha.get_attribute("src")

    captchaText = solveCaptcha(src)

    captchaInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[3]/div/div/div[1]/input")))
    captchaInput.send_keys("".join(captchaText.split()))

    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='button']")))
    button.click()

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/ul/li[1]/div/span")))
        deviceInfoPage()
    except TimeoutException:
        attempts = attempts - 1
        if attempts == 0 :
           sendEmail(None, 404)
        else :
           loginPage()

def deviceInfoPage() :
    menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/ul/li[1]/div/span")))
    menu.click()

    sleep(0.5)
    submenu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/ul/li[1]/ul/li[4]/span")))
    submenu.click()

    sleep(0.5)
    licenseRemainingAmount = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#device-list > div.listen-box > div > div > table > tbody > tr > td:nth-child(4) > div > span.el-descriptions-item__content")))
    sleep(5)

    licenseQuantity = int(licenseRemainingAmount.text)
    with open("licenseQuantity.yaml", "r") as info :
        data = yaml.safe_load(info)
        LICENSE_LIMIT = data["LIMITED_AMOUNT_LICENSES"]["QUANTITY"]

    if licenseQuantity < LICENSE_LIMIT :
        sendEmail(licenseQuantity, None)

loginPage()
