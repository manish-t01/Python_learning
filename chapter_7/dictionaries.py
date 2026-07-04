
print("")
print("----------------LEARNING DICTIONARIES----------------")

# 1st method of creating dictionary.
band = {
    "vocals": "Plant",
    # key   = #value
    "guitar": "Page"
}
print("")

# 2nd method.
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(type(band2))
print(len(band))
print(len(band2))
print("")

# Methods of accessing the items inside the dictonries.

# 1st method.
print(band["vocals"])

# 2nd method.
print(band.get("guitar"))
print("")

# list all keys.
print(band.keys())

# list all values.
print(band.values())
print("")

# list of key/values pairs as tuples.
print(band.items())

# varify a key exists or not.
print("guitar" in band)
print("Plant" in band)
print("Car" in band)
print("")

# Changing and Adding new values to the dictonery.

# -----changing values-----
band["vocals"] = "Coverdale"

# -----adding values-------
band.update({"bass": "JPJ"})
print(band)
print("")

# Removing items
print(band.pop("bass"))
print(band)
print("")

# -----adding values-------
band["drum"] = "Bonham"
print(band)
print("")

# NOTE: It removes the last added item in the dictonary. And print the removed intems in the form of tuple.
print(band.popitem())
print(band)
print('')

# Delete and Clear item.
band["drums"] = "bonham"  # adding item drums.
print(band)
del band["drums"]  # deleting item drums.
print(band)
print("")

band2.clear()  # it clear all the items from the band2.
print(band2)

del band2  # it fully delets the band2.
print("")

# Copy dictionaries.
band2 = band  # creates a reference and a proper copy.
print("BAD COPY!")
print(band2)
print(band)

band2["drums"] = "DumDum"
print(band)
print("")

band2 = band.copy()
band2["name"] = "Manish"
print("Good Copy!")
print(band)
print(band2)
print("")

# Another way of coping using dict() constructor function.
band3 = dict(band)
band3["bird"] = "ostrich"
print("Good Copy!")
print(band)
print(band3)
print("")

print("----------Nested Dictionaries-----------")

