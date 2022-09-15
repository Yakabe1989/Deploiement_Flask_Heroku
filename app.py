from flask import Flask, jsonify
import pickle


app = Flask(__name__)
@app.route('/')
def SCORING():
    #load data
    with open('./FLASK_P7.pkl', 'rb') as features_data:
        data = pickle.load(features_data)
    Donnees_API = data.to_dict()
    return jsonify(Donnees_API)

if __name__ == "__main__":
        app.run()