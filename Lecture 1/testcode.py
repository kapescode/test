def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight / (height ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value according to the standard categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    interpretation = interpret_bmi(bmi)

    # Display results
    print("Your BMI is:", round(bmi, 2))
    print("Interpretation:", interpretation)

if __name__ == "__main__":
    main()