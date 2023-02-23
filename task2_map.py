import folium
import pandas as pd

# Define a function to style the state names
def style_function(feature):
    return {
        'color': 'black',
        'weight': 0.5,
        'fillOpacity': 0,
        'dashArray': '5, 5'
    }

# Read the CSV file with state data
df = pd.read_csv('events_with_states.csv')

# Group the data by state_postal and count the number of rows for each group
counts = df.groupby('state_postal').count().reset_index()

# Rename the count column to cnt
counts = counts.rename(columns={'geo': 'cnt'})

# Select only the state_postal and cnt columns
counts = counts[['state_postal', 'cnt']]
# print(counts)
counts = counts[counts['state_postal'] != "Not Found"]
# Create a map centered on the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

state_geo = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
)
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=counts,
    columns=["state_postal", "cnt"],
    key_on="feature.id",
    fill_color="RdYlGn",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Count of events",
).add_to(m)

# Create a GeoJSON layer with state names
state_names = folium.GeoJson(
    state_geo,
    name='state names',
    style_function=style_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['name'],
        aliases=['State Name: '],
        sticky=True,
        opacity=0.9,
        direction='top'
    )
)

state_names.add_to(m)

# Display the map
m.save("map.html")




