def find_settling_time(filename, tolerance=0.02):
    # Read data from file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Extracting time and y-values
    time_values = [float(line.split()[0]) for line in lines]
    y_values = [float(line.split()[1]) for line in lines]

    # Ask user for the steady state value
    steady_state = float(input("Enter the steady-state value: "))

    # Define the tolerance band
    lower_bound = (1 - tolerance) * steady_state
    upper_bound = (1 + tolerance) * steady_state

    # Traverse data from end to beginning to find the settling time
    for i in range(len(y_values) - 1, -1, -1):
        if y_values[i] < lower_bound or y_values[i] > upper_bound:
            # Return the time of the subsequent data point
            return time_values[i+1] if i+1 < len(time_values) else time_values[i]
    
    return time_values[0]  # If the system was always within the band

def main():
    filename = input("Enter the full path of the data file (e.g., D:\\path\\to\\data.txt): ")
    tolerance_percent = float(input("Enter the tolerance as a percentage (e.g., 2 for 2%): "))
    tolerance = tolerance_percent / 100.0

    settling_time = find_settling_time(filename, tolerance)
    print(f"The settling time is: {settling_time:.6f} units of time")

if __name__ == "__main__":
    main()