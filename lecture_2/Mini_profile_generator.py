# function for determine life stage
def generate_profile(age: int):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

# Get user name & birth year
print("Hi anonymous user")
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")

# convert birth year to int
birth_year = int(birth_year_str)
# calculate current age
current_age = 2025 - birth_year

# get user hobbies
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

    if hobby.lower() == "stop":
        break

    hobbies.append(hobby)

# calculate live stage
life_stage = generate_profile(current_age)

# bild user profile
user_profile = {
    "name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies
}

# print user profile
print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")

# print hobbies
if len(hobbies) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")
