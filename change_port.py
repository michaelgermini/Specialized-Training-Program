#!/usr/bin/env python3
"""
Script pour changer facilement le port de l'application
"""

import re
import sys

def change_port(new_port):
    """Change le port dans le fichier de configuration"""

    # Vérifier que le port est valide
    try:
        port_num = int(new_port)
        if port_num < 1 or port_num > 65535:
            print("❌ Erreur : Le port doit être entre 1 et 65535")
            return False
    except ValueError:
        print("❌ Erreur : Le port doit être un nombre")
        return False

    # Modifier le fichier config.py
    try:
        with open("config.py", "r", encoding="utf-8") as f:
            content = f.read()

        # Remplacer la ligne PORT
        old_line = r'PORT = \d+'
        new_line = f'PORT = {new_port}'
        content = re.sub(old_line, new_line, content)

        with open("config.py", "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Port changé avec succès : {new_port}")
        print(f"📱 Nouvelle URL : http://127.0.0.1:{new_port}")
        return True

    except Exception as e:
        print(f"❌ Erreur lors du changement de port : {e}")
        return False

def main():
    """Fonction principale"""
    print("🔧 Changeur de port pour Français-Thaï Moderne")
    print("=" * 50)

    if len(sys.argv) != 2:
        print("Usage : python change_port.py <port>")
        print("Exemple : python change_port.py 8080")
        sys.exit(1)

    new_port = sys.argv[1]
    success = change_port(new_port)

    if success:
        print("\n💡 Pensez à redémarrer l'application pour appliquer le changement !")
        print("   python run.py")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
