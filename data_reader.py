import csv

def fetch_satellite_data(csv_file_path):
    """
    Fetches satellite data from a CSV file and returns a list of dictionaries.
    Each dictionary represents a satellite with its attributes as key-value pairs.
    """
    satellites = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            satellites.append(row)
    return satellites
