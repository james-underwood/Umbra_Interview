import matplotlib.pyplot as plt
from data_reader import fetch_satellite_data
from data_processor import process_satellite_data
from data_visualizer import visualize_satellite_data
from data_calculations import *
def main():
    csv_file_path = 'database.csv'
    satellites = fetch_satellite_data(csv_file_path)
    #process_satellite_data(satellites)
    
    calculate_summary_statistics(satellites)
    calculate_correlation(satellites)
    analyze_distributions(satellites)
    analyze_time_series(satellites)

if __name__ == '__main__':
    main()
