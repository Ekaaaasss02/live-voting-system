# 🗳️ Live Voting & Polling System

A modern **web-based Live Voting and Polling Machine** built using **Python (Flask)**. This project enables users to vote in real time through a clean and interactive interface while maintaining structured backend logic with database support.

---

## 🚀 Features

- 🎨 **Modern User Interface**  
  Attractive landing page with animated login screen.

- 👤 **User Registration Form**  
  Collects user details such as:
  - Name  
  - Age  
  - Gmail  
  - Phone Number  

- 🗳️ **Live Voting System**  
  Users can vote for multiple candidates.

- 📊 **Real-Time Vote Counting**  
  Votes are stored and counted using SQLite database.

- 🔐 **Admin Panel**  
  Add or manage candidates easily.

- 🧠 **SQLite Database Integration**  
  Lightweight and efficient backend storage.

- 🌐 **Client-Server Architecture**  
  Demonstrates core Computer Networks concepts.

---

## 🏗️ Project Structure

```bash
live-voting-system/
│── app.py                 # Main Flask backend
│── database.py            # Database creation/setup
│── requirements.txt       # Required Python packages
│── README.md              # Project documentation
│
├── database/
│   └── voting.db         # SQLite database
│
├── templates/
│   ├── index.html        # Landing page
│   ├── login.html        # Animated login page
│   ├── vote.html         # Voting page
│   ├── results.html      # Results page
│   └── admin.html        # Admin panel
│
└── static/
    └── style.css         # CSS styling

```
⚙️ Technologies Used
Frontend
HTML
CSS
JavaScript
Backend
Python
Flask
Database
SQLite
Version Control
Git
GitHub
🧪 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Ekaaaasss02/live-voting-system.git
cd live-voting-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create the Database
python database.py

4️⃣ Run the Flask Server
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

🔄 Application Flow
Landing Page
     ↓
Login Form
     ↓
Voting Page
     ↓
Submit Vote
     ↓
Results Page

🌐 Computer Networks Concepts Used
Client-Server Architecture
HTTP Request / Response Cycle
Multiple Client Handling
Real-Time Data Communication (can be extended using WebSockets)
🔮 Future Enhancements
🔴 Real-Time Voting using WebSockets
📊 Graphical Results Dashboard
🔐 Secure Authentication System
🧾 Voting History Tracking
⏱️ Live Poll Timer

👨‍💻 Author

Bismun Singh

🔗 GitHub: https://github.com/Ekaaaasss02
