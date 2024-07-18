<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div class="container">
        <h1>arete.network.chatbot</h1>
        <p>This is a Python script that automates posting comments in the chat room at <a href="https://arete.network/chat/IP2/" target="_blank">https://arete.network/chat/IP2/</a>.</p>
        <h2>Features</h2>
        <ul>
            <li>Automates login to the chat room</li>
            <li>Continuously posts comments in the chat room</li>
        </ul>
        <h2>Prerequisites</h2>
        <p>Ensure you have the following installed:</p>
        <ul>
            <li>Python 3.x</li>
            <li>Selenium package</li>
            <li>WebDriver for your browser (e.g., ChromeDriver for Google Chrome)</li>
        </ul>
        <h2>Installation</h2>
        <pre><code>pip install selenium</code></pre>
        <p>Download the WebDriver for your browser and ensure it is in your system's PATH.</p>
        <h2>Usage</h2>
        <p>Update the script with your login credentials and comment text:</p>
    
        <pre><code>username = "your_username"
    password = "your_password"
    comment = "This is an automated comment."</code></pre>
        <p>Run the script:</p>
        <pre><code>python path_to_your_script.py</code></pre>
        <h2>Script</h2>
        <pre><code>from selenium import webdriver
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
# No driver.quit() here, so the WebDriver window will remain open</code>
</pre>
        <h2>Contributing</h2>
        <p>Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.</p>
        <h2>License</h2>
        <p>This project is licensed under the GPL-3.0 License - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>
    </div>
</body>
</html>
