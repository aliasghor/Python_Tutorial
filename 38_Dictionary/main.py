# Dictionary is often called as an asociative array

data_dict = {
    "Name":"Ali",
    "Age":20,
    "University":"University Of Wollongong",
    "Places That Has Been visit":["Switzerland","Singapore","Malaysia","Bali"],
    "Citizen Of":"Indonesia"
}

print(data_dict)

# Indexing a dictionary
print("\nIndexing a dictionary is using a keys name")

print(f"Currently studying in: {data_dict['University']}")
print(f"Places that i have been visited: {data_dict['Places That Has Been visit']}")
print(f"I am a citizen of: {data_dict['Citizen Of']}")