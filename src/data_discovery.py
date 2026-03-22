import os
import glob

def analyze_dataset(label_path):
    stats = {'fire': 0, 'smoke': 0, 'total_boxes': 0}
    
    # Récupérer tous les fichiers .txt (format YOLO)
    label_files = glob.glob(os.path.join(label_path, "*.txt"))
    
    if not label_files:
        print("Aucun fichier de labels trouvé !")
        return

    for file in label_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if not data: continue
                
                cls = int(data[0])
                
                # Comptage des classes (selon config DFire : 0=fire, 1=smoke)
                if cls == 0: stats['fire'] += 1
                elif cls == 1: stats['smoke'] += 1
                stats['total_boxes'] += 1

    print(f"--- Rapport Flash ---")
    print(f"Images : {len(label_files)}")
    print(f"🔥 Flammes : {stats['fire']}")
    print(f"💨 Fumée : {stats['smoke']}")

# On l'utilisera plus tard sur Colab comme ça :
# analyze_dataset('chemin_vers_le_dataset_cloné')