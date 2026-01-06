# 🔮 Next Word Prediction using LSTM & Early Stopping

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://next-word-prediction-using-lstm-early-stopping-0007.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)

A Deep Learning project that predicts the next word in a given sequence of text using **Long Short-Term Memory (LSTM)** networks. The model is trained with **Early Stopping** to prevent overfitting.

🔗 **Live Demo:** [Click here to try the app](https://next-word-prediction-using-lstm-early-stopping-0007.streamlit.app/)

---

## 📌 Project Overview

Next Word Prediction is a fundamental task in **Natural Language Processing (NLP)**. This project demonstrates how to build a predictive model that learns from textual data to suggest the most probable next word.

### ✨ Key Features
* 🧠 **LSTM Architecture:** Captures long-term dependencies in text sequences.
* 🛑 **Early Stopping:** Monitors validation loss to stop training at the optimal point.
* ⚡ **Interactive UI:** Real-time predictions via Streamlit.
* 🔢 **Custom Tokenization:** Converts text to numerical sequences using Keras Tokenizer.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | 🐍 Python 3.11 |
| **DL Framework** | 🤖 TensorFlow / Keras |
| **Web Framework** | 👑 Streamlit |
| **Computation** | 🧮 NumPy |
| **Serialization** | 🥒 Pickle |

---

## 📂 Project Structure

```bash
├── 📄 app.py                   # Main Streamlit application
├── 📁 model/
│   ├── 🧠 next_word_model.h5   # Trained LSTM model
│   └── 🥒 tokenizer.pickle     # Saved Tokenizer object
├── 📁 notebooks/
│   └── 📓 training.ipynb       # Model training notebook
├── 📄 requirements.txt         # Dependencies
└── 📄 README.md                # Documentation
