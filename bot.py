from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your actual login credentials
username = "your_username"
password = "your_password"
comment = "This is an automated comment."

# Initialize the WebDriver (assuming Chrome)
driver = webdriver.Chrome()

try:
    # Set an implicit wait
    driver.implicitly_wait(10)  # Wait up to 10 seconds when trying to find elements
    
    # Go to the chat room page
    driver.get("https://arete.network/chat/IP2/")
    
    # Click on the user dropdown to log in
    user_dropdown = driver.find_element(By.CSS_SELECTOR, "#userDropdown > span.user")
    user_dropdown.click()
    
    # Enter username
    login_username = driver.find_element(By.CSS_SELECTOR, "#loginUsername")
    login_username.send_keys(username)
    
    # Enter password
    login_password = driver.find_element(By.CSS_SELECTOR, "#loginPassword")
    login_password.send_keys(password)
    
    # Submit login form
    submit_button = driver.find_element(By.CSS_SELECTOR, "#loginPrompt > form > div:nth-child(4) > input[type=submit]")
    submit_button.click()
    
    # Go back to the chat room page after login
    driver.get("https://arete.network/chat/IP2/")
    
    # Find the input box and send keys
    input_box = driver.find_element(By.CSS_SELECTOR, '#input-box')
    
    # Infinite loop to continuously post messages
    while True:
        input_box.click()  # Click to focus
        input_box.send_keys(comment)
        
        # Send the message using the specific CSS Selector
        send_button = driver.find_element(By.CSS_SELECTOR, '#chat-input-inner > div:nth-child(3)')
        send_button.click()
        
        # Optional: Add a delay between posts
        time.sleep(5)  # Adjust as needed to control the posting rate

except Exception as e:
    print(f"An error occurred: {str(e)}")

# No driver.quit() here, so the WebDriver window will remain open

