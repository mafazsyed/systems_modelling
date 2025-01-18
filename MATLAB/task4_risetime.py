def interpolate(x1, y1, x2, y2, y_target):
    return x1 + (y_target - y1) * (x2 - x1) / (y2 - y1)

def main():
    # Input data
    line1 = input("Enter the first data point (x1 y1): ")
    x1, y1 = map(float, line1.split())
    
    line2 = input("Enter the second data point (x2 y2): ")
    x2, y2 = map(float, line2.split())

    # Target value
    y_target = 0.9

    # Interpolation
    x_target = interpolate(x1, y1, x2, y2, y_target)
    print(f"The interpolated x value for y = {y_target} is: {x_target}")

if __name__ == "__main__":
    main()