# Looping dictionary Without using the dictionary methods
print(20 * "=" + " Looping dictionary Without using the dictionary methods " + 20 * "=")

alis_identity = {
    "Name":"Ali Masyhuri Asghor",
    "Age":20,
    "University":"University Of Wollongong",
    "Places That Has Been Visited":["Switzerland","Malaysia","Bali","Singapore"],
    "Citizen Of":"Indonesia"
}

for identity in alis_identity:
    print(identity)

# Looping dictionary using the dictionary methods
print("\n" + 20 * "=" + " Looping dictionary using the dictionary methods " + 20 * "=")

# Using The Keys Method
print("Using The Keys Method")
data_keys = alis_identity.keys()
print(data_keys)

for identity in alis_identity.keys():
    print(identity)


# Using The values Method
print("\nUsing The values Method")
data_values = alis_identity.values()

for identity in alis_identity.values():
    print(identity)


# Using The items Method
print("\nUsing The items Method")
data_items = alis_identity.items()

for key, value in alis_identity.items():
    print(f"{key} : {value}")


# Delete a dictonary key
print("\nDelete a dictonary key")

del alis_identity['University']
print(alis_identity)