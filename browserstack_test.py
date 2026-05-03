# Cross Browser Testing using BrowserStack

from selenium import webdriver

USERNAME = "your_browserstack_username"
ACCESS_KEY = "your_browserstack_access_key"

url = "https://the-internet.herokuapp.com/login"

capabilities = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "os": "Windows",
    "osVersion": "10",
    "name": "Login Test on Chrome"
}

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=capabilities
)

driver.get(url)

print("Test executed on Chrome")

driver.quit()
