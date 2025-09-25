from tkinter import *
import random
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv(dotenv_path="C:\\Users\\admin\\Desktop\\GenAI dashboard\\.env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini Flash directly
model = genai.GenerativeModel("gemini-1.5-flash")

# Simulate sensor data
def get_sensor_data():
    return {
        "temperature": round(random.uniform(20, 80), 2),
        "voltage": round(random.uniform(3.0, 5.0), 2),
        "motion": random.choice(["Detected", "None"])
    }

# Update GUI labels with new sensor data
def update_labels():
    data = get_sensor_data()
    temp_label.config(text=f"Temperature: {data['temperature']} °C")
    volt_label.config(text=f"Voltage: {data['voltage']} V")
    motion_label.config(text=f"Motion: {data['motion']}")
    window.after(2000, update_labels)

from sentence_transformers import SentenceTransformer
import faiss

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base
with open("sensor_guide.txt", "r", encoding="utf-8") as f:
    documents = f.read().split("\n")

# Embed and index
doc_embeddings = embedder.encode(documents)
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)
# Diagnose sensor data using Gemini
def diagnose(sensor_data):
    query = f"Temperature: {sensor_data['temperature']}°C, Voltage: {sensor_data['voltage']}V, Motion: {sensor_data['motion']}"
    context = retrieve_context(query)

    prompt = f"""
    Context:
    {context}

    Sensor Readings:
    Temperature: {sensor_data['temperature']}°C
    Voltage: {sensor_data['voltage']}V
    Motion: {sensor_data['motion']}

    Based on the context and readings, suggest diagnostic actions.
    """

    try:
        response = model.generate_content(prompt)
        return {
            "status": "success",
            "suggestion": response.text.strip()
        }
    except Exception as e:
        return {
            "status": "fallback",
            "suggestion": f"Model error: {e}"
        }

def retrieve_context(query, top_k=3):
    query_embedding = embedder.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    return "\n".join([documents[i] for i in indices[0]])

# Button-triggered diagnosis and GUI update
def diagnose_and_update():
    sensor_data = {
        "temperature": temp_label.cget("text").split(": ")[1].split(" ")[0],
        "voltage": volt_label.cget("text").split(": ")[1].split(" ")[0],
        "motion": motion_label.cget("text").split(": ")[1]
    }

    result = diagnose(sensor_data)
    response_label.config(text=f"GenAI Suggestion: {result['suggestion']}")

# GUI setup
window = Tk()
window.title("AutoQuery - GenAI Troubleshooter")
window.geometry("500x350")

temp_label = Label(window, text="Temperature: -- °C", font=("Arial", 12))
temp_label.pack(pady=5)
volt_label = Label(window, text="Voltage: -- V", font=("Arial", 12))
volt_label.pack(pady=5)
motion_label = Label(window, text="Motion: --", font=("Arial", 12))
motion_label.pack(pady=5)

diagnose_button = Button(window, text="Diagnose", font=("Arial", 12), command=diagnose_and_update)
diagnose_button.pack(pady=10)

response_label = Label(window, text="GenAI Suggestion: --", wraplength=400, font=("Arial", 10), justify=LEFT)
response_label.pack(pady=5)

update_labels()

window.mainloop()
