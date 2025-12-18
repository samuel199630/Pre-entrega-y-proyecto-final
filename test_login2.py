from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()


    try:
        driver.get("https://www.saucedemo.com/")

        time.sleep(1)
        
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        
        time.sleep(2)

        assert "/inventory.html" in driver.current_url, "no se redirigio correctamente al inventario"

        print("login exitoso y validado correctamente")

    except Exception as e: 
        print(f"error en test login: {e}")
        raise
    finally:
        driver.quit()