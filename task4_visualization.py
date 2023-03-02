import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('events_with_states.csv')

df['created'] = pd.to_datetime(df['created'])

# Create a new column for the date (without time)
df['date'] = df['created'].dt.date

# Group the data by date and calculate the sum of eventValue for each day
daily_data = df.groupby('date')['eventValue'].sum().reset_index()
daily_data['cnt'] = df.groupby('date')['eventValue'].count().reset_index()['eventValue']
# Calculate the moving average of total daily eventValue (using a window size of 7 days)
window_size = 7
daily_data['moving_average'] = daily_data['eventValue'].rolling(window=window_size).mean() / 100
# Visualize the trends using a line chart
plt.plot(daily_data['date'], daily_data['moving_average'])
plt.title('Temporal trends of event data')
plt.xlabel('Date')
plt.ylabel('Total daily eventValue moving average (hundreds)')
plt.xticks(rotation=90)
plt.show()
