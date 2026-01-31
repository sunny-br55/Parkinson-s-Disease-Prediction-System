🧠 Parkinson’s Disease Prediction Web Application

📌 Project Description

This project is a Machine Learning-based web application that predicts whether a person is affected by Parkinson’s Disease using voice measurement data.
The system analyzes multiple biomedical voice parameters and classifies the patient as Healthy or Parkinson’s Positive.

The goal of this project is to demonstrate how Machine Learning models can be integrated with a modern web interface to build an end-to-end healthcare prediction system.

🧠 About Parkinson’s Disease

Parkinson’s Disease is a neurological disorder that affects movement, speech, and muscle control.
Early detection is important for timely treatment and better quality of life.

This system uses voice-based features such as jitter, shimmer, frequency, and noise ratios to help predict the presence of Parkinson’s Disease.

⚙️ Technologies Used
🔹 Machine Learning

Python

NumPy

Pandas

Scikit-learn

🔹 Web Development

Flask (Backend)

HTML

CSS

JavaScript

🔹 Dataset

UCI Parkinson’s Disease Dataset

Features: 22 biomedical voice parameters

Target: status

0 = Healthy

1 = Parkinson’s Disease



🔍 How the System Works

The dataset is loaded and preprocessed using Pandas.

A Machine Learning classifier (e.g., Random Forest / Logistic Regression / SVM) is trained using scikit-learn.

The trained model is saved as model.pkl.

A Flask web application loads the trained model
