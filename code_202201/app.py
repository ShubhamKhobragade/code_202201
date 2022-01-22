from jsonRead import readRawData
import json

def bmiCalculator():
    df = readRawData()
    df['BMI'] = round(df['WeightKg']/(df['HeightCm']/100)**2,2)
    
    df['BMI Category'] = ['Overweight' if 25 <= k <= 29.9 else 'Underweight' if k <= 18.4 else 'Normal weight' if 18.5 <= k <= 24.9 
        else 'Moderately obese' if 30<= k <=34.9 else 'Severely obese' if 35<= k <= 39.9 else 'Very severely obese' if 40 <= k else 'None' for k in df['BMI']]
    
    df['Health risk'] = ['Enhanced risk' if k == 'Overweight' else 'Malnutrition risk' if k == 'Underweight' else 'Low risk' if k == 'Normal weight' 
        else 'Medium risk' if k == 'Moderately obese' else 'High risk' if k == 'Severely obese' else 'Very high risk' if k == 'Very severely obese' else 'None' for k in df['BMI Category']]
    
    df.to_json('data.json',orient='records')
    return 'Executed'

def totalOverweightPerson():
    df = readRawData()
    print('Total number of Overweight people :-',df.loc[df['BMI Category'] == 'Overweight', 'BMI Category'].count())
    return 'Executed'