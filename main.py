from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import string
import secrets

def generate_password(length=6):
    all_characters = string.ascii_letters + string.digits + "@"
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def save_credentials(username, password, filename="credentials.txt"):
    with open(filename, 'a') as file:
        file.write(f"{username}:{password}\n")
    
    print(f"Credentials for {username} saved successfully.")

options = Options()

def automate(us_name):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.hackerrank.com/auth/signup")
    time.sleep(10)
    user_name = driver.find_element("xpath","/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[1]/div/div[1]/input")
    user_email = driver.find_element("xpath","/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[2]/div/div[1]/input")
    user_password = driver.find_element("xpath","/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[3]/div/div[1]/input")
    hacker_policy = driver.find_element("xpath","/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[4]/div/button")
    submit = driver.find_element("xpath","/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[5]/button")
    user_name.send_keys("CSE FEST")
    user_email.send_keys(us_name+"@g.com")
    ps = generate_password()

    user_password.send_keys(ps)
    hacker_policy.click()
    save_credentials(us_name,ps)
    submit.click()
    time.sleep(5)
    driver.delete_all_cookies()
    driver.quit()
    time.sleep(5)

try:
    with open("team_name.txt", "r") as file:
        team_names = [line.strip() for line in file if line.strip()]  # Remove empty lines
except FileNotFoundError:
    print("Error: team_name.txt not found.")
    team_names = []

for team in team_names:
    automate(team)
    time.sleep(3)