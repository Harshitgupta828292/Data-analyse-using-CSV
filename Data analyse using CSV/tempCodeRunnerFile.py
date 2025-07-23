import pandas as pd


# CSV file ko read karo
dataFrame = pd.read_csv("C:\Users\Harshitramji11\Downloads\Amazon Sales data (1).csv")

# Groupby ka use karo (yahan 'Region' ke hisaab se)
group = dataFrame.groupby('Region')

# Sum ka use karo (yahan 'Total Revenue' ka sum)
sum_state = group['Total Revenue'].sum()
print("Har Region ka Total Revenue:")
print(sum_state)