import pandas as pd

import matplotlib.pyplot as plt

# Group by a column and sum another column

# Read the CSV file
dataFrame = pd.read_csv("C:\\Users\\Harshitramji11\\Downloads\\Amazon Sales data (1).csv")
print("Our dataframe:", dataFrame)
grouped = dataFrame.groupby("Region")["Total Profit"].sum()

# Plot the result
grouped.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.title("Total Profit by Region")
plt.show()
# Define the path to save the Excel file
save_path = "C:\\Users\\Harshitramji11\\Downloads\\Amazon_Sales_data.xlsx"

# Save to Excel
dataFrame.to_excel(save_path, index=False, engine='openpyxl')
print(f"Excel file saved successfully at: {save_path}")