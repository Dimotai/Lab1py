# Author: Tim Dai tfd5244@psu.edu (Myself)
# Collaborator: Matthew Bronstein msb5970@psu.edu
# Collaborator: Sana Tipnis sat5652@psu.edu
# Collaborator: Pradhyumna Adusumilli pza5189@psu.edu



temp = input("Enter temperature: ")
cOrF = input("Enter unit in F/f or C/c: ")
if(cOrF.lower() == "c"):
    print(f"{temp}° in Celsius is equivalent to {(float(temp)*9/5)+32}° Fahrenheit.")
elif(cOrF.lower() == "f"):
    print(f"{temp}° in Fahrenheit is equivalent to {(float(temp)-32)*5/9}° Celsius.")
else:
    print(f"Invalid unit({cOrF}).")
