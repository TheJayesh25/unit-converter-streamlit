# 🌐 Unit Converter Assistant

An interactive Streamlit app to convert between **distance**, **temperature**, and **currency** units — all backed by real Python logic and live exchange rates.

> 💡 Built as a modular, portfolio-friendly tool using clean Python functions and Streamlit UI.

---

## 🚀 Features

- 📏 Distance conversions — metric and imperial (e.g., km to miles, inches to yards)  
- 🌡️ Temperature conversions — Celsius, Fahrenheit, Kelvin  
- 💱 Currency conversions — live exchange rates via [ExchangeRate API](https://www.exchangerate-api.com/)  
- ⚡ Real-time feedback with a responsive UI  
- 🧩 Modular architecture with separate files for each conversion type  

---

## 🖥️ Live Demo

👉 [Launch the App](https://unit-converter-app-js25.streamlit.app/)

---

## 📦 Project Structure

```bash
unit_converter_app/
├── app.py # Streamlit UI
├── requirements.txt # Minimal dependencies
├── conversions/ # Modular Python logic
│ ├── temperature.py
│ ├── distance.py
│ └── currency.py
├── .gitignore
└── README.md
```

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/unit-converter-assistant.git
cd unit-converter-assistant
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Set Up API Key
Create a .env file in the project root:

EXCHANGE_RATE_API_KEY=your_api_key_here
🔑 You can get a free API key from [ExchangeRate](exchangerate-api.com)

### 4. Run the App Locally
```bash
streamlit run app.py
```

### 🧠 Tech Stack
- Python 3.8+
- Streamlit
- requests
- python-dotenv


### ✅ Features

- ✅ Modular, testable Python logic  
- ✅ Real-world currency API integration  
- ✅ Clean UI with Streamlit  
- ✅ Deploys in seconds via Streamlit Cloud


### 💡 Future Ideas

- 🔊 Voice input with speechrecognition
- 📈 Currency history chart (e.g., INR to USD over time)
- 🧠 Natural language input parsing (e.g., “Convert 5 feet to meters”)


### 🧑‍💻 Author
Jayesh Suryawanshi
🧠 Python Developer | 💡 AI Tools Builder | 🌍 Data & Engineering Enthusiast
📫 [LinkedIn](https://www.linkedin.com/in/jayesh-suryawanshi-858bb21aa/)

### 📜 License
MIT License — free to use, modify, and share.
---
Let me know if you want a `LICENSE` file or a badge-based header (like stars, forks, version, license).
