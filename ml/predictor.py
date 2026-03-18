def predict_crop(data):
    """
    Simple rule-based crop prediction
    """
    temp = data['temperature']
    rainfall = data['rainfall']
    nitrogen = data['nitrogen']
    phosphorus = data['phosphorus']
    potassium = data['potassium']


    if rainfall > 120 and 20 <= temp <= 30:
        return "Maize"
    elif rainfall < 80 and temp >= 25:
        return "Sorghum"
    elif nitrogen < 50:
        return "Cassava"
    elif potassium > 60:
        return "Tomato"
    else:
        return "Beans"