Sustainable Shopping Assistant 🌍🌱
An AI/ML-powered chatbot designed to empower consumers to make more eco-conscious purchasing decisions and reduce household waste, directly supporting UN Sustainable Development Goal 12: Responsible Consumption and Production.

Project Overview
This project implements an interactive chatbot that serves as a personal guide for sustainable shopping. It addresses the challenge consumers face in finding reliable and quick information about eco-friendly alternatives, waste reduction, and the environmental impact of products. Built with a modular architecture, it lays the groundwork for advanced AI/ML integrations.

Features
The Sustainable Shopping Assistant can currently:

Suggest Eco-Friendly Alternatives: Provides suggestions for common household and grocery items (e.g., alternatives to plastic wrap, single-use coffee pods).

Offer Food Waste Reduction Tips: Gives practical advice on how to minimize food waste at home.

Explain Environmental Impact: Provides insights into the environmental footprint of certain products (e.g., beef, avocados).

Provide General Sustainability Tips: Offers broad advice for more sustainable living and shopping.

Interactive Interface: Available via a simple Command-Line Interface (CLI) and a Graphical User Interface (GUI) built with Tkinter.

Technical Stack
Language: Python 3.x

Core Libraries:

re (Regular Expressions) for Natural Language Understanding (NLU)

tkinter (Python's standard GUI library) for the graphical interface

chart.js (via CDN) for data visualization in the web showcase

Styling (Web Showcase): Tailwind CSS (via CDN)

Information Architecture: Designed for intuitive user exploration and understanding.

Project Structure
The project is organized into modular Python files for clarity and maintainability:

sustainable_shopping_assistant/
├── main.py             # Entry point for the GUI application
├── chatbot.py          # Core chatbot logic: processes input, gets responses
├── nlu.py              # Natural Language Understanding: classifies intent and extracts entities
└── knowledge_base.py   # Stores all curated data (alternatives, tips, impacts)

How It Works (Current Architecture)
The chatbot operates on a rule-based system, forming a strong foundation for future ML enhancements:

User Input: The user types a query into the CLI or GUI.

NLU Module (nlu.py): Uses regular expressions and keyword matching to analyze the input, identify the user's intent (e.g., asking for an alternative, tips, or impact), and extract any relevant entities (e.g., "plastic bags").

Chatbot Logic (chatbot.py): Based on the identified intent and entity, this module queries the knowledge_base.py.

Knowledge Base (knowledge_base.py): A collection of Python dictionaries and lists containing pre-defined eco-friendly alternatives, food waste tips, and environmental impact information.

Bot Response: The chatbot constructs and delivers a relevant response to the user.

Setup and Installation
To run this project locally, follow these steps:

Clone the repository (or create the files manually):

git clone <repository_url_here> # If hosted on Git
cd sustainable_shopping_assistant

If you're creating files manually, ensure all .py files (main.py, chatbot.py, nlu.py, knowledge_base.py) are in the same directory.

Ensure Python is installed: This project requires Python 3.x. You can download it from python.org.

No external Python libraries are strictly required beyond standard library modules for the core chatbot. Tkinter is usually included with Python installations.

Usage
You can interact with the chatbot via two interfaces:

1. Command-Line Interface (CLI)
This is useful for quick testing of the core logic.

Open your terminal or command prompt.

Navigate to the sustainable_shopping_assistant directory.

Run the chatbot.py file directly:

python chatbot.py

Type your queries (e.g., "food waste tips", "eco-friendly alternative for plastic wrap", "environmental impact of beef"). Type quit or exit to end the conversation.

2. Graphical User Interface (GUI)
This provides a more user-friendly experience.

Open your terminal or command prompt.

Navigate to the sustainable_shopping_assistant directory.

Run the main.py file:

python main.py

A new window will appear where you can type your questions and interact with the chatbot.

Future Enhancements (Towards Advanced AI/ML)
The current project serves as a strong foundation. Future development will focus on integrating more sophisticated AI/ML techniques:

ML-Based NLU: Transition from rule-based regex to trained machine learning models (e.g., using Scikit-learn for intent classification and SpaCy for Named Entity Recognition) for improved accuracy and understanding of diverse user phrasing.

Personalized Recommendation System: Implement a recommendation engine (content-based or collaborative filtering) to offer more tailored sustainable product suggestions.

Knowledge Graph Integration: Connect to external, dynamic sustainability databases and APIs to expand the chatbot's knowledge base and ensure up-to-date information.

Sentiment Analysis: Incorporate sentiment analysis to better understand user emotions and provide more empathetic responses.

Deployment: Explore deploying the chatbot as a web service (e.g., using Flask/Django) or integrating it into a mobile application.

Contribution
Feel free to fork this repository, suggest improvements, or contribute to its development.