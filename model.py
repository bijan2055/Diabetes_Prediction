import joblib
def make_pred(input_Data):
    model = joblib.load('saved/DecisionTreeDiabetes.pkl')
    prediction = model.predict([input_Data])
    return prediction