# Rule-Based Expert System
# Syntecxhub AI Internship - Week 1

def expert_system():
    print("🩺 Welcome to the Medical Expert System")
    print("Enter symptoms separated by commas")
    
    user_input = input("Symptoms: ").lower()
    facts = set(symptom.strip() for symptom in user_input.split(","))

    rules = [
        ({"fever", "cough"}, "flu"),
        ({"fever", "headache"}, "viral infection"),
        ({"cough", "cold"}, "common cold"),
        ({"stomach pain", "vomiting"}, "food poisoning")
    ]

    conclusions = set()
    reasoning = []

    for condition, result in rules:
        if condition.issubset(facts):
            conclusions.add(result)
            reasoning.append(f"{','.join(condition).title()} were detected\nThese symptoms match the {result} rule")

    print("\n🔍 Reasoning Process:")
    if reasoning:
        for step in reasoning:
            print(step)
    else:
        print("No matching rules found.")

    print("\n🧠 Conclusion:")
    if conclusions:
        for c in conclusions:
            print(f"You may have: {c}")
    else:
        print("Unable to determine condition.")

expert_system()
