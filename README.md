# 💪 Gym AI Assistant (Powered by Mistral API)

A simple **AI-powered Gym & Fitness Assistant** built with **Python** and the **Mistral API**.
This assistant is designed to answer **only gym, fitness, and health-related questions** such as workouts, nutrition, recovery, biomechanics, and exercise science.

The goal of this project is to create a **focused AI assistant** that behaves like a **personal fitness trainer**, providing helpful and science-backed responses while ignoring unrelated topics.

---

## 🚀 Features

* 🏋️ Answers questions about **workouts and exercises**
* 🧠 Explains the **science behind training** (physiology, biomechanics, etc.)
* 🥗 Provides guidance on **diet and nutrition**
* 😴 Gives advice on **sleep and recovery**
* 💊 Discusses **supplements and fitness strategies**
* 🛑 Blocks non-fitness questions to keep the assistant focused
* 💬 Interactive **command line chat interface**

Example topics the assistant can handle:

* Muscle building and hypertrophy
* Strength training and progressive overload
* Exercise form and technique
* Workout routines and training splits
* Fat loss and body recomposition
* Nutrition and protein intake
* Sleep and recovery for athletes
* Fitness biomechanics and exercise science

---

## 🧠 How It Works

The assistant uses:

1. **Mistral AI Model** – to generate intelligent responses.
2. **System Prompt Restriction** – forces the AI to behave like a gym trainer.
3. **Keyword Filtering** – ensures questions are related to fitness before sending them to the AI.
4. **CLI Chat Interface** – lets users interact with the assistant directly from the terminal.

If a user asks something unrelated, the assistant replies:

```text
I can only answer gym and fitness related questions.
```

---

## 🔑 Add Your Mistral API Key

Create a `.env` file in the project folder:

```env
MISTRAL_API_KEY=your_api_key_here
```

You can get an API key from:
https://console.mistral.ai/

---

## ▶️ Running the Assistant

Run the Python file:

```bash
python gym_assistant.py
```

You will see:

```text
💪 Gym AI Assistant
Ask any gym or fitness question
Type 'exit' to quit
```

---

## 💬 Example Usage

```text
You: how do I grow my biceps?

Assistant:
To grow your biceps effectively you should focus on progressive overload,
proper exercise selection like barbell curls and hammer curls,
and maintaining adequate protein intake.

You: how does creatine work?

Assistant:
Creatine helps regenerate ATP, the main energy molecule used
during short and intense workouts like weightlifting.

You: who is the president of India?

Assistant:
I can only answer gym and fitness related questions.
```

---

## 📚 Topics the Assistant Understands

* Gym workouts
* Strength training
* Hypertrophy science
* Exercise physiology
* Biomechanics
* Anatomy and muscles
* Diet and macronutrients
* Supplements
* Recovery and sleep
* Injury prevention
* Fitness equipment

---

## 🛠 Technologies Used

* **Python**
* **Mistral AI API**
* **python-dotenv**
* **CLI Interface**

---

## 📈 Future Improvements

This project can be expanded into a **full AI fitness coach**, including:

* 🧾 AI **Workout Plan Generator**
* 🥗 AI **Diet Planner**
* 📊 Progress Tracking
* 🎙 Voice Fitness Assistant
* 🌐 Web App (FastAPI + React)
* 📚 RAG with fitness research papers

---

## 👨‍💻 Author

Built by **Ebin Prabhakar**
B.Tech Artificial Intelligence & Data Science

---

**Train smart. Stay consistent. Build strength. 💪**
