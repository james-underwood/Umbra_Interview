# Umbra_Interview

# Satellite Data Summary Statistics

This program is a demonstration of Python knowledge created for the Umbra interview. It calculates summary statistics for satellite data provided in a CSV format.

## Description

The program reads satellite data from a CSV file and calculates summary statistics for the launch mass, power, and expected lifetime of the satellites. The calculated statistics include mean, standard deviation, minimum, and maximum values for each attribute.

## Features

- Reads satellite data from a CSV file
- Handles various data formats and converts them to appropriate numeric values
- Calculates summary statistics for launch mass, power, and expected lifetime
- Prints the calculated statistics to the console

## How to Use

1. Ensure that you have Python 3.x installed on your machine.

2. Clone this repository or download the files to your local machine.

3. Prepare a CSV file containing the satellite data in the following format:
Official Name of Satellite,Country/Organization of UN Registry,Operator/Owner,Country of Operator/Owner,Users,Purpose,Detailed Purpose,Class of Orbit,Type of Orbit,Longitude of Geosynchronous Orbit (Degrees),Perigee (Kilometers),Apogee (Kilometers),Eccentricity,Inclination (Degrees),Period (Minutes),Launch Mass (Kilograms),Dry Mass (Kilograms),Power (Watts),Date of Launch,Expected Lifetime (Years),Contractor,Country of Contractor,Launch Site,Launch Vehicle,COSPAR Number,NORAD Number
AAUSat-4,NR,University of Aalborg,Denmark,Civil,Earth Observation,Automatic Identification System (AIS),LEO,Sun-Synchronous,0,442,687,0.0177,98.2,95.9,1,,,4/25/2016,,University of Aalborg,Denmark,Guiana Space Center,Soyuz 2.1a,2016-025E,41460
ABS-2,NR,Asia Broadcast Satellite Ltd.,Multinational,Commercial,Communications,,GEO,,75,35778,35793,0.000178,0.08,1436.03,6330,,16000,2/6/2014,15,Space Systems/Loral,USA,Guiana Space Center,Ariane 5 ECA,2014-006A,39508

4. Modify the `satellites` list of dictionaries in the `main.py` file to match the data in your CSV file.

5. Open a terminal or command prompt and navigate to the project directory.

6. Run the program by executing the following command:

7. The program will calculate the summary statistics and display them in the console output.

## Dependencies

This program requires the following Python modules:

- csv
- statistics

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

