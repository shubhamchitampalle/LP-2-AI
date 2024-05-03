def ask_question(question):
    print(question)
    answer = input("Enter your answer (yes/no): ").lower()
    while answer not in ['yes', 'no']:
        print("Please enter 'yes' or 'no'.")
        answer = input("Enter your answer (yes/no): ").lower()
    return answer == 'yes'

def diagnose():
    symptoms = {
        "fever": ask_question("Do you have a fever?"),
        "cough": ask_question("Do you have a cough?"),
        "sore throat": ask_question("Do you have a sore throat?"),
        "shortness of breath": ask_question("Do you have shortness of breath?"),
        "fatigue": ask_question("Do you feel fatigued?"),
        "body aches": ask_question("Do you have body aches?"),
        "runny nose": ask_question("Do you have a runny nose?"),
        "nausea": ask_question("Do you experience nausea?"),
        "vomiting": ask_question("Do you experience vomiting?"),
        "diarrhea": ask_question("Do you have diarrhea?"),
        "loss of taste or smell": ask_question("Have you lost your taste or smell?")
    }

    conditions = {
        "Common Cold": ["cough", "sore throat", "runny nose"],
        "Flu": ["fever", "cough", "body aches", "fatigue"],
        "COVID-19": ["fever", "cough", "shortness of breath", "loss of taste or smell"],
        "Stomach Flu": ["nausea", "vomiting", "diarrhea"]
    }

    possible_conditions = [condition for condition, symptoms_required in conditions.items() if all(symptoms[symptom] for symptom in symptoms_required)]

    if possible_conditions:
        print("Based on your symptoms, you may have one of the following conditions:")
        for condition in possible_conditions:
            print("- " + condition)
    else:
        print("Based on your symptoms, it's difficult to determine the diagnosis. Please consult a healthcare professional.")

if __name__ == "__main__":
    print("Welcome to the Advanced Medical Expert System!")
    print("Please answer the following questions to receive a diagnosis.")
    diagnose()


