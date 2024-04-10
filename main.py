# Remove the first item from a Dictionary in Python

a_dict = {
    'site': 'bobbyhadz.com',
    'topic': 'Python',
    'id': 100
}

first_key = next(iter(a_dict))
print(first_key)  # 👉️ site

first_value = a_dict.pop(first_key)
print(first_value)  # 👉️ bobbyhadz.com

print(a_dict)  # 👉️ {'topic': 'Python', 'id': 100}