import matplotlib.pyplot as plt

def visualize_satellite_data(satellites):
    """
    Visualizes the satellite data by creating plots or charts.
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

