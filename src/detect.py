from ultralytics import YOLO
import cv2

# Charger le modèle depuis le dossier models/
model = YOLO('models/yolo26n.pt')

# Lancer la détection sur ton image
# 'save=True' va créer un dossier avec l'image entourée de cadres
results = model.predict(source='tests_media/test.jpg', conf=0.25, save=True)

print("\n--- Détection terminée ! ---")
print(f"Va voir tes résultats dans : {results[0].save_dir}")