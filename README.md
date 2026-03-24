# 🔥 FireVision : Système Intelligent de Détection d'Incendies

## 📖 Présentation du Projet
FireVision est un système de vision par ordinateur basé sur l'architecture **YOLO** (Ultralytics), conçu pour détecter les départs de feu et la fumée en temps réel. Entraîné sur le dataset D-Fire, ce modèle offre un excellent compromis entre vitesse d'inférence et précision, ce qui le rend idéal pour des systèmes d'alerte précoce.

---

## 🚀 Démonstration en Action

Voici ce dont le modèle est capable sur des données de test inédites. Les résultats ci-dessous ont été générés localement par le modèle final :

### 📸 Détection sur Images
*(Le modèle identifie avec précision les zones critiques et dessine des boîtes de délimitation (bounding boxes) avec un score de confiance).*

<div align="center">
  <img src="runs/detect/predict/forest.jpg" alt="Détection de feu" width="45%">
  <img src="runs/detect/predict/ftest.jpg" alt="Détection de fumée" width="45%">
</div>

### 🎥 Détection sur Vidéo en Temps Réel
*(Test d'inférence continue sur un flux vidéo)*

<video src="runs/detect/predict/vidfire.MP4" controls="controls" style="max-width: 100%;">
  Votre navigateur ne supporte pas la lecture de vidéos.
</video>

---

## 📊 Performances et Statistiques (Modèle Final)
Le modèle a été entraîné sur 50 époques avec les résultats suivants :
* **mAP50 (Global)** : 78.5%
* **Précision (Fumée)** : 83.9%
* **Vitesse d'inférence** : ~3.0ms par image (Testé sur GPU Tesla T4)
* **Poids du modèle** : ~19 Mo (`best.pt`)

---

## 🛠️ Architecture du Projet

Le projet respecte les standards de développement Python :
* `data/` : Scripts d'exploration de données (EDA) et graphiques de distribution.
* `models/` : Poids du modèle entraîné (`best.pt`).
* `notebooks/` : Le code source de l'entraînement sur le cloud.
* `runs/` : Résultats des prédictions et démonstrations visuelles générées par le modèle.
* `src/` : Scripts d'inférence propres et exécutables en local.
* `tests_media/` : Médias originaux utilisés pour la validation.

---

## 💻 Installation et Utilisation

**1. Cloner le dépôt**
```bash
git clone https://github.com/Sofiane-Meziane/FireVision.git
cd FireVision
```

**2. Installer les dépendances**
L'environnement nécessite Python 3.8+ et les bibliothèques suivantes :
```bash
pip install -r requirements.txt
```

**3. Lancer une prédiction**
Le modèle de 19 Mo est directement inclus dans le dépôt. Lancez l'analyse avec :
```bash
python src/detect.py
```
*Note : Les résultats générés (images ou vidéos annotées) seront automatiquement sauvegardés dans le dossier `runs/detect/predict/`.*

---

## 👨‍💻 À propos de l'Auteur
**Sofiane Meziane**
*Étudiant en Master 1 Intelligence Artificielle - Université de Béjaïa*

Ce projet a été développé dans le but de consolider mes compétences en Computer Vision et en conception de systèmes intelligents de bout en bout.
