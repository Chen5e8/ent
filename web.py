import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://ent.ecollege78.fr/auth/login?callback=https%3A%2F%2Fent.ecollege78.fr%2F#/")

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "email"))
)

password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "password"))
)

element.send_keys("austin.chen")
password.send_keys("saint.Germain.en.Laye MI09")

time.sleep(5)
button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Connexion')]"))
)

button.click()

time.sleep(5)

driver.execute_script("alert('connexion réussite')")
time.sleep(1)
alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
alert.accept()

button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Mes applis']"))
)

button.click()

time.sleep(5)
input("pour terminer, entréer '\\n'")
# driver.quit()