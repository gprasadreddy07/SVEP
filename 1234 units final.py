# prompt: take only top 5 and low 5 of data and generate as useval 

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file with the openpyxl engine
df = pd.read_excel('1234 units final.xlsx', engine='openpyxl')

# Assuming the Excel file has columns 'Mandal', 'ActivityName', 'VO', 'SanctionedAmount', 'TotalAmount'
# Group by 'Mandal' and sum the 'TotalAmount'
mandal_grouped = df.groupby('Mandal')['Total Amount'].sum().reset_index()

# Sort the Mandal data by Total Amount in descending order and take the top 5 and bottom 5
top_5_mandal = mandal_grouped.sort_values('Total Amount', ascending=False).head(5)
bottom_5_mandal = mandal_grouped.sort_values('Total Amount').head(5)

# Concatenate the top 5 and bottom 5 Mandal dataframes
mandal_top_bottom = pd.concat([top_5_mandal, bottom_5_mandal])

# Create a column chart for Mandal wise Total Amount (Top 5 and Bottom 5)
plt.bar(mandal_top_bottom['Mandal'], mandal_top_bottom['Total Amount'], label='Total Amount')
plt.xlabel('Mandal')
plt.ylabel('Total Amount')
plt.title('Mandal wise Total Amount (Top 5 and Bottom 5)')
plt.legend()
plt.show()

# Repeat the same process for Activity Name and VO

# Group by 'ActivityName' and sum the 'TotalAmount'
activity_grouped = df.groupby('Activity Name')['Total Amount'].sum().reset_index()

# Sort the Activity Name data by Total Amount in descending order and take the top 5 and bottom 5
top_5_activity = activity_grouped.sort_values('Total Amount', ascending=False).head(5)
bottom_5_activity = activity_grouped.sort_values('Total Amount').head(5)

# Concatenate the top 5 and bottom 5 Activity Name dataframes
activity_top_bottom = pd.concat([top_5_activity, bottom_5_activity])

# Create a bar chart for Activity Name wise Total Amount (Top 5 and Bottom 5)
activity_top_bottom.plot(kind='bar', x='Activity Name', y='Total Amount', title='Activity Name wise Total Amount (Top 5 and Bottom 5)')
plt.show()

# Group by 'VO' and sum the 'TotalAmount'
vo_grouped = df.groupby('VO')['Total Amount'].sum().reset_index()

# Sort the VO data by Total Amount in descending order and take the top 5 and bottom 5
top_5_vo = vo_grouped.sort_values('Total Amount', ascending=False).head(5)
bottom_5_vo = vo_grouped.sort_values('Total Amount').head(5)

# Concatenate the top 5 and bottom 5 VO dataframes
vo_top_bottom = pd.concat([top_5_vo, bottom_5_vo])

# Create a line chart for VO wise Total Amount (Top 5 and Bottom 5)
plt.plot(vo_top_bottom['VO'], vo_top_bottom['Total Amount'], label='Total Amount')
plt.xlabel('VO')
plt.ylabel('Total Amount')
plt.title('VO wise Total Amount (Top 5 and Bottom 5)')
plt.legend()
plt.show()
