import kagglehub
import os
import pandas as pd

path = kagglehub.dataset_download("wordsforthewise/lending-club")

csv_filename = "accepted_2007_to_2018Q4.csv.gz"
full_path = os.path.join(path, csv_filename)

loan_data_accepted = pd.read_csv(full_path, low_memory=False, nrows=500000)

csv_filename = "rejected_2007_to_2018Q4.csv.gz"
full_path = os.path.join(path, csv_filename)

loan_data_rejected = pd.read_csv(full_path, low_memory=False, nrows=500000)

#print(loan_data_accepted.head())
#print(loan_data_rejected.head())

rej_data = loan_data_rejected[['Amount Requested', 'Risk_Score','Debt-To-Income Ratio', 'Employment Length']]
#print(rej_data.head())

acc_data = loan_data_accepted[[
    'loan_amnt', 'dti', 'emp_length', 'fico_range_low', 
    'fico_range_high', 'loan_status', 'int_rate', 'grade', 
    'annual_inc', 'home_ownership', 'purpose', 'addr_state'
]]
#print(acc_data.head())

acc_data["risk_score"] = (acc_data["fico_range_low"] + acc_data["fico_range_high"]) / 2

joined_data = pd.concat([acc_data, rej_data], ignore_index=True)
#print(joined_data.head())

os.makedirs("processed_data", exist_ok=True)

rej_data.to_csv(os.path.join("processed_data", "rejected_data.csv"), index=False)
acc_data.to_csv(os.path.join("processed_data", "accepted_data.csv"), index=False)
joined_data.to_csv(os.path.join("processed_data", "joined_data.csv"), index=False)