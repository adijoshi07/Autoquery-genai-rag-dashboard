import random
import time

def generate_sensor_data():
    while True:
        data = {
            "temperature": round(random.uniform(20, 80), 2),
            "voltage": round(random.uniform(3.0, 5.0), 2),
            "motion": random.choice(["Detected", "None"])
        }
        print(f"Sensor Log: {data}")
        time.sleep(2)  # Simulate real-time stream

if __name__ == "__main__":
    generate_sensor_data()