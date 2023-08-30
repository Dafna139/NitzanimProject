import DataAnalisys


# The function updates the results dict according to the new symptom
def update_possible_diseases(symptom_from_the_user):
    for disease in DataAnalisys.results_dict.keys():
        if symptom_from_the_user not in DataAnalisys.results_dict.get(disease):
            del DataAnalisys.results_dict[disease]
