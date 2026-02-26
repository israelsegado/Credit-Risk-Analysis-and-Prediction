This project utilizes Machine Learning techniques to automate credit decision-making based on real-world data from LendingClub. The model predicts whether a loan application will be approved or rejected by analyzing applicants' financial health and credit history.

Project Overview
The system processes a unified dataset of 500,000 records, balancing both accepted and rejected loan requests. Through Exploratory Data Analysis (EDA) and predictive modeling, we identify the critical thresholds that financial institutions use to determine creditworthiness.

Libraries used
Language: Python 3.x
Data Analysis: Pandas, NumPy
Visualization: Seaborn, Matplotlib
Machine Learning: Scikit-Learn (Logistic Regression, Random Forest)

Key Results
After comparing multiple approaches, the final Random Forest model achieved significant performance milestones:

- Global Accuracy: 90%
- Primary Driver: Risk Score (FICO) was identified as the most influential factor, followed by the Debt-To-Income (DTI) ratio.

How the Simulator Works
The project features a real-time simulation engine. By inputting four key variables, the model provides an instant credit decision:

- Loan Amount: The total capital requested.
- Risk Score: The applicant's credit score (FICO).
- DTI: The Debt-to-Income ratio percentage.
- Employment Length: Years of professional stability.
- The engine outputs the application status along with the specific Acceptance/Rejection probability.

Repository Structure
data_preprocessing.py: Script for cleaning and merging the raw Kaggle datasets.
01_Credit_Analysis.ipynb: Notebook containing deep EDA, risk tier segmentation, and correlation heatmaps.
02_Prediction_Model.ipynb: Machine Learning pipeline, model comparison (Logistic Regression vs. Random Forest), and the final simulation engine.
