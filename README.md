# 🏦 Smart Lender – Loan Approval Prediction System

A Machine Learning-based web application developed using Flask to predict loan approval based on applicant details. The project is deployed on Render for live access.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-success?style=for-the-badge)](https://smart-lender-loan-approval-prediction-sg6c.onrender.com)

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)

![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask)

---

# 🌐 Live Demo

### Render Deployment

https://smart-lender-loan-approval-prediction-sg6c.onrender.com

---

# 📸 Application Screenshots

## 🏠 Home Page

The home page welcomes users and provides access to the Smart Lender Loan Approval Prediction System.

<p align="center">
<img src="screenshots/home.png" width="900">
</p>

---

## 📝 Loan Prediction Form

Users enter applicant details such as gender, marital status, education, income, loan amount, credit history, and property area to predict loan approval.

<p align="center">
<img src="screenshots/loan_form.png" width="900">
</p>

---

## ✅ Prediction Result

The application predicts whether the loan is approved or rejected using the trained Machine Learning model.

<p align="center">
<img src="screenshots/prediction_result.png" width="900">
</p>

---

# 🎯 Project Objective

The objective of this project is to develop a Machine Learning-powered web application that predicts loan approval based on applicant details.

The system simplifies and automates the loan evaluation process by providing quick and reliable predictions through an easy-to-use web interface.

---

# 📖 Project Description

Financial institutions process numerous loan applications every day.

Evaluating each application manually is time-consuming and may lead to inconsistent decisions.

The **Smart Lender – Loan Approval Prediction System** automates this process using Machine Learning.

The application analyzes applicant information and predicts whether the loan is likely to be approved, helping improve efficiency, accuracy, and consistency in loan evaluation.

---

# ✨ Features

- Machine Learning-Based Loan Prediction
- Flask Web Application
- User-Friendly Interface
- Data Preprocessing
- Model Training and Evaluation
- Interactive Data Visualization using Matplotlib & Seaborn
- Input Validation
- Responsive User Interface
- Live Deployment using Render
- Organized Project Documentation

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| Scikit-learn | Machine Learning |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Jupyter Notebook | Machine Learning Workflow |
| HTML | Frontend Development |
| CSS | Styling |
| Git | Version Control |
| GitHub | Repository Hosting |
| Render | Cloud Deployment |

---

# 🤖 Machine Learning Algorithms

The following Machine Learning algorithms were trained and evaluated during the project:

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

After comparing the performance of all models, the best-performing model was selected and saved as **model.pkl**.

The trained model is integrated with the Flask application to predict loan approval in real time.

---

# 📂 Project Structure

```text
Smart-Lender-Loan-Approval-Prediction-System
│
├── 1. Brainstorming & Ideation
├── 2. Requirement Analysis
├── 3. Project Design Phase
├── 4. Project Planning Phase
├── 5. Project Development Phase
├── 6. Project Testing
├── 7. Project Documentation
├── 8. Project Demonstration
│
├── dataset
│   └── loan_prediction.csv
│
├── model
│   ├── model.pkl
│   └── scaler.pkl
│
├── screenshots
│
├── static
│   └── style.css
│
├── templates
│   ├── home.html
│   ├── predict.html
│   └── submit.html
│
├── Loan_Prediction_Using_ML.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```---

# ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/23ata05317/Smart-Lender-Loan-Approval-Prediction-System.git
```

---

### Step 2: Navigate to the Project Folder

```bash
cd Smart-Lender-Loan-Approval-Prediction-System
```

---

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Machine Learning Notebook

Open **Loan_Prediction_Using_ML.ipynb** and execute all the cells.

This notebook performs:

- Data Cleaning
- Exploratory Data Analysis
- Data Preprocessing
- Model Training
- Model Evaluation
- Saves:
  - `model/model.pkl`
  - `model/scaler.pkl`

---

### Step 5: Run the Flask Application

```bash
python app.py
```

---

### Step 6: Open in Browser

Visit:

```
http://127.0.0.1:5000
```

---

# 🤖 Machine Learning Workflow

The Machine Learning workflow followed in this project is:

- Dataset Collection
- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis (EDA)
- Label Encoding
- Feature Selection
- Data Balancing using SMOTE
- Feature Scaling using StandardScaler
- Train-Test Split
- Model Training
- Model Evaluation
- Accuracy Comparison
- Model Saving (`model.pkl` & `scaler.pkl`)
- Flask Application Integration
- Loan Approval Prediction

---

# 📁 Repository Contents

This repository contains:

- Flask Source Code
- Machine Learning Notebook
- Trained Machine Learning Models
- Loan Prediction Dataset
- HTML Templates
- CSS Files
- Project Documentation
- Testing Reports
- Demonstration Files
- Deployment Configuration

---

# 🚀 Future Enhancements

The project can be further enhanced by implementing:

- User Authentication
- Database Integration
- Cloud Database Support
- Admin Dashboard
- Loan History Management
- Email Notifications
- Additional Machine Learning Models
- Improved Prediction Accuracy
- PDF Report Generation
- API Integration

---

# 👥 Team Members

- **Doranala Surya Teja** *(Team Lead)*
- **Shaik Alfisha Maheen**
- **Shaik Sonu**

---

# 📄 License

This project was developed for **academic purposes** as part of the **SkillWallet Capstone Project**.

---

# 🙏 Acknowledgement

We sincerely thank **SkillWallet** for providing the opportunity to work on this Machine Learning project.

This project helped us gain practical knowledge in:

- Machine Learning
- Data Preprocessing
- Flask Web Development
- Git & GitHub
- Cloud Deployment using Render

---

# ⭐ Support

If you found this project useful, please consider giving this repository a **⭐ Star** on GitHub.

It helps support the project and encourages future improvements.

---

# 📬 Contact

For any suggestions or queries regarding this project, feel free to reach out through GitHub.

GitHub Repository:

https://github.com/23ata05317/Smart-Lender-Loan-Approval-Prediction-System

---

## ⭐ Thank You!

Thank you for visiting our **Smart Lender – Loan Approval Prediction System** repository.

We hope this project is useful for learning Machine Learning and Flask-based web application development.