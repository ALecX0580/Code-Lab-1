weather_condition = input("Select the weather condition from the folloawing options: \033[1msunny, rainy, cloudy, other\033[0m ").lower()
temperature = float(input("What is current temperature? "))

if weather_condition == "sunny" and temperature >= 25:
    print(f"\nIt's sunny and warm, wear some shorts and sunglasses.")
elif weather_condition == "rainy":
    print(f"\nIt's rainy, carry a Unbrella with you.")
elif temperature <= 10:
    print(f"\nIt's cold, wear a jacket")
elif weather_condition == "cloudy": 
    print(f"\nIt's cloudy but it's dry, just wear light clothes")
else:
    print(f"\nNo specific suggestions, dress whatever is comfortable")
    