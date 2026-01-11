import pandas as pd
import numpy as np
import sys
from data_cleaning_agent import DataCleaningAgent

# Fix encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Create sample data for testing
print("=" * 60)
print("DATA CLEANING AGENT - TEST RUN")
print("=" * 60)

# Create a sample dataset with various issues
data = {
    'name': ['John', 'jane', 'JOHN', 'Mary', 'mary', 'John', 'Bob'],
    'age': [25, 30, 25, None, 35, 25, 40],
    'city': ['New York', 'new york', 'NEW YORK', 'Boston', 'boston', 'New York', 'Chicago'],
    'salary': [50000, 60000, None, 70000, 55000, 50000, 80000],
    'department': ['IT', 'IT', 'IT', 'HR', 'HR', 'IT', 'Finance']
}

df = pd.DataFrame(data)

print("\n[INFO] Sample Dataset Created:")
print(df)
print("\n" + "=" * 60)

# Initialize the agent
agent = DataCleaningAgent(df)

# Run all cleaning steps
numeric_cols, categorical_cols = agent.data_overview()
agent.missing_values()

# For automated testing, we'll skip interactive inputs
# In real usage, you would interact with the prompts
print("\n[DUPLICATE] DUPLICATE ROW CHECK")
dup_count = agent.df.duplicated().sum()
print(f"Duplicate Rows Found: {dup_count}")
if dup_count > 0:
    print("(In interactive mode, you would be prompted to remove duplicates)")
    # Auto-remove for demo
    agent.df = agent.df.drop_duplicates()
    print("Duplicates removed (auto-mode).")
    print("Updated Shape:", agent.df.shape)
    agent.report.append(f"{dup_count} duplicate rows removed.")

print("\n[STANDARDIZE] STANDARDIZATION SUGGESTIONS")
print("(In interactive mode, you would be prompted for each column)")
print("Sample standardization would be applied to 'name' and 'city' columns")

# Generate final summary
agent.summary_report()

print("\n" + "=" * 60)
print("Final Cleaned Dataset:")
print(agent.df)
print("=" * 60)

