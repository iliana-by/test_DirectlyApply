import requests
import csv
from datetime import datetime
from multiprocessing import Pool, cpu_count

start_time = datetime.now()

# Define the API endpoint URL
url = "https://us-state-api.herokuapp.com/"


def process_row(row):
    # Extract the latitude and longitude from the "geo" field
    geo = row['geo']
    lon, lat = geo.strip('POINT()').split(' ')

    # Make a GET request to the API endpoint with the latitude and longitude as parameters
    params = {'lat': lat, 'lon': lon}
    response = requests.get(url, params=params)
    # Extract the state data from the API response and add it to the current row
    state_data = response.json()['state']
    for d in ('name', 'slug', 'postal'):
        try:
            row['state_' + d] = state_data[d]
        except TypeError:
            row['state_' + d] = "Not Found"
    return row


def multiproc():
# Open the CSV file containing the event data
    with open('event_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        # Process each row in parallel using a pool of worker processes
        with Pool(cpu_count()) as pool:
            results = pool.map(process_row, rows)

        # Write the updated rows to a new CSV file
        with open('events_with_states.csv', 'w', newline='') as outfile:
            fields = list(results[0].keys())
            writer = csv.DictWriter(outfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(results)

    print(datetime.now() - start_time)


if __name__ == '__main__':
    multiproc()