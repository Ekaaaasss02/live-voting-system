 Live Voting & Polling System

A web-based **Live Voting and Polling Machine** built using **Python (Flask)**, designed for real-time voting with a clean UI and structured backend.

---

🚀 Features

- 🎨 Modern UI (Landing Page + Animated Login)
- 👤 User Entry Form (Name, Age, Gmail, Phone)
- 🗳️ Voting System with Multiple Candidates
- 📊 Live Vote Counting (Database-based)
- 🔐 Admin Panel to Add Candidates
- 🧠 SQLite Database Integration
- 🌐 Client-Server Architecture (Computer Networks Concept)

---

 🏗️ Project Structure
 live-voting-system
│
├── app.py # Main Flask backend
├── database.py # Database setup
├── requirements.txt
├── README.md
│
├── database
│ └── voting.db # SQLite database
│
├── templates
│ ├── index.html # Landing page
│ ├── login.html # Animated login page
│ ├── vote.html # Voting page
│ ├── results.html # Results page
│ └── admin.html # Admin panel
│
└── static
└── style.css # Styling


 ⚙️ Technologies Used

- Frontend:** HTML, CSS, JavaScript
- Backend:** Python (Flask)
- Database:** SQLite
- Version Control:** Git & GitHub



 🧪 How to Run the Project

1️⃣ Clone the Repository

 bash
git clone https://github.com/YOUR_USERNAME/live-voting-system.git
cd live-voting-system

Install Dependencies
pip install -r requirements.txt

Create Database
python database.py

Run the Server
python app.py

Open in Browser
http://127.0.0.1:5000


Application Flow
Landing Page
    ↓
Login Form
    ↓
Voting Page
    ↓
Submit Vote
    ↓
Results Page


Computer Networks Concepts Used
Client-Server Architecture
HTTP Request/Response Cycle
Multiple Client Handling
Real-Time Data Updates (extendable with WebSockets)

Future Enhancements
🔴 Real-time voting (WebSockets)
📊 Graphical results dashboard
🔐 Secure authentication system
🧾 Voting history tracking
⏱️ Live poll timer


Author

Bismun Singh

GitHub: https://github.com/Ekaaaasss02