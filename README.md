# Accident Severity Prediction System

## Overview
This project is designed to help an insurance company detect potential discrepancies in injury claims following road accidents. The model predicts the severity of an injury—whether it's **slight**, **serious**, or **fatal**—based on various factors such as the time of the accident, weather conditions, driver details, and more. This predictive capability aids in preventing fraudulent claims, improving efficiency, and ensuring accurate claim processing.

## Business Problem
Imagine an insurance company that frequently receives claims from customers involved in road accidents. Some customers may exaggerate or misrepresent the severity of their injuries to receive higher compensation. By using this predictive model, the insurance company can assess the likelihood of an injury being slight, serious, or fatal based on the details provided.

When a claim is made, the company inputs relevant accident details into the model. If the prediction suggests that the injury is likely to be **slight**, but the customer claims a **severe injury**, this raises a red flag. The company can then conduct a more thorough investigation, examining medical reports, police records, or even reconstructing the accident scene.

This predictive system helps prevent fraudulent claims, saving the insurance company millions in potential payouts. Additionally, it ensures that genuine claims are processed more quickly and accurately, enhancing the company’s overall efficiency and profitability, while promoting fairness and transparency.

## Inputs
The following information is collected from the user and fed into the model:

- **Hour_of_Day**: The time of day when the accident occurred (e.g., Early Morning, Night).
- **Day_of_week**: The day of the week when the accident occurred (e.g., Monday, Friday).
- **Age_band_of_driver**: The age group of the driver involved (e.g., 18-30, Over 51).
- **Age_band_of_casualty**: The age group of the casualty involved (e.g., Under 18, 31-50).
- **Number_of_vehicles_involved**: The number of vehicles involved in the accident.
- **Number_of_casualties**: The number of casualties resulting from the accident.
- **Types_of_Junction**: The type of junction where the accident occurred (e.g., T Shape, Y Shape, No junction).
- **Area_accident_occured**: The area where the accident took place (e.g., Residential areas, Urban Areas).
- **Light_conditions**: The lighting conditions at the time of the accident (e.g., Daylight, Darkness - no lighting).
- **Weather_conditions**: The weather conditions at the time of the accident (e.g., Raining, Cloudy).

## Output
The model predicts the severity of the injury as one of the following classes:
- **Slight Injury**
- **Serious Injury**
- **Fatal Injury**

## Deployed system
https://road-accident-severity-predictor.onrender.com
