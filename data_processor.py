import matplotlib.pyplot as plt	

def process_satellite_data(satellites):
    for satellite in satellites:
        satellite_name = satellite['Official Name of Satellite']
        country = satellite['Country/Organization of UN Registry']
        operator = satellite['Operator/Owner']
        country_of_operator = satellite['Country of Operator/Owner']
        users = satellite['Users']
        purpose = satellite['Purpose']
        detailed_purpose = satellite['Detailed Purpose']
        class_of_orbit = satellite['Class of Orbit']
        type_of_orbit = satellite['Type of Orbit']
        longitude_of_geo_orbit = satellite['Longitude of Geosynchronous Orbit (Degrees)']
        perigee = satellite['Perigee (Kilometers)']
        apogee = satellite['Apogee (Kilometers)']
        eccentricity = satellite['Eccentricity']
        inclination = satellite['Inclination (Degrees)']
        period = satellite['Period (Minutes)']
        launch_mass = satellite['Launch Mass (Kilograms)']
        dry_mass = satellite['Dry Mass (Kilograms)']
        power = satellite['Power (Watts)']
        date_of_launch = satellite['Date of Launch']
        expected_lifetime = satellite['Expected Lifetime (Years)']
        contractor = satellite['Contractor']
        country_of_contractor = satellite['Country of Contractor']
        launch_site = satellite['Launch Site']
        launch_vehicle = satellite['Launch Vehicle']
        cospar_number = satellite['COSPAR Number']
        norad_number = satellite['NORAD Number']

def process_satellite_data(satellites):
    """
    Processes the satellite data by performing specific tasks.
    Modify this function based on your project requirements.
    """
    purposes = [satellite['Purpose'] for satellite in satellites]

    # Count the number of satellites for each purpose
    purpose_counts = {}
    for purpose in purposes:
        purpose_counts[purpose] = purpose_counts.get(purpose, 0) + 1

    # Group purposes with small counts into 'Other' category
    threshold = 5  # Adjust the threshold as per your preference
    filtered_purpose_counts = {}
    other_count = 0
    for purpose, count in purpose_counts.items():
        if count >= threshold:
            filtered_purpose_counts[purpose] = count
        else:
            other_count += count

    if other_count > 0:
        filtered_purpose_counts['Other'] = other_count

    # Create the bar chart
    purposes = list(filtered_purpose_counts.keys())
    counts = list(filtered_purpose_counts.values())

    plt.bar(purposes, counts)
    plt.xlabel('Purpose')
    plt.ylabel('Count')
    plt.title('Satellites by Purpose (Grouped)')
    plt.xticks(rotation=45)
    plt.show()

