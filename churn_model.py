# churn_model.py
# # HAD TO CREATE A VIRTUAL ENVIRONMENT TO INSTALL PANDAS_PROFILING

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
#from pandas_profiling import ProfileReport  
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv('Expresso_churn_dataset.csv',  encoding='latin1')  

# Basic info
print(df.head())
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Check duplicates
print(f"Duplicates: {df.duplicated().sum()}")

# Drop duplicates 
df = df.drop_duplicates()

# Handle missing values
# For numerical columns fill with median 
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# For categorical columns fill with mode
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].apply(lambda col: col.fillna(col.mode()[0]))

# Drop columns with too many missing values
df = df.drop(columns=['ZONE1', 'ZONE2'])  # Adjust if needed

# Encode categorical variables
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# Handle outliers using IQR method
numerical_cols = ['MONTANT', 'FREQUENCE_RECH', 'REVENUE', 'ARPU_SEGMENT','FREQUENCE', 'DATA_VOLUME', 'ON_NET', 'ORANGE', 'TIGO', 'REGULARITY', 'FREQ_TOP_PACK']

for col in numerical_cols:
    if col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]


# Feature selection
X = df.drop(columns=['user_id', 'CHURN'])
y = df['CHURN']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'expresso_churn_model.pkl')
print("Model saved as expresso_churn_model.pkl")

# Generate profiling report
# profile = ProfileReport(df, title='Expresso Churn Dataset Report', explorative=True)
# profile.to_file("expresso_churn_report.html")
profile = ProfileReport(df, title='Expresso Churn Dataset Report')
profile.to_file("expresso_churn_report.html")
print("Profiling report saved as expresso_churn_report.html")
