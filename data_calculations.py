import datetime
import statistics
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def calculate_summary_statistics(satellites):
    def convert_to_float(value):
        value = value.replace(',', '').replace('+', '')  # Remove comma and '+'
        if '(' in value:
            value = value.split('(')[0].strip()  # Remove text in parentheses
        if '-' in value:
            value_range = value.split('-')
            value = sum(float(v) for v in value_range) / len(value_range)  # Calculate average of the range
        if 'yrs' in value:
            value = value.split('yrs')[0].strip()  # Remove 'yrs' text
        return float(value) if value else 0.0
        if 'yr' in value:
            value = value.split('yr')[0].strip()  # Remove 'yr' text
        return float(value) if value else 0.0

    launch_masses = []
    powers = []
    expected_lifetimes = []

    for satellite in satellites:
        launch_mass = convert_to_float(satellite['Launch Mass (Kilograms)'])
        power = convert_to_float(satellite['Power (Watts)'])
        expected_lifetime = convert_to_float(satellite['Expected Lifetime (Years)'])

        launch_masses.append(launch_mass)
        powers.append(power)
        expected_lifetimes.append(expected_lifetime)

    launch_mass_mean = sum(launch_masses) / len(launch_masses)
    launch_mass_std = statistics.stdev(launch_masses)
    launch_mass_min = min(launch_masses)
    launch_mass_max = max(launch_masses)

    power_mean = sum(powers) / len(powers)
    power_std = statistics.stdev(powers)
    power_min = min(powers)
    power_max = max(powers)

    lifetime_mean = sum(expected_lifetimes) / len(expected_lifetimes)
    lifetime_std = statistics.stdev(expected_lifetimes)
    lifetime_min = min(expected_lifetimes)
    lifetime_max = max(expected_lifetimes)

    print("Launch Mass Summary Statistics:")
    print(f"Mean: {launch_mass_mean}")
    print(f"Standard Deviation: {launch_mass_std}")
    print(f"Minimum: {launch_mass_min}")
    print(f"Maximum: {launch_mass_max}")

    print("Power Summary Statistics:")
    print(f"Mean: {power_mean}")
    print(f"Standard Deviation: {power_std}")
    print(f"Minimum: {power_min}")
    print(f"Maximum: {power_max}")

    print("Expected Lifetime Summary Statistics:")
    print(f"Mean: {lifetime_mean}")
    print(f"Standard Deviation: {lifetime_std}")
    print(f"Minimum: {lifetime_min}")
    print(f"Maximum: {lifetime_max}")

def calculate_correlation(satellites):
    launch_masses = [float(satellite['Launch Mass (Kilograms)']) for satellite in satellites]
    powers = [float(satellite['Power (Watts)']) for satellite in satellites]
    expected_lifetimes = [float(satellite['Expected Lifetime (Years)']) for satellite in satellites]

    mass_power_correlation = statistics.correlation(launch_masses, powers)
    mass_lifetime_correlation = statistics.correlation(launch_masses, expected_lifetimes)
    power_lifetime_correlation = statistics.correlation(powers, expected_lifetimes)

    print("Correlation between Launch Mass and Power:", mass_power_correlation)
    print("Correlation between Launch Mass and Expected Lifetime:", mass_lifetime_correlation)
    print("Correlation between Power and Expected Lifetime:", power_lifetime_correlation)


def plot_distribution(data, attribute_name):
    plt.hist(data, bins=10)
    plt.xlabel(attribute_name)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {attribute_name}')
    plt.show()


def analyze_distributions(satellites):
    launch_masses = [float(satellite['Launch Mass (Kilograms)']) for satellite in satellites]
    powers = [float(satellite['Power (Watts)']) for satellite in satellites]
    expected_lifetimes = [float(satellite['Expected Lifetime (Years)']) for satellite in satellites]

    plot_distribution(launch_masses, 'Launch Mass')
    plot_distribution(powers, 'Power')
    plot_distribution(expected_lifetimes, 'Expected Lifetime')

def convert_to_datetime(date_string):
    return datetime.datetime.strptime(date_string, '%m/%d/%Y')

def analyze_time_series(satellites):
    launch_dates = [convert_to_datetime(satellite['Date of Launch']) for satellite in satellites]
    expected_lifetimes = [float(satellite['Expected Lifetime (Years)']) for satellite in satellites]

    plt.plot_date(launch_dates, expected_lifetimes, '-')
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xlabel('Launch Date')
    plt.ylabel('Expected Lifetime (Years)')
    plt.title('Expected Lifetime of Satellites over Time')
    plt.xticks(rotation=45)
    plt.show()
