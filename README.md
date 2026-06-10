# Moniteur SolarOps

Agent IA avec Splunk pour la maintenance prédictive des installations solaires au Bénin. Projet Hackathon Splunk DeltaSTEMHorizon Hacks VI.

## 1. Problème
Au Bénin, 80% des pannes solaires sont détectées trop tard : poussière, ombrage, onduleur HS. Le client perd de l'argent sans le savoir car il n'a pas de monitoring.

## 2. Solution : Comment ça fonctionne
`Moniteur SolarOps` surveille ton installation 24h/24 et prédit les pannes avant qu'elles arrivent.

**Étape 1 : Collecte**
L'agent récupère les données en temps réel via Splunk : 
1.  Production kW de l'onduleur
2.  Irradiation, température, poussière 
3.  Consommation maison

**Étape 2 : Analyse IA**
1.  `Agent Performance` : Compare Prod Réelle vs Prod Théorique. Si écart >15% = Anomalie détectée.
2.  `Agent Diagnostic` : Identifie la panne : Poussière, Ombrage, Onduleur HS, Vol de panneau.
3.  `Agent Prédictif` : Modèle ML qui prédit une panne 7 jours à l'avance.

**Étape 3 : Alertes**
1.  `Dashboard Streamlit` : Vue temps réel : kW produits, santé système %, économies du jour.
2.  `Notifications` : Alerte WhatsApp/SMS : "Alerte: Perte 22% sur String 3. Nettoyage recommandé."
3.  `Rapport Auto` : Gemini génère un rapport PDF hebdo avec les actions à faire.

## 3. Stack Technique
-   **Frontend** : Streamlit
-   **IA/ML** : Python, Scikit-learn, Google Gemini API
-   **Data** : API Splunk pour météo et logs
-   **Backend** : FastAPI, Pandas, InfluxDB
-   **Déploiement** : Streamlit Community Cloud

## 4. Installation Locale
```bash
cd moniteur-solarops
pip install -r requirements.txt
streamlit run app.py
