import torch
from ultralytics import YOLO
import cv2

print(f"--- FireVision Setup Check ---")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA disponible (GPU): {torch.cuda.is_available()}")
print(f"OpenCV version: {cv2.__version__}")

# Tester le chargement du modèle SOTA
try:
    model = YOLO('yolo26n.pt') 
    print("Succès : Modèle YOLO26 chargé correctement !")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")