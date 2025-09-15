#!/usr/bin/env python3
"""
Script de test rapide pour vérifier le fonctionnement de l'application
"""

import os
import sys

def test_imports():
    """Test des imports nécessaires"""
    try:
        import flask
        import gtts
        import csv
        import hashlib
        print("✅ Imports réussis")
        return True
    except ImportError as e:
        print(f"❌ Import échoué : {e}")
        return False

def test_files():
    """Test de la présence des fichiers essentiels"""
    required_files = [
        "app.py",
        "lexique_complet.csv",
        "templates/index.html",
        "templates/lecon.html",
        "config.py"
    ]

    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print(f"❌ Fichiers manquants : {missing}")
        return False

    print("✅ Tous les fichiers essentiels sont présents")
    return True

def test_csv_format():
    """Test du format du fichier CSV"""
    try:
        import csv
        with open("lexique_complet.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            first_row = next(reader)

            required_columns = ["fr", "th", "phon", "category"]
            for col in required_columns:
                if col not in first_row:
                    print(f"❌ Colonne manquante dans CSV : {col}")
                    return False

        print("✅ Format CSV valide")
        return True
    except Exception as e:
        print(f"❌ Erreur CSV : {e}")
        return False

def test_directories():
    """Test de la création des dossiers nécessaires"""
    directories = ["static/audio"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    print("✅ Dossiers créés")
    return True

def main():
    """Fonction principale de test"""
    print("🧪 Test du logiciel Français-Thaï Moderne")
    print("=" * 50)

    tests = [
        ("Imports", test_imports),
        ("Fichiers", test_files),
        ("Format CSV", test_csv_format),
        ("Dossiers", test_directories)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🔍 Test : {test_name}")
        if test_func():
            passed += 1
        else:
            print(f"❌ Test {test_name} échoué")

    print("\n" + "=" * 50)
    print(f"📊 Résultats : {passed}/{total} tests réussis")

    if passed == total:
        print("🎉 Tous les tests sont passés ! L'application est prête.")
        print("\n🚀 Pour lancer l'application :")
        print("   python run.py")
        print("   ou")
        print("   python app.py")
        print("\n📱 Interface accessible sur : http://127.0.0.1:8080")
        return True
    else:
        print("⚠️ Certains tests ont échoué. Vérifiez la configuration.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
