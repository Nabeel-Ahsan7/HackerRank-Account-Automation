# HackerRank Account Automation

This project automates the creation of HackerRank accounts using Selenium. It reads team names from \	eam_name.txt\, generates unique passwords, and saves credentials in \credentials.txt\.

## Features
- Reads team names from \	eam_name.txt\
- Generates passwords using \-z\, \A-Z\, \ -9\, and \@\
- Automates the signup process on HackerRank
- Saves credentials in \credentials.txt\

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome
- ChromeDriver

## Installation
1. Clone this repository:
   \\\sh
   git clone https://github.com/Nabeel-Ahsan7/HackerRank-Account-Automation.git
   cd HackerRank-Account-Automation
   \\\
2. Install dependencies:
   \\\sh
   pip install -r requirements.txt
   \\\

## Usage
1. Add team names (one per line) in \	eam_name.txt\.
2. Run the script:
   \\\sh
   python main.py
   \\\
3. Check \credentials.txt\ for generated usernames and passwords.

## File Structure
\\\
📂 HackerRank-Account-Automation
 ├── main.py             # Main automation script
 ├── team_name.txt       # List of team names
 ├── credentials.txt     # Saved credentials
 ├── requirements.txt    # Dependencies
 ├── README.md           # Documentation
\\\

## Notes
- Ensure \	eam_name.txt\ exists before running the script.
- Modify \generate_password()\ in \main.py\ to adjust password rules if needed.

## License
This project is licensed under the MIT License.

---

Happy Coding! ��
