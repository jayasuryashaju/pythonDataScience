"""
monuments
"""

city = input("enter a city : ")
monument = ""

if city == "Delhi" or city == "DELHI" or city == "delhi":
    monument = "Red Fort"
elif city == "Agra" or city == "AGRA" or city == "agra":
    monument = "Taj  Mahal"
elif city == "Jaipur" or city == "JAIPUR" or city == "jaipur":
    monument = "Jal Mahal"

print("The monument is : ", monument)
