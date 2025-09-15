#!/usr/bin/env python3
"""
Script de lancement pour le logiciel Français-Thaï Moderne
"""

import os
import sys
import subprocess

def check_requirements():
    """Vérifie si les dépendances sont installées"""
    try:
        import flask
        import gtts
        print("✅ Dépendances vérifiées")
        return True
    except ImportError as e:
        print(f"❌ Dépendance manquante : {e}")
        print("Installez les dépendances avec : pip install -r requirements.txt")
        return False

def check_files():
    """Vérifie si les fichiers nécessaires sont présents"""
    required_files = [
        "app.py",
        "lexique_complet.csv",
        "templates/index.html",
        "templates/lecon.html"
    ]

    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print("❌ Fichiers manquants :")
        for file in missing_files:
            print(f"  - {file}")
        return False

    print("✅ Tous les fichiers sont présents")
    return True

def create_directories():
    """Crée les dossiers nécessaires"""
    directories = ["static/audio"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✅ Dossiers créés")

def main():
    """Fonction principale"""
    print("🚀 Démarrage du logiciel Français-Thaï Moderne")
    print("=" * 50)

    # Vérifications
    if not check_requirements():
        sys.exit(1)

    if not check_files():
        sys.exit(1)

    create_directories()

    print("\n📚 Chargement du lexique...")
    print("🎵 Génération des audios (cette opération peut prendre quelques minutes)...")

    # Lancement de l'application
    try:
        print("\n🌐 Démarrage du serveur web...")
        print("📱 Interface accessible sur : http://127.0.0.1:8080")
        print("🛑 Appuyez sur Ctrl+C pour arrêter le serveur")
        print("-" * 50)

        # Lancement de Flask
        subprocess.run([sys.executable, "app.py"], check=True)

    except KeyboardInterrupt:
        print("\n\n👋 Arrêt du serveur demandé par l'utilisateur")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors du lancement : {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
