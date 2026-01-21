def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(f):
    return f / 3.28084

def show_menu():
    print("\n--- File / Unit Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Exit")

def main():
    print("Welcome to the Conversion Utility!")
    
    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == '5':
            print("Exiting converter. Bye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                val = float(input("Enter value to convert: "))
                if choice == '1':
                    print(f"{val}°C is {celsius_to_fahrenheit(val):.2f}°F")
                elif choice == '2':
                    print(f"{val}°F is {fahrenheit_to_celsius(val):.2f}°C")
                elif choice == '3':
                    print(f"{val} meters is {meters_to_feet(val):.2f} feet")
                elif choice == '4':
                    print(f"{val} feet is {feet_to_meters(val):.2f} meters")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
