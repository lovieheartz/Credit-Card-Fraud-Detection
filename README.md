# 💳 Credit Card Fraud Detection

This project demonstrates a machine learning approach to detecting fraudulent credit card transactions using a real-world dataset. The model is deployed as a Flask web application with an interactive dashboard that accepts user input and displays predictions in real-time.

---

## 📝 Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)
- [Results](#results)
- [Conclusion](#conclusion)

---

## 📌 Introduction

Credit card fraud is a major concern for financial institutions. Fraudulent transactions are rare but can cause significant losses. This project utilizes machine learning to classify transactions as either legitimate or fraudulent based on a variety of anonymized features.

---

## 📂 Dataset

- Source: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Features: 30 (including anonymized PCA features `V1` to `V28`, `Amount`, and `Time`)
- Imbalance: 99.83% legitimate, 0.17% fraud

---

## 🛠 Technologies Used

- **Python 3.x**
- **Pandas**, **NumPy** – Data handling
- **Matplotlib**, **Seaborn** – Visualization
- **Scikit-learn** – Preprocessing and modeling
- **XGBoost** – Advanced classification model
- **Flask** – Web application framework
- **HTML/CSS + Bootstrap** – Frontend design

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fraud-detection-app.git
cd fraud-detection-app

2. **Install dependencies**

Make sure you have Python installed. Then install the required libraries:

```bash
pip install -r requirements.txt

3.**Run the Flask app**

```bash
python app.py

