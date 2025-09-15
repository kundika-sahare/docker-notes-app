# 📝 Notes App with Flask + Docker

A simple **Notes App** built with **Flask** and containerized using **Docker**.  
This project allows you to add, view, and manage notes. Data is stored in a local JSON file.

---

## 🚀 Features
- Add and view notes easily  
- Backend built with Flask (Python)  
- Lightweight storage using `notes.json`  
- Fully containerized with Docker → no manual dependency setup needed  

---

## 🛠️ Tech Stack
- Python 3
- Flask
- Docker

---

## 📂 Project Structure
notes-app/
│── app.py # Flask main application file
│── requirements.txt # Python dependencies
│── Dockerfile # Docker build instructions
│── README.md # Project documentation
│── notes.json # (auto-created) JSON file to store notes

## ▶️ Run Without Docker
1. Clone the repo:
   ```bash
   git clone https://github.com/kundika-sahare/docker-notes-app.git
   cd notes-app
2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

## ▶️ Run With Docker

1. Build the image:
   docker build -t notes-app .

2. Run the container:
   docker run -p 5000:5000 notes-app

3. Open in browser:
   http://127.0.0.1:5000


---

## 📜 License
This project is licensed under the **MIT License**.  
Feel free to use and modify it as you like.  
