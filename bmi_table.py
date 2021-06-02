from tabulate import tabulate
from test_data import data


# Function to  calculate bmi and add new columns to the data
def calculate_bmi(dat):
    for i in dat:
        bmi = i["WeightKg"] / (i["HeightCm"] / 100) ** 2
        if bmi <= 18.4:
            bmi_category = "Underweight"
            Health_risk = "Malnutrition risk"
        elif bmi <= 24.9:
            bmi_category = "Normal weight"
            Health_risk = "Low risk"
        elif bmi <= 29.9:
            bmi_category = "Overweight"
            Health_risk = "Enhanced risk"
        elif bmi <= 34.9:
            bmi_category = "Moderately obese"
            Health_risk = "Medium risk"
        elif bmi <= 39.9:
            bmi_category = "Severely obese"
            Health_risk = "High risk"
        else:
            bmi_category = "Very severely obese"
            Health_risk = "Very high risk"
        i["BMI"] = bmi
        i["BMICategory"] = bmi_category
        i["HealthRisk"] = Health_risk


def count_obese(dat):
    calculate_bmi(dat)
    count = 0
    for i in dat:
        if i['BMICategory'] == 'Overweight':
            count += 1
    return count


count_obese(data)
print(tabulate(data))
