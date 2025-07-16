# 🌍 Sustainable Shopping Assistant

An **AI/ML-powered chatbot** designed to empower consumers to make more eco-conscious purchasing decisions and reduce household waste — directly supporting **UN Sustainable Development Goal 12: Responsible Consumption and Production**.

---

## 📘 Project Overview

This project implements an interactive chatbot that acts as a personal guide for sustainable shopping. It addresses the challenge consumers face in finding reliable and quick information about:
- Eco-friendly alternatives
- Waste reduction strategies
- The environmental impact of commonly purchased products

Built with a **modular architecture**, the system is designed for future enhancements, including machine learning capabilities and personalized recommendations.

---

## 🚀 Features

- 🛒 **Suggest Eco-Friendly Alternatives**  
  Recommends sustainable options for everyday items (e.g., beeswax wrap instead of plastic wrap).

- 🍽️ **Offer Food Waste Reduction Tips**  
  Provides practical ways to minimize household food waste.

- ♻️ **Explain Environmental Impact**  
  Gives insights into the ecological footprint of products like beef, avocados, etc.

- 🌿 **Provide General Sustainability Tips**  
  Broader advice on sustainable living and shopping habits.

- 💬 **Interactive Interface**  
  Available via:
  - Command-Line Interface (CLI)
  - Graphical User Interface (GUI) using Tkinter

---

## 🛠️ Technical Stack

- **Language**: Python 3.x  
- **Libraries**:
  - `re` – for regex-based Natural Language Understanding (NLU)
  - `tkinter` – for GUI interface
- **Web Visualization (Demo)**:
  - `Chart.js` (via CDN)
  - `Tailwind CSS` (via CDN)

---

## 📁 Project Structure
```
sustainable_shopping_assistant/
├── main.py # GUI application entry point
├── chatbot.py # Core chatbot logic
├── nlu.py # Natural Language Understanding module
└── knowledge_base.py # Predefined knowledge database
```

---

## 🔄 How It Works (Architecture)

1. **User Input** via CLI or GUI
2. **NLU Module (`nlu.py`)**  
   - Uses regex & keyword matching  
   - Identifies intent (e.g., request for alternative/tip)  
   - Extracts entity (e.g., "plastic wrap")
3. **Chatbot Logic (`chatbot.py`)**  
   - Matches intent/entity with knowledge base
4. **Knowledge Base (`knowledge_base.py`)**  
   - Python dictionaries/lists with curated eco-data
5. **Bot Response** is generated and shown to the user

---
