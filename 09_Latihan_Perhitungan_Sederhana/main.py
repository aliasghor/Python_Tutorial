# Program konversi celcius ke satuan lain

print(20 * "=" + "Program konversi temperatur" + 20 * "=")

celcius = float(input("Masukan suhu dalem celcius: "))

print(f"Suhu dalem celcius: {celcius}")

# Reamur
reamur = (4 / 5) * celcius
print(f"Suhu dalem reamur: {reamur:.2f}")

# Fahrenheit
fahrenheit = (4 / 5) * celcius + 32
print(f"Suhu dalem fahrenheit: {fahrenheit:.2f}")

# Kelvin
kelvin = celcius + 273
print(f"Suhu dalem kelvin: {kelvin}")

# Fahrenheit to kelvin
fahrenheit = float(input("Insert a temperature in fahrenheit: "))
celcius = 5 / 9 * (fahrenheit - 32)
kelvin = celcius + 273

print(f"Temperature from fahrenheit to kelvin is: {kelvin:.2f}")

# Kelvin to fahrenheit
kelvin = float(input("Insert a temperature from kelvin to fahrenheit: "))
celcius = kelvin - 273
fahrenheit = (9 / 5 * celcius) + 32
print(f"Temperature from kelvin to fahrenheit is: {fahrenheit:.2f}") 
