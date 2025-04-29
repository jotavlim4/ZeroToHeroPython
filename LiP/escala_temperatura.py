fahrenheit = float(input())
char = input()

if (char == "c" or char == "C"):
    escala = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit:.2f}F equivale a {escala:.2f}C")
else:
    escala = (5/9)*(fahrenheit - 32) + 273.15
    print(f"{fahrenheit:.2f}F equivale a {escala:.2f}K")  
