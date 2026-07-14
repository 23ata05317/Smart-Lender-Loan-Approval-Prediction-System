# 🏦 Smart Lender – Loan Approval Prediction System

A Machine Learning-based web application developed using **Python, Flask, and Scikit-learn** to predict whether a loan application is **Approved** or **Rejected** based on applicant details.

The project was developed as part of the **SkillWallet Internship** and is deployed on **Render** for live access.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-success?style=for-the-badge)](https://smart-lender-loan-approval-prediction-sg6c.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)

---

# 🌐 Live Demo

### Render Deployment

https://smart-lender-loan-approval-prediction-sg6c.onrender.com

---

# 🎥 Project Demo Video

Watch the complete project demonstration here:

https://drive.google.com/file/d/1cWUUWlCeQN96xQUtEoKztUTRGImE0OwC/view?usp=sharing

---

# 📸 Application Screenshots

## 🏠 Home Page

The home page welcomes users and provides access to the Smart Lender Loan Approval Prediction System.

<p align="center">
<img src="screenshots/home.png" width="900">
</p>

---

## 📝 Loan Prediction Form

Users enter applicant details such as Gender, Married Status, Education, Income, Loan Amount, Credit History, and Property Area.

<p align="center">
<img src="screenshots/loan_form.png" width="900">
</p>

---

## ✅ Prediction Result

The Machine Learning model predicts whether the loan application is **Approved** or **Rejected**.

<p align="center">
<img src="screenshots/prediction_result.png" width="900">
</p>

---

# 🎯 Project Objective

The objective of this project is to develop a Machine Learning-powered web application that predicts loan approval based on applicant information.

The application helps banks and financial institutions make faster, more accurate, and consistent loan approval decisions while helping applicants understand their eligibility before applying.

---

# 📖 Project Description

Loan approval in many financial institutions is still a time-consuming manual process.

The **Smart Lender – Loan Approval Prediction System** automates this process using Machine Learning.

The application analyzes applicant information such as:

- Gender
- Marital Status
- Dependents
- Education
- Self Employment
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

and predicts whether the loan is likely to be approved.

---

# ✨ Features

- Machine Learning-based Loan Approval Prediction
- User-friendly Web Interface
- Data Preprocessing
- Model Training & Evaluation
- Interactive Data Visualization
- Input Validation
- Responsive Design
- Flask Web Application
- Live Deployment using Render
- Complete Project Documentation

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
| Jupyter Notebook | Machine Learning Development |
| HTML5 | Frontend |
| CSS3 | Styling |
| Git | Version Control |
| GitHub | Repository Hosting |
| Render | Cloud Deployment |

---

# 🤖 Machine Learning Algorithms

The following algorithms were trained and evaluated:

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

After comparing all models, the best-performing model was selected and saved as:

- **model.pkl**
- **scaler.pkl**

These files are loaded by the Flask application for real-time loan prediction.

---

# 📂 Project Structure

```text
Smart-Lender-Loan-Approval-Prediction-System
│
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
├── 6. Project Testing/
├── 7. Project Documentation/
├── 8. Project Demonstration/
│
├── dataset/
│   └── loan_prediction.csv
│
├── model/
│   ├── model.pkl
│   └── scaler.pkl
│
├── screenshots/
│   ├── home.png
│   ├── loan_form.png
│   └── prediction_result.png
│
├── static/
│   └── style.css
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── submit.html
│
├── Loan_Prediction_Using_ML.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/23ata05317/Smart-Lender-Loan-Approval-Prediction-System.git
```

---

### 2️⃣ Navigate to the Project Folder

```bash
cd Smart-Lender-Loan-Approval-Prediction-System
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Machine Learning Notebook

Open:

```
Loan_Prediction_Using_ML.ipynb
```

Run all cells.

The notebook performs:

- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis
- Label Encoding
- SMOTE
- Feature Scaling
- Model Training
- Model Evaluation
- Saves:
  - model.pkl
  - scaler.pkl

---

### 5️⃣ Run the Flask Application

```bash
python app.py
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

# 🤖 Machine Learning Workflow

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
- Model Saving
- Flask Integration
- Loan Prediction

---

# 📁 Repository Contents

This repository contains:

- Flask Source Code
- Machine Learning Notebook
- Loan Prediction Dataset
- Trained Models
- HTML Templates
- CSS Files
- Project Documentation
- Performance Testing Reports
- Project Demonstration Files
- Deployment Configuration

---

# 🚀 Future Enhancements

- User Authentication
- Database Integration
- Admin Dashboard
- Loan History Management
- Email Notifications
- REST API
- Cloud Database Support
- Improved Prediction Accuracy
- PDF Report Generation
- Additional Machine Learning Models

---

# 👥 Team Members

- **Doranala Surya Teja** *(Team Lead)*
- **Shaik Alfisha Maheen**
- **Shaik Sonu**

---

# 📄 License

This project was developed for academic purposes as part of the **SkillWallet Internship Program**.

---

# 🙏 Acknowledgement

We sincerely thank **SkillWallet** for providing us the opportunity to work on this Machine Learning project.

This project helped us gain practical knowledge in:

- Machine Learning
- Data Analysis
- Flask Development
- Git & GitHub
- Cloud Deployment using Render

---

# ⭐ Support

If you found this project helpful,

⭐ **Please Star this Repository**

It motivates us to build more useful projects.

---

# 📬 Contact

**GitHub Repository**

https://github.com/23ata05317/Smart-Lender-Loan-Approval-Prediction-System

---

## ⭐ Thank You!

Thank you for visiting our **Smart Lender – Loan Approval Prediction System** repository.

We hope this project helps you learn **Machine Learning**, **Flask Web Development**, and **Deployment using Render**.