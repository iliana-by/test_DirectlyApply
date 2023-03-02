import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a pandas dataframe
df = pd.read_csv('events_with_states.csv')

# Group the data by state and sum the eventValue, divided by 1000
state_totals = df.groupby('state_name')['eventValue'].sum() / 100

# Create a bar plot of the state totals
state_totals.plot(kind='bar')
plt.xlabel('State')
plt.ylabel('Event Value (hundreds)')
plt.title('Sum of Event Value by State')
plt.show()
