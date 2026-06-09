"""
SolarOps-Monitor: Agent IA pour maintenance prédictive solaire
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import datetime
import json

class SolarAgent:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.model_trained = False
        self.model_path = 'solar_model.pkl'

    def train_model(self, df):
        features = df[['tension', 'courant', 'temperature']]
        self.model.fit(features)
        joblib.dump(self.model, self.model_path)
        self.model_trained = True
        print(f"Modèle entraîné et sauvegardé dans {self.model_path}")

    def load_model(self):
        try:
            self.model = joblib.load(self.model_path)
            self.model_trained = True
            print(f"Modèle chargé depuis {self.model_path}")
        except FileNotFoundError:
            print("Aucun modèle trouvé. Lancez train_model() d'abord.")

    def predict_anomaly(self, df):
        if not self.model_trained:
            self.load_model()
        features = df[['tension', 'courant', 'temperature']]
        df['anomaly'] = self.model.predict(features)
        df['anomaly_label'] = df['anomaly'].map({1: 'Normal', -1: 'Anomalie'})
        return df

if __name__ == "__main__":
    agent = SolarAgent()
    data = pd.read_csv('exemple_donnees.csv')
    agent.train_model(data)
    resultats = agent.predict_anomaly(data)
    print(resultats)
