# We copy paste the JSON format data into a JSON file for easy parsing.
# We import Python's JSON library for reading, writing, and parsing JSON into python.
# We import Python's panda library for manipulation and conversions of the data frame.
import json
import pandas


# we open the JSON file
with open("data.json", "r") as openfile:
    json_object = json.load(openfile)
    print(type(json_object))
# We print our imported JSON object for viewing and inspection in Python.
print(json_object)

# We create a data frame using the panda library's in-built read_json function.
df = pandas.read_json("data.json")
# We make the columns case insensitive for the future dictionary's key using Python's casefold function.
df["diagnosis"] = df["diagnosis"].str.casefold()
# We drop the 'id' column to maintain the key value structure for our future dictionary.
df = df.drop(["id"], axis=1)
print(df)

# We convert the dataframe into a dictionary object using Python's in-built zip function, and define the key-value pair.
symptoms_dict = dict(zip(df.diagnosis, df.symptoms))
print(symptoms_dict)

# We inspect the output of our dictionary's call function to ensure that it's a list.
print(symptoms_dict["flu"], type(symptoms_dict["flu"]))

# We define the get_symptoms_by_diagnosis function, and make it case insensitive using Python's casefold function.
def get_symptoms_by_diagnosis():
    user_diagnosis = input("What is your diagnosis? ")
    user_diagnosis = user_diagnosis.casefold()
    for key, value in symptoms_dict.items():
        if key == user_diagnosis:
            print(symptoms_dict[key])
            break
    else:
        print("Your diagnosis was not found")


# We call the get_symptoms_by_diagnosis, and input our text, and voila!
get_symptoms_by_diagnosis()
