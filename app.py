from flask import Flask, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/')
def SCORING():
    #load data
    with open('./valeur_flask.pkl', 'rb') as features_data:
        data = pickle.load(features_data)
    #load model
    model = pickle.load(open('./logistic_model', 'rb'))
    # probabilite et prediction
    data['model_proba_client'] = model.predict_proba(data)[:, 1]
    data['model_prediction'] = np.where(data['model_proba_client'] > 0.52, 1, 0)
    data['model_decision_credit'] = np.where(data['model_prediction'] > 0, "Acceptation_credit", "Refus_credit")
    Donnees_API = data[['SK_ID_CURR','model_proba_client','model_prediction','model_decision_credit']].to_dict()
    return jsonify(Donnees_API)


