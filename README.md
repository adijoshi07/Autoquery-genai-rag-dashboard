AutoQuery Live – Real-Time Sensor Diagnostics with GenAI + RAG

AutoQuery Live is a Python-based dashboard that reads live sensor data and uses AI to suggest diagnostic actions. It combines real-time simulation, context retrieval, and Gemini-powered suggestions to help troubleshoot issues intelligently.

---

🔧 What This Project Does

- Simulates sensor readings (temperature, voltage, motion)
- Retrieves relevant information from a knowledge base using RAG (Retrieval-Augmented Generation)
- Uses Gemini to generate smart suggestions based on both sensor data and retrieved context
- Displays everything in a simple GUI built with Tkinter

---

📁 Files Included

- gui_dashboard.py – Main dashboard with GenAI and RAG integration
- rag.py – Handles embedding and retrieval of context
- sensor_simulator.py – Simulates live sensor data
- sensor_guide.txt – Knowledge base for diagnostics
- requirements.txt – Python packages needed to run the project

---

⚙ How to Run

1. Install dependencies
   `bash
   pip install -r requirements.txt
   `

2. Add your Gemini API key  
   Create a .env file in the project folder:
   `
   GEMINIAPIKEY=yourkeyhere
   `

3. Run the dashboard
   `bash
   python gui_dashboard.py
   `

---

🧠 Technologies Used

- Python
- Tkinter
- FAISS
- SentenceTransformers
- Gemini (Google Generative AI)

---

🎯 Purpose

This project was built for a hackathon track focused on Dynamic RAG and real-time AI applications. It shows how GenAI can be combined with live data and retrieved context to make smarter decisions.

---

🙋 Author

Aditi – Passionate about AI, backend logic, and building intelligent dashboards that solve real-world problems.
