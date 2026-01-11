import pandas as pd
import numpy as np


class DataCleaningAgent:
    """
    Data Cleaning & EDA Agent
    Author: Kaushik Chereddy (extendable)
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.original_shape = df.shape
        self.report = []

    # ---------------- STEP 1: DATA OVERVIEW ---------------- #
    def data_overview(self):
        print("\n[DATA OVERVIEW]")
        print(f"Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")
        print("\nColumns & Data Types:")
        print(self.df.dtypes)

        numeric_cols = self.df.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()

        print("\nNumerical Columns:", numeric_cols)
        print("Categorical Columns:", categorical_cols)

        self.report.append("Data overview completed.")
        return numeric_cols, categorical_cols

    # ---------------- STEP 2: MISSING VALUES ---------------- #
    def missing_values(self):
        print("\n[MISSING VALUES] MISSING VALUES REPORT")

        missing_count = self.df.isnull().sum()
        missing_percent = (missing_count / len(self.df)) * 100

        missing_df = pd.DataFrame({
            'Missing_Count': missing_count,
            'Missing_Percent': missing_percent.round(2)
        })

        missing_df = missing_df[missing_df.Missing_Count > 0]

        if missing_df.empty:
            print("No missing values found.")
        else:
            print(missing_df.sort_values(by="Missing_Percent", ascending=False))

        self.report.append("Missing values analysis completed.")
        return missing_df

    # ---------------- STEP 3: DUPLICATE HANDLING ---------------- #
    def check_duplicates(self):
        print("\n[DUPLICATE] DUPLICATE ROW CHECK")

        dup_count = self.df.duplicated().sum()
        print(f"Duplicate Rows Found: {dup_count}")

        if dup_count > 0:
            decision = input("Do you want to remove duplicates? (yes/no): ").lower()
            if decision == "yes":
                self.df = self.df.drop_duplicates()
                print("Duplicates removed.")
                print("Updated Shape:", self.df.shape)
                self.report.append(f"{dup_count} duplicate rows removed.")
            else:
                print("Duplicates retained.")
                self.report.append("Duplicates retained by user.")
        else:
            self.report.append("No duplicate rows found.")

    # ---------------- STEP 4: STANDARDIZATION ---------------- #
    def standardize_categories(self, categorical_cols):
        print("\n[STANDARDIZE] STANDARDIZATION SUGGESTIONS")

        for col in categorical_cols:
            unique_vals = self.df[col].dropna().unique()

            # Skip high-cardinality columns (scalability)
            if len(unique_vals) > 50:
                continue

            normalized = {val: str(val).strip().title() for val in unique_vals}
            if len(set(normalized.values())) < len(unique_vals):
                print(f"\nColumn: {col}")
                print("Detected inconsistent values:")
                print(unique_vals)
                decision = input("Apply standardization? (yes/no): ").lower()

                if decision == "yes":
                    self.df[col] = self.df[col].map(lambda x: normalized.get(x, x))
                    print(f"{col} standardized.")
                    self.report.append(f"{col} standardized.")
                else:
                    self.report.append(f"{col} not standardized (user decision).")

    # ---------------- STEP 5: FINAL SUMMARY ---------------- #
    def summary_report(self):
        print("\n[SUMMARY] FINAL CLEANING SUMMARY")
        print("Original Shape:", self.original_shape)
        print("Final Shape:", self.df.shape)

        print("\nActions Taken:")
        for action in self.report:
            print("-", action)

        print("\nDataset is ready for analysis or modeling.")

