Python Data Cleaning: Bike Share Company Dataset
____________________________________________________________________________
Project Description
This project involves cleaning and preprocessing a dataset from a bike share company. The objective was to enhance data quality and prepare it for future exploratory analysis. The cleaned dataset includes customer details, sales, revenue, and profit-related data, providing insights for business decision-making.
________________


Key Features
* Data Cleaning:
   * Removed duplicate and blank rows.
   * Standardized column names by renaming and formatting.
   * Removed unnecessary columns with no analytical value.
   * Transformed financial data fields (e.g., removing $ and , symbols).
* Data Transformation:
   * Converted financial fields to numeric data types for analysis.
   * Added new calculated columns:
      * Contribution Margin (%)
      * Profit Per Item
      * Final Profit
      * Profit Margin (%).
________________


Dataset Information
* Data Source: Customer data from a bike share company.
* Sample Columns:
   * Customer Name: Name of the customer.
   * Age: Age of the customer.
   * revenue: Total revenue generated from the customer.
   * profit: Profit generated per customer.
   * Contribution_margin: Contribution margin percentage for each sale.
   * profit_margin: Profit margin percentage for each sale.
________________


Installation and Usage Instructions
1. Dataset:
   * Ensure the data.csv file is in the working directory.
2. Steps to Run:
   * Run the Python script (cleaned.py) to clean the dataset.
   * Use the cleaned dataset for analysis or visualization.
________________


Methodology/Approach
1. Initial Cleaning:
   * Removed duplicate and null rows.
   * Renamed columns to improve clarity and usability.
2. Column Removal:
   * Deleted unnecessary fields like Year, Month, Day, Age_Group, and Product_Category.
   * Removed columns with uniform or redundant values, such as Sub_Category.
3. Data Transformation:
   * Standardized financial fields (removed $, ,).
   * Converted financial columns to numeric types.
   * Added new calculated fields for profit and margin analysis.
________________


Key Insights/Results
* Prepared a cleaned and structured dataset for analysis.
* Generated new columns for advanced business metrics:
   * Profit margin.
   * Contribution margin.
   * Profit per item.
* Dataset ready for exploratory and visual analysis.
________________


Dependencies
* Python 3.x
* Libraries:
   * pandas
   * numpy
   * datetime
