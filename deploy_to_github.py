#!/usr/bin/env python3
"""
Script de déploiement automatique vers GitHub
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔧 {description}")
    print(f"📝 Commande: {command}")

    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(f"✅ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur: {e}")
        if e.stdout:
            print(f"📄 Sortie: {e.stdout}")
        if e.stderr:
            print(f"⚠️ Erreur détaillée: {e.stderr}")
        return False

def main():
    """Fonction principale de déploiement"""
    print("🚀 Déploiement vers GitHub - Specialized-Training-Program")
    print("=" * 60)

    # Vérifications préalables
    if not os.path.exists('.git'):
        print("❌ Aucun dépôt Git trouvé. Initialisez d'abord le dépôt avec 'git init'")
        return False

    # Vérifier les fichiers importants
    required_files = ['README.md', 'app.py', 'lexique_complet.csv']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Fichier manquant: {file}")
            return False

    print("✅ Fichiers requis présents")

    # Étapes de déploiement
    steps = [
        ("git add .", "Ajout de tous les fichiers"),
        ("git status", "Vérification du statut"),
        ('git commit -m "🚀 Initial commit: Specialized-Training-Program v1.2.0\\n\\n✨ Fonctionnalités principales:\\n- Application web Flask avec génération d\'audios\\n- Lexique multilingue (FR, EN, DE, TH) - 321 entrées\\n- Interface moderne et responsive\\n- Mode leçon interactif\\n- Génération d\'audios à la demande\\n\\n🛠️ Infrastructure:\\n- CI/CD avec GitHub Actions\\n- Tests automatiques\\n- Documentation complète\\n- Templates d\'issues\\n- Configuration PyPI prête\\n\\n📚 Contenu éducatif:\\n- 5 catégories thématiques\\n- Phonétique intégrée\\n- Support multilingue complet"', "Commit des changements"),
        ("git branch -M main", "Renommage de la branche en main"),
        ("git remote add origin https://github.com/michaelgermini/Specialized-Training-Program.git", "Ajout du remote GitHub"),
        ("git push -u origin main", "Push vers GitHub"),
    ]

    for command, description in steps:
        if not run_command(command, description):
            print(f"\n❌ Échec lors de l'étape: {description}")
            return False

    print("\n" + "=" * 60)
    print("🎉 Déploiement réussi !")
    print("\n📍 Votre projet est maintenant disponible sur :")
    print("🌐 https://github.com/michaelgermini/Specialized-Training-Program")
    print("\n📖 Documentation principale :")
    print("📄 https://github.com/michaelgermini/Specialized-Training-Program#readme")
    print("\n🔧 Prochaines étapes recommandées :")
    print("1. 📋 Activez les Issues dans les paramètres du dépôt")
    print("2. 💬 Activez les Discussions si souhaité")
    print("3. 📊 Configurez les branches protégées")
    print("4. 🏷️ Ajoutez des topics pertinents (education, thai, french, etc.)")
    print("5. 📝 Créez un premier release")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
