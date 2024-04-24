import json

def get_person_data():
    #opens the data base and returns a dictionary of the person data
    # Opening JSON file
    file = open("data/person_db.json")
    # Loading the JSON File in a dictionary
    person_data = json.load(file)
    return person_data

#jetzt überflüssig, da wir neue Liste für Names haben
#def get_names(person_data):
    #returns a list of names of the people in the data base

# Funktion für Liste, dass die Namen zurückgegeben werden
def get_person_list(person_data):
    #Liste für die Namen
    names = []
    #Für jeden Eintrag in der Datenbank
    for eintrag in person_data:
        #Namen in der Liste speichern
        names.append(eintrag['lastname'] + ', ' + eintrag['firstname'])
    return names

#Testen der Funktionen
if __name__ == "__main__":
    #Variablen für die Funktionen
    person_data = get_person_data()
    print(person_data)
    names = get_person_list(person_data)

    print(names)