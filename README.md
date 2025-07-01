# 📬 Email/SMS Spam Classifier 🕵️‍♀️

A lightweight, ML-powered web app to detect whether a message is 🚫 spam or ✅ legit. Built using Python, scikit-learn, and Streamlit — no NLTK, no fuss!

---

## 🧠 Tech Stack

🖥️ Frontend:  
• Streamlit (for the interactive web interface)  
🧪 Backend & ML:  
• Scikit-learn  
• Pandas, NumPy  
• Regex (for tokenization & preprocessing)  
• TF-IDF vectorizer + Multinomial Naive Bayes model  

---

## 🚀 Features

✨ Minimal UI — enter any message to test  
📊 Pre-trained ML model (no need to retrain)  
🧼 Clean, regex-based preprocessing  
📦 No NLTK or heavy dependencies  
💻 One-click local deployment

---

## 🗃️ Folder Structure

```text
📁 email-spam-classifier/
├── app.py              # Streamlit app script
├── vectorizer.pkl      # Saved TF-IDF vectorizer
├── spam_model.pkl      # Trained Naive Bayes model
└── README.md           # You are here!

```

## 🛠️ How to Run Locally

1. ⬇️ Clone the repository:
```bash
git clone https://github.com/your-username/email-spam-classifier.git
cd email-spam-classifier

```

2. 📦 Install the dependencies:
   ```bash
   pip install -r requirements.txt



3. ▶️ Launch the Streamlit app:

   ```bash
   streamlit run app.py


## 🌐 The app will open in your browser at:

http://localhost:8501
