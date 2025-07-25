import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Sample extended dataset
data = pd.DataFrame({
    'Skill': ['Coding', 'Writing', 'Data Analysis', 'Marketing', 'Design'],
    'Interest': ['Technology', 'Media', 'Business', 'Art', 'Technology'],
    'Education': ['Bachelor', 'Master', 'Bachelor', 'High School', 'Bachelor'],
    'WorkStyle': ['Independent', 'Team', 'Team', 'Independent', 'Team'],
    'GoalType': ['Entrepreneurial', 'Creative', 'Analytical', 'Executive', 'Academic'],
    'CodingLevel': ['High', 'None', 'Medium', 'Low', 'High'],
    'LearningStyle': ['Self-paced', 'Instructor-led', 'Blended', 'Blended', 'Self-paced'],
    'Tools': ['Python', 'MS Word', 'Excel', 'Photoshop', 'Figma'],
    'Location': ['Remote', 'On-site', 'Hybrid', 'Remote', 'On-site'],
    'Income': ['High', 'Medium', 'High', 'Low', 'Medium'],
    'Career': ['Software Engineer', 'Content Writer', 'Data Analyst', 'Marketing Manager', 'UX Designer']
})

X = data.drop('Career', axis=1)
y = data['Career']

categorical_features = X.columns.tolist()
preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier())
])

pipeline.fit(X, y)

# Save model
with open("career_model.pkl", "wb") as file:
    pickle.dump(pipeline, file)

print("✅ Model trained and saved successfully!")
