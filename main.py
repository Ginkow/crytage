import subprocess
import threading
import time
# import sys

def run_script(script_name):
    print(f"💻 Lancement de {script_name}...")
    subprocess.run(["python", script_name])

if __name__ == "__main__":   
    subprocess.run(["python", "Bot_Discord.py"])
    
    scripts = ["encryptage.py", "cam.py", "pacman.py"]
    threads = [threading.Thread(target=run_script, args=(script,)) for script in scripts]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
