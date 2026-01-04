Secure Login System with OTP (Cybersecurity Project)

A beginner-friendly yet real-world authentication system that demonstrates password security, OTP-based multi-factor authentication (MFA), and session handling using Flask.

This project was built as part of a Cybersecurity learning journey, focusing on how login systems work internally and how to secure them.

Features:

     User Registration with Strong Password Enforcement

     Password Hashing using bcrypt

     OTP-based Multi-Factor Authentication (MFA)

     Secure Session-based Login

     Clean & Modern User Interface

     Input validation & basic attack prevention

     Logout functionality

Authentication Flow (How It Works):

    Register → Login → OTP Verification → Dashboard

Step-by-step:

- User registers with a strong password

- Password is hashed and stored securely

- User logs in with username & password

- If credentials are correct → OTP is generated

- User enters OTP (demo: shown on UI)

- After OTP verification → user accesses dashboard

🛠️ Tech Stack

- Python

- Flask

- SQLite

- bcrypt (password hashing)

- pyotp (OTP generation)

- HTML + CSS (modern UI)

🔐 Security Concepts Implemented:

Concept	How it’s used
Password Hashing	bcrypt (no plain passwords stored)
Strong Password Policy	8+ chars, uppercase, lowercase, number
Multi-Factor Authentication	OTP after password login
Session Management	Flask sessions
Attack Awareness	Prevents plain-text leaks & basic brute force

📁 Project Structure:

secure-login-system/
│
├── app.py
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── otp.html
│   └── dashboard.html

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/secure-login-system.git
cd secure-login-system

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000


🔎 Demo OTP Note (Important)

⚠️ Demo Only Behavior

OTP is displayed on the UI for learning/demo purposes

In real-world systems, OTP would be sent via:

Email

SMS

Authenticator apps

This decision is intentional for easier understanding during development.

    What I Learned from This Project:

    How insecure login systems get compromised

    Why hashing > encryption for passwords

    How OTP adds an extra security layer

    Importance of session handling

    How backend security logic works in real applications

    Debugging real authentication issues (sessions, redirects, OTP)

Future Improvements

    Email-based OTP delivery

    OTP retry limits & account lockout

    JWT-based authentication

    Session expiration & timeout

    Deployment with HTTPS (cloud)

⭐ Why This Project Matters

    This project focuses on security mindset, not just functionality:

    Thinking like an attacker

    Defending authentication flows

    Balancing security with usability




📌 Author

K. Narsimhulu