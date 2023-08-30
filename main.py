import DataAnalisys


# The function updates the results dict according to the new symptom
def update_possible_diseases(symptom_from_the_user):
    for disease in DataAnalisys.results_dict.keys():
        if symptom_from_the_user not in DataAnalisys.results_dict.get(disease):
            del DataAnalisys.results_dict[disease]


# The function checks and returns if a symptom is related to a specific disease
def is_symptom_related_to_disease(symptom_from_the_user, disease):
    symptoms_of_disease = DataAnalisys.results_dict.get(disease)
    return symptom_from_the_user in symptoms_of_disease
