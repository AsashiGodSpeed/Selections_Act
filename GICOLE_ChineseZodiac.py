def chinese_zodiac(year):
    zodiac_animals = ["Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger",
                      "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey"]
    start_year = 1

    if year < start_year:
        print("The Chinese zodiac cycle starts from 1924. Please enter a valid year.")
    else:
        zodiac_index = (year - start_year) % 12
        zodiac_sign = zodiac_animals[zodiac_index]
        print(f"The Chinese zodiac sign for the year {year} is {zodiac_sign}.")


try:
    year = int(input("Enter a year to find the Chinese zodiac sign: "))
    chinese_zodiac(year)
except ValueError:
    print(" Please enter a year: ")
