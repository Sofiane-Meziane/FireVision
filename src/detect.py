import os
from ultralytics import YOLO

print("--- FireVision : Système de Détection ---")

# 1. Charger le modèle
model_path = '../models/best.pt'
model = YOLO(model_path)

# 2. Définir le média à analyser (Image ou Vidéo)
media_path = 'tests_media/vidfire.mp4' 

# 3. Lancer la prédiction avec des paramètres optimisés
if os.path.exists(media_path):
    print(f"Analyse en cours sur : {media_path} ...")
    results = model.predict(
        source=media_path,
        conf=0.40,
        save=True,
        line_width=2,
        exist_ok=True             # Écrase le fichier précédent au lieu de créer predict2, predict3...
    )
    print(f"\nSuccès ! Résultat sauvegardé dans : {results[0].save_dir}")
else:
    print(f"Erreur : Le fichier {media_path} est introuvable.")