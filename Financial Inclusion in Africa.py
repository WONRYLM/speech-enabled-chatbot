import pandas as pd

# Load dataset CSV file (replace with your local path or downloaded CSV)
df = pd.read_csv('C:/Users/USER/Downloads/Financial_inclusion_dataset.csv', encoding='latin1')

# Path C:\Users\USER\Downloads\Financial_inclusion_dataset.csv
# Check the first few rows of the dataset
print(df.head()) 

# Show general info
print(df.info())

# Show first 5 rows
print(df.head())

# Basic stats for numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Generate a profiling report
from pandas_profiling import ProfileReport

profile = ProfileReport(df, title='Financial Inclusion Africa Profiling Report')
profile.to_file("financial_inclusion_report.html")

# Data Cleaning Steps
# Handle missing values
# Fill missing values with the mode for categorical columns
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Fill missing values with the mean for numerical columns
for col in df.select_dtypes(include='number').columns:
    df[col].fillna(df[col].median(), inplace=True)

# Check for duplicates
# Remove duplicates 
print(f"Duplicates before: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
print(f"Duplicates after: {df.duplicated().sum()}")

# Outliers handling
# Visualize outliers using boxplots
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(df['household_size'])
plt.show()

# Capping outliers
Q1 = df['household_size'].quantile(0.25)
Q3 = df['household_size'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['household_size'] = df['household_size'].clip(lower_bound, upper_bound)

# Remove outliers based on IQR
# Q1 = df['household_size'].quantile(0.25)
# Q3 = df['household_size'].quantile(0.75)    
# IQR = Q3 - Q1
# df = df[~((df['household_size'] < (Q1 - 1.5 * IQR)) | (df['household_size'] > (Q3 + 1.5 * IQR)))]

# Encoding categorical variables
from sklearn.preprocessing import LabelEncoder

cat_cols = ['country', 'location_type', 'cellphone_access', 'gender_of_respondent', 
            'relationship_with_head', 'marital_status', 'education_level', 'job_type']

le_dict = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le  # Save encoders to use later in Streamlit app

# Show the cleaned data
print(df.head())

# Prepare the cleaned data for further analysis or modeling
df['bank_account'] = df['bank_account'].map({'Yes': 1, 'No': 0})

# Splitting the dataset into features and target variable
X = df.drop(['uniqueid', 'bank_account'], axis=1)
y = df['bank_account']

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train a Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Save the model for later use
import joblib
joblib.dump(clf, 'financial_inclusion_model.joblib')

# Also save label encoders
joblib.dump(le_dict, 'label_encoders.joblib')
# End of the financial inclusion analysis script