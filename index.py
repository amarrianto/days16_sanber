import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_success(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
    
    def test_failed_login_without_username(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        errorMessage = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message").text
        self.assertIn("Required", errorMessage)


    def test_failed_login_without_password(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()
        errorMessage = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message").text
        self.assertIn("Required", errorMessage)

        

if __name__ == '__main__':
    unittest.main()