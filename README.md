# HackerRank Account Automation

This project automates the creation of HackerRank accounts using Selenium. It reads team names from `team_name.txt`, generates unique passwords, and saves credentials in `credentials.txt`.

## Features
- Reads team names from `team_name.txt`
- Generates passwords using `a-z`, `A-Z`, `0-9`, and `@`
- Automates the signup process on HackerRank
- Saves credentials in `credentials.txt`

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome
- ChromeDriver

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Nabeel-Ahsan7/HackerRank-Account-Automation.git
   cd HackerRank-Account-Automation
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Add your team names to team_name.txt (one team name per line).

5. Run the script to automate the account creation process:
   ``` sh
   python main.py
   ```
6. The script will create accounts and save the credentials in credentials.txt.(save format -> User_Name:Password)

## File Structure
```bash
HackerRank-Account-Automation/
 ├── main.py              # Main automation script
 ├── team_name.txt        # List of team names
 ├── credentials.txt      # Saved credentials
 ├── requirements.txt     # Dependencies
 ├── README.md 
 ```
 ## Notes
 1. Ensure team_name.txt exists before running the script.
 2. Modify generate_password() in main.py to adjust password rules if needed.
 