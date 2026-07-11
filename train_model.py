import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("dataset/loan_prediction.csv")

# Display first 5 rows
print(df.head())

# Plot style
plt.style.use("fivethirtyeight")

# Applicant Income Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["ApplicantIncome"], kde=True)
plt.title("Applicant Income Distribution")
plt.show()

# Loan Amount Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["LoanAmount"], kde=True)
plt.title("Loan Amount Distribution")
plt.show()

# Count Plot for Gender
plt.figure(figsize=(5,4))
sns.countplot(x="Gender", data=df)
plt.title("Gender Count")
plt.show()

# Count Plot for Education
plt.figure(figsize=(5,4))
sns.countplot(x="Education", data=df)
plt.title("Education Count")
plt.show()

# Count Plot for Credit History
plt.figure(figsize=(5,4))
sns.countplot(x="Credit_History", data=df)
plt.title("Credit History")
plt.show()
# -----------------------------
# Bivariate Analysis
# -----------------------------

# Gender vs Married
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", hue="Married", data=df)
plt.title("Gender vs Married")
plt.show()

# Education vs Self Employed
plt.figure(figsize=(6,4))
sns.countplot(x="Education", hue="Self_Employed", data=df)
plt.title("Education vs Self Employed")
plt.show()

# Property Area vs Loan Amount Term
plt.figure(figsize=(8,4))
sns.countplot(x="Loan_Amount_Term", hue="Property_Area", data=df)
plt.title("Loan Amount Term vs Property Area")
plt.show()
# -----------------------------
# Multivariate Analysis
# -----------------------------
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()