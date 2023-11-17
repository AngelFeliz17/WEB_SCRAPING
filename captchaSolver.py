import pytesseract
from selenium import webdriver
from PIL import Image
import cv2

def solveCaptcha(src) :
    driver = webdriver.Chrome()
    driver.get(src)
    driver.save_screenshot("captcha.png")

    image = Image.open("captcha.png")
    convertedImg = image.convert("L")

    convertedImg.save("captcha_gray.png")

    img = cv2.imread("captcha_gray.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, result = cv2.threshold(img, 92, 255, cv2.THRESH_BINARY)
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    text = pytesseract.image_to_string(result, config = custom_config)
    text = text[:4]

    driver.close()
    return text   
