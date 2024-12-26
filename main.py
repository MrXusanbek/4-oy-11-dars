#4 - oy 11 - dars
import asyncio

# 1.
async def remove_digits_from_password(password):
    result = ""
    i = 0
    while i < len(password):
        if not password[i].isdigit():
            result += password[i]
        i += 1
    print(f"Updated Password: \033[92m{result}\033[0m")

# 2.
async def first_10_characters(text):
    result = ""
    i = 0
    while i < min(len(text), 10):
        result += text[i]
        i += 1
    print(f"First 10 Characters: \033[92m{result}\033[0m")

# 3.
async def remove_digits_from_name(name):
    result = ""
    i = 0
    while i < len(name):
        if not name[i].isdigit():
            result += name[i]
        i += 1
    print(f"Cleaned Name: \033[92m{result}\033[0m")

# 4.
async def lowercase_and_remove_spaces(text):
    result = ""
    i = 0
    while i < len(text):
        if not text[i].isspace():
            result += text[i].lower()
        i += 1
    print(f"Processed Text: \033[92m{result}\033[0m")

# 5.
async def extract_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0
    while i < len(text):
        if text[i] in vowels:
            result += text[i]
        i += 1
    print(f"Vowels: \033[92m{result}\033[0m")

# 6.
async def replace_ab_with_hash(word):
    result = ""
    i = 0
    while i < len(word):
        if i < len(word) - 1 and word[i] == "a" and word[i + 1] == "b":
            result += "#"
            i += 2
        else:
            result += word[i]
            i += 1
    print(f"Processed Word: \033[92m{result}\033[0m")

# 7.
async def reverse_if_digits(text):
    if text.isdigit():
        print(f"Reversed Text: \033[92m{text[::-1]}\033[0m")
    else:
        print("Input is not fully numeric.")

# 8.
async def remove_middle_character(word):
    length = len(word)
    if length > 0:
        middle = length // 2
        result = word[:middle] + word[middle + 1:]
        print(f"Word without Middle Character: \033[92m{result}\033[0m")

# 9.
async def lowercase_if_ends_with_a(name):
    if name.endswith("a"):
        print(f"Processed Name: \033[92m{name.lower()}\033[0m")
    else:
        print(f"Name: \033[92m{name}\033[0m")

# 10.
async def remove_duplicate_characters(text):
    result = ""
    seen = set()
    i = 0
    while i < len(text):
        if text[i] not in seen:
            result += text[i]
            seen.add(text[i])
        i += 1
    print(f"Unique Characters: \033[92m{result}\033[0m")

# 11.
async def uppercase_if_vowels_only(word):
    vowels = "aeiouAEIOU"
    if all(char in vowels for char in word):
        print(f"Uppercase Word: \033[92m{word.upper()}\033[0m")
    else:
        print(f"Word: \033[92m{word}\033[0m")

# 12.
async def get_weather(city):
    import aiohttp
    api_key = "YOUR_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                print(f"Weather in {city}: \033[92m{temp}°C, {description}\033[0m")
            else:
                print(f"Failed to fetch weather data for {city}.")


async def main():
    await remove_digits_from_password("pass123word")
    await first_10_characters("ThisIsAReallyLongText")
    await remove_digits_from_name("Will2024")
    await lowercase_and_remove_spaces("HELLO World")
    await extract_vowels("Programming")
    await replace_ab_with_hash("abracadabra")
    await reverse_if_digits("123456789")
    await remove_middle_character("Python")
    await lowercase_if_ends_with_a("Anna")
    await remove_duplicate_characters("mississippi")
    await uppercase_if_vowels_only("aeiou")
    await get_weather("Tashkent")

asyncio.run(main())
