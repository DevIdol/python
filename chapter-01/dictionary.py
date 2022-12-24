#Dictionary (Key , Value)

students = {"roll-01": "Mg Mg", "roll-02": "Ko Ko"}

print("Dictionary:", students)#Dictionary: {'roll-01': 'Mg Mg', 'roll-02': 'Ko Ko'}

print("roll-01:", students.get("roll-01"))#roll-01: Mg Mg

students["roll-02"] = "Aung Aung"
print("Dictionary:", students)#Dictionary: {'roll-01': 'Mg Mg', 'roll-02': 'Aung Aung'}