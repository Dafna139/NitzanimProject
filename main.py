# import
results_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
def update_possible_diseases(symptom_from_the_user):
    for disease in results_dict.keys():
        if symptom_from_the_user not in results_dict.get(disease):
            del results_dict[disease]

