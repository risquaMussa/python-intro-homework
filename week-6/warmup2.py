#Warmup 2: Functions that Return Values
def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius

print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"72°F = {fahrenheit_to_celsius(72):.1f}°C")


