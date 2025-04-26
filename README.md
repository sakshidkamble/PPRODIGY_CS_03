
# PPRODIGY_CS_03
Task 3- Password complexity checker ( Submission of Prodigy InfoTech Internship[CyberSecurity Track])

A Python-based GUI application built with Tkinter to analyze password strength, generate secure passwords, and export detailed reports. This tool calculates entropy, estimates crack time, detects patterns, checks for breaches using the Have I Been Pwned API, and offers a user-friendly interface with dark/light theme support.

## Features
- Password Analysis:
  - Calculates entropy (in bits) based on character set complexity.
  - Estimates time to crack the password using brute-force methods.
  - Detects common patterns (e.g., "123456", "qwerty").
  - Checks if the password has been exposed in data breaches via the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3).
- Password Generation: Generates cryptographically secure random passwords.
- Report Export: Saves analysis results as a PDF report.
- User Interface:
  - Built with Tkinter for a clean, responsive GUI.
  - Supports dark and light themes.
  - Includes password history and clipboard functionality.

## Screenshots

![cs03](https://github.com/user-attachments/assets/efd0bf8f-1213-4a1b-9f0e-1c059f8c3e68)
![cso3 1](https://github.com/user-attachments/assets/4985aad4-9252-4a48-b6d9-9cbd75aa24f2)
![cso3 2](https://github.com/user-attachments/assets/fbead1cd-d118-4fd0-ada2-8db20e454d12)
![cso3 3](https://github.com/user-attachments/assets/ace4e63c-0464-481e-807a-088c31a1da23)
![cso3 4](https://github.com/user-attachments/assets/96b2723c-54d6-4205-bd9a-74824543ee7f)
![cso3 5](https://github.com/user-attachments/assets/6ba4d81e-6c77-4325-9ac5-819f40ee7501)
![cso3 6](https://github.com/user-attachments/assets/041c453a-3be1-44b1-8ffa-29ac24e8ccb0)
![cso3 7](https://github.com/user-attachments/assets/a3e7d382-0786-407e-bd3f-523acd082242)
![cso3 8](https://github.com/user-attachments/assets/25412e75-e66a-402c-b371-f2da5150adca)
![cso3 9](https://github.com/user-attachments/assets/2e937990-66af-49e5-8933-1f614a1904fa)

----------------
## Installation

### Prerequisites
- Python 3.6 or higher
- Required libraries: `requests`, `reportlab`, `pyperclip`

### Setup
1. Clone the repository
2. Install dependencies:
pip install requests reportlab pyperclip
3. Run the file:
python password_analyzer.py

==================================================================================================
Usage

Launch the app using python password_analyzer.py.
Enter a password in the input field or click "Generate Password" for a secure random password.
Click "Analyze" to view entropy, crack time, patterns, and breach status.
Use "Copy Password" to copy the password to your clipboard.
Click "Export Report" to save the analysis as a PDF.
Toggle between dark and light themes with the "Toggle Theme" button.


Dependencies

tkinter: For the GUI (usually included with Python).
requests: For querying the Have I Been Pwned API.
reportlab: For generating PDF reports.
pyperclip: For clipboard functionality.
hashlib, secrets, math, string, datetime: Standard Python libraries.


Contributing
Contributions are welcome! To contribute:
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit (git commit -m "Add feature").
Push to your fork (git push origin feature-name).
Open a pull request.
=============================================================================
---

If you have any suggestions or feedback, feel free to reach out!  

---

http://www.linkedin.com/in/sakshi-dhananjay-kamble-4444ba219

---
