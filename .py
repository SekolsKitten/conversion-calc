def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ").upper()

            if unit == 'C':
                converted_temperature = celsius_to_fahrenheit(temperature)
                print(f"{temperature} Celsius is {converted_temperature:.2f} Fahrenheit.")
            elif unit == 'F':
                 converted_temperature = fahrenheit_to_celsius(temperature)
                 print(f"{temperature} Fahrenheit is {converted_temperature:.2f} Celsius.")
            else:
                print("Invalid input. Please enter 'F' or 'C'.")

            another_conversion = input("Do you want to do another conversion? (yes/no): ").upper()
            if another_conversion != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter a valid number for temperature.")

if __name__ == "__main__":
    main()



