🎬 Mini-scénario – « Opération GhostByte »
Dans l’ombre d’un bureau encombré, un jeune développeur ingénieux met au point un système discret et multifonctionnel baptisé GhostByte. 
Son objectif ? Créer un ensemble d'outils capables de chiffrer des données sensibles, capturer des images, envoyer des fichiers à distance, et même… jouer à un Pac-Man maison. Voici comment il a orchestré cette mission :


🧠 1. Centralisation avec main.py
    C'est le chef d'orchestre. Ce fichier lance plusieurs scripts en parallèle :
        - Le bot Discord pour transmettre des fichiers.
        - Le module de chiffrement des fichiers.
        - Une capture d'image par webcam.
        - Un jeu Pac-Man comme couverture ludique.

📤 2. Surveillance et transmission – Bot_Discord.py
    Ce script agit comme un agent de liaison, envoyant :
        - Des messages sur un canal Discord via un webhook.
        - Des fichiers depuis un dossier ciblé (Documents/cible).
        - Il peut uploader tous les fichiers d’un répertoire, sauf ceux déjà chiffrés (.enc), pour une discrétion optimale.

📸 3. Espion silencieux – cam.py
    Ce module active la webcam de l'utilisateur, capture une image, et la transmet via Discord. La caméra est discrètement activée sans afficher d'interface visible.

🔐 4. Chiffrement – encryptage.py
    Il s'agit du gardien des données :
        - Génère une clé de chiffrement si elle n'existe pas.
        - Chiffre tous les fichiers du dossier ciblé à l’aide de Fernet.
        - Supprime les fichiers originaux après chiffrement.

🔓 5. Déchiffrement – decrypte.py
    Contrepartie du module précédent :
        - Charge la même clé.
        - Déchiffre tous les fichiers .enc dans le dossier ciblé.
        - Restaure les fichiers initiaux et efface les versions chiffrées.

👾 6. Détour ludique – pacman.py
    Un jeu Pac-Man personnalisé intégré pour la couverture (ou la détente ?) :
    Utilise Pygame pour afficher un labyrinthe, un Pac-Man et un fantôme.
    Gère les collisions, score, et permet de redémarrer une partie.