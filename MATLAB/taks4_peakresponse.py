def calculate_overshoot(data):
    # Extract y-values (responses)
    y_values = [float(line.split()[1]) for line in data]
    
    # Identify the maximum value and the steady-state value
    max_value = max(y_values)
    steady_state_value = y_values[-1]
    
    # Calculate overshoot
    overshoot = (max_value - steady_state_value) / steady_state_value * 100
    return overshoot

def main():
    # Get data from user
    data = []
    print("Enter your data (type 'stop' when done):")
    while True:
        line = input()
        if line.lower() == 'stop':
            break
        data.append(line)
    
    overshoot = calculate_overshoot(data)
    print(f"The overshoot is: {overshoot:.2f}%")

if __name__ == "__main__":
    main()