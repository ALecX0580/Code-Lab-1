name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

personal_info = {
    "name": name,
    "age": age,
    "country": country
}

print(f"\nName: {personal_info['name']}\nage: {personal_info['age']}\ncountry: {personal_info['country']}")