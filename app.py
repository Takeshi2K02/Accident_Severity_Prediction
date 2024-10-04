from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

day_of_week_mapping = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

Age_band_of_driver_mapping = {
    'Under 18': 1,
    '18-30': 2,
    '31-50': 3,
    'Over 51': 4,
    'Unknown': 0
}

Types_of_Junction_mapping = {
    'Y Shape':0.396395,
    'No junction':0.337366,
    'Crossing':0.189997,
    'Other':0.039298,
    'Unknown':0.016401,
    'O Shape':0.014615,
    'T Shape':0.004872,
    'X Shape':0.001056
}

Age_band_of_casualty_mapping = {
    'Under 18': '0',
    '18-30': '1',
    '31-50': '2',
    'Over 51': '3'
}

hour_of_day_mapping = {
    'Early Morning': 0,
    'Morning Rush': 1,
    'Midday': 2,
    'Afternoon Rush': 3,
    'Evening': 4,
    'Night': 5
}

def prediction(list):
    filename = 'model/accident_severity.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        predicted_value = model.predict(np.array([list]))[0]
        # Mapping numeric predictions to text
        severity_mapping = {
            0: 'Slight Injury',
            1: 'Serious Injury',
            2: 'Fatal Injury'
        }
        
        return severity_mapping.get(predicted_value)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/predictor', methods=['POST', 'GET'])
def index():
    pred = ''
    form_data = {}
    if request.method == 'POST':
        # to get all the values related to a prediction
        form_data = {
            'Day_of_week': request.form['Day_of_week'],
            'Age_band_of_driver': request.form['Age_band_of_driver'],
            'Types_of_Junction': request.form['Types_of_Junction'],
            'Number_of_vehicles_involved': request.form['Number_of_vehicles_involved'],
            'Number_of_casualties': request.form['Number_of_casualties'],
            'Age_band_of_casualty': request.form['Age_band_of_casualty'],
            'Hour_of_Day': request.form['Hour_of_Day'],
            'Light_conditions': request.form['Light_conditions'],
            'Weather_conditions': request.form['Weather_conditions'],
            'Area_accident_occured': request.form['Area_accident_occured'],            
        }
        
        # get the form data before passing to the model
        Day_of_week = request.form['Day_of_week']
        Age_band_of_driver = request.form['Age_band_of_driver']
        Types_of_Junction = request.form['Types_of_Junction']
        Number_of_vehicles_involved = request.form['Number_of_vehicles_involved']
        Number_of_casualties = request.form['Number_of_casualties']
        Age_band_of_casualty = request.form['Age_band_of_casualty']
        Hour_of_Day = request.form['Hour_of_Day']
        Light_conditions = request.form['Light_conditions']
        Weather_conditions = request.form['Weather_conditions']
        Area_accident_occured = request.form['Area_accident_occured']

        # pass values after label encoding and frequency encoding
        feature_list=[]
        feature_list.append(day_of_week_mapping[Day_of_week])
        feature_list.append(Age_band_of_driver_mapping[Age_band_of_driver])
        feature_list.append(Types_of_Junction_mapping[Types_of_Junction])
        feature_list.append(int(Number_of_vehicles_involved))
        feature_list.append(int(Number_of_casualties))
        feature_list.append(Age_band_of_casualty_mapping[Age_band_of_casualty])
        feature_list.append(hour_of_day_mapping[Hour_of_Day])
        
        # pass values after One-Hot encoding
        Light_conditions_list = ['Darkness - lights lit', 'Darkness - lights unlit', 'Darkness - no lighting', 'Daylight']
        Weather_conditions_list = ['Cloudy Conditions', 'Fog or mist', 'Normal Weather', 'Other', 'Precipitation', 'Windy Conditions']
        Area_accident_occured_list = ['Church areas', 'Office areas', 'Other', 'Residential areas', 'Rural Areas', 'Urban Areas']

        def traverse(list, values):
            for item in list:
                if item == values:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse(Light_conditions_list, Light_conditions)
        traverse(Weather_conditions_list, Weather_conditions)
        traverse(Area_accident_occured_list, Area_accident_occured)

        pred = prediction(feature_list)
      
        print(pred)

    return render_template("predictor.html", pred = pred, form_data=form_data)

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000, debug=True)