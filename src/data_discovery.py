import os
import glob
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

def professional_eda(base_path):
    print(f"--- Analyse Exploratoire Complète (Images + Labels) ---")
    print(f"Dossier ciblé : {base_path}\n")
    
    img_path = os.path.join(base_path, 'images')
    lbl_path = os.path.join(base_path, 'labels')
    
    stats = {'fire': 0, 'smoke': 0, 'total_boxes': 0, 'empty_files': 0, 'corrupt_images': 0}
    
    # 1. Vérification de l'intégrité des images
    print("🔍 Étape 1 : Vérification des images corrompues...")
    images = glob.glob(os.path.join(img_path, "*.*"))
    
    if not images:
        print("Erreur : Aucune image trouvée. Vérifie le chemin.")
        return

    # tqdm affiche une barre de progression dans le terminal
    for img_file in tqdm(images, desc="Scan des images", unit="img"):
        img = cv2.imread(img_file)
        if img is None:
            stats['corrupt_images'] += 1
            # On affiche le nom de l'image posant problème
            print(f"\n[ALERTE] Image corrompue détectée : {os.path.basename(img_file)}")
            # Optionnel : os.remove(img_file) pour la supprimer automatiquement

    # 2. Analyse des labels
    print("\n📊 Étape 2 : Analyse des annotations (Labels)...")
    label_files = glob.glob(os.path.join(lbl_path, "*.txt"))
    
    for file in tqdm(label_files, desc="Scan des labels", unit="fichier"):
        with open(file, 'r') as f:
            lines = f.readlines()
            if not lines:
                stats['empty_files'] += 1
                continue
                
            for line in lines:
                data = line.split()
                if not data: continue
                cls = int(data[0])
                if cls == 1: stats['fire'] += 1
                elif cls == 0: stats['smoke'] += 1
                stats['total_boxes'] += 1

    # 3. Affichage du rapport complet
    print(f"\n=== RAPPORT D'INTÉGRITÉ ===")
    print(f"Images analysées : {len(images)}")
    print(f"❌ Images corrompues : {stats['corrupt_images']}")
    print(f"📄 Labels vides (Background sans feu/fumée) : {stats['empty_files']}")
    print(f"🎯 Objets détectables : {stats['total_boxes']}")
    print(f"  🔥 Flammes (Classe 1) : {stats['fire']}")
    print(f"  💨 Fumée (Classe 0) : {stats['smoke']}")

    # 4. Génération de l'artefact visuel
    plt.style.use('ggplot')
    plt.figure(figsize=(8, 5))
    bars = plt.bar(['Fumée', 'Flammes'], [stats['smoke'], stats['fire']], color=['gray', 'orange'])
    plt.title('Distribution des classes dans D-Fire')
    plt.ylabel('Nombre d\'occurrences')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom')

    plt.savefig('class_distribution.png')
    print(f"\n✅ Graphique sauvegardé sous 'class_distribution.png'")

if __name__ == "__main__":
    # On pointe vers le dossier parent 'train' qui contient 'images' et 'labels'
    target_path = '../data/dfire/train'
    professional_eda(target_path)