import pandas as pd
import matplotlib.pyplot as plt

# Load the events data with state information
events_data = pd.read_csv('events_with_states.csv')

# Group the data by state and count the number of events in each state
events_by_state = events_data.groupby('state_name').size().reset_index(name='count')

# Create a bar chart showing the number of events in each state
plt.bar(events_by_state['state_name'], events_by_state['count'])
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Number of Events')
plt.title('Distribution of Events Across States')
plt.show()
