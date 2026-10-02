def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(lb):
    return lb / 2.20462

def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

options = {
    "1": ("Kilometres to miles", km_to_miles),
    "2": ("Miles to kilometres", miles_to_km),
    "3": ("Kilograms to pounds", kg_to_pounds),
    "4": ("Pounds to kilograms", pounds_to_kg),
    "5": ("Celsius to Fahrenheit", c_to_f),
    "6": ("Fahrenheit to Celsius", f_to_c),
}

print("Unit Converter")
for key, (name, _) in options.items():
    print(f"{key}. {name}")

choice = input("Choose an option: ")
if choice in options:
    value = float(input("Enter the value: "))
    result = options[choice][1](value)
    print(f"Result: {result:.2f}")
else:
    print("Invalid option")
