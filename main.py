# Tool by Shinra Custom By Insur not skid please.

import os
import re
from pystyle import Colorate, Colors
from pathlib import Path

def print_tool_banner():
    tool = """  
     ____                      _                 ____  ____  
    / ___|  ___  __ _ _ __ ___| |__   ___ _ __  |  _ \| __ ) 
    \___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__| | | | |  _ \ 
     ___) |  __/ (_| | | | (__| | | |  __/ |    | |_| | |_) |
    |____/ \___|\__,_|_|  \___|_| |_|\___|_|    |____/|____/ 

    """
    print(Colorate.Horizontal(Colors.red_to_blue, tool))

def grep(pattern, folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, start=1):
                        if re.search(pattern, line):
                            print(Colorate.Horizontal(Colors.blue_to_green, f"Résultat : {file_path}: ligne {line_number}: {line.strip()}"))
            except UnicodeDecodeError:
                print(Colorate.Horizontal(Colors.red_to_yellow, f"Erreur de décodage Unicode pour le fichier : {file_path}"))

def main():
    print_tool_banner()
    folder = "database"
    pattern = input(Colorate.Horizontal(Colors.green_to_yellow, "Entrez le motif à rechercher : "))
    grep(pattern, folder)

if __name__ == "__main__":
    main()
