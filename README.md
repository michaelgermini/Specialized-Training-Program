# 📚 Méthode Français-Thaï Moderne - Logiciel d'Apprentissage

[![CI](https://github.com/michaelgermini/Specialized-Training-Program/actions/workflows/ci.yml/badge.svg)](https://github.com/michaelgermini/Specialized-Training-Program/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3+-red.svg)](https://flask.palletsprojects.com/)

Un logiciel Python moderne pour apprendre le français-thaï avec génération automatique d'audios et interface web interactive.

## 🖼️ Aperçu

screenshots/home.png

*L'interface moderne et intuitive de Specialized-Training-Program*

## ✨ Fonctionnalités

- **🎵 Génération automatique d'audios** : Création d'audios pour le français, thaï, anglais et allemand
- **📖 Lexique structuré** : 321 mots/phrases organisés en 5 catégories thématiques
- **🌐 Interface web moderne** : Design responsive avec contrôles audio intégrés
- **📚 Mode leçon** : Apprentissage progressif avec exercices interactifs
- **🎯 Phonétique intégrée** : Transcription phonétique pour une prononciation parfaite
- **🔍 Recherche et filtrage** : Navigation facile dans le lexique

## 📂 Structure du Projet

```
blogiciel_francais_thai/
├── app.py                 # Application Flask principale
├── lexique_complet.csv    # Base de données complète (200+ entrées)
├── lexique.csv           # Version simplifiée
├── requirements.txt      # Dépendances Python
├── README.md            # Documentation
├── templates/
│   ├── index.html       # Page principale du lexique
│   └── lecon.html       # Template des leçons
└── static/
    └── audio/           # Fichiers audio générés
```

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancement de l'application

```bash
python app.py
```

L'application sera accessible à l'adresse : http://127.0.0.1:8080

#### Changer de port

Si le port 8080 est occupé, vous pouvez le changer facilement :

```bash
python change_port.py 3000  # Change vers le port 3000
```

## 📖 Utilisation

### Interface Principale

1. **Page d'accueil** : Affiche le lexique complet avec tous les mots/phrases
2. **Contrôles audio** : Boutons de lecture pour chaque langue
3. **Filtrage** : Sélection par catégorie (Noyau, Quotidien, Social, Travail, Spécial)
4. **Génération d'audios** : Bouton pour régénérer tous les fichiers audio

### Mode Leçon

- Accédez aux leçons via `/lecon/0/20` pour les 20 premiers mots
- Mode entraînement avec textes masqués
- Lecture séquentielle des audios

## 📊 Structure du Lexique

### 🟢 Noyau (0-50) - Base & Survie
- Salutations et politesse
- Nombres et pronoms
- Verbes essentiels
- Couleurs et formes

### 🔵 Quotidien (50-100) - Vie de Tous les Jours
- Alimentation et boissons
- Transport et déplacements
- Maison et logement
- Temps et horaires

### 🟣 Social (100-150) - Vie Sociale
- Famille et amis
- Émotions et sentiments
- Sorties et loisirs
- Technologies modernes

### 🟠 Travail & Études (150-180) - Vie Professionnelle
- Bureau et entreprise
- Éducation et apprentissage
- Métiers et professions

### 🔴 Situations Spéciales (180-200+) - Urgences et Culture
- Santé et urgences
- Voyage et tourisme
- Culture et religion
- Environnement

## 🎵 Génération d'Audios

Le logiciel utilise **gTTS (Google Text-to-Speech)** pour générer automatiquement les fichiers audio :

- **Français** : Voix française standard
- **Thaï** : Voix thaïlandaise native
- **Anglais** : Voix anglaise américaine
- **Allemand** : Voix allemande standard

Les fichiers sont stockés dans `static/audio/` avec des noms uniques basés sur le hash du contenu.

## 🔧 Personnalisation

### Ajouter de nouveaux mots

1. Éditez `lexique_complet.csv`
2. Format : `fr,en,de,th,phon,category`
3. Redémarrez l'application pour régénérer les audios

### Modifier les catégories

Les catégories disponibles :
- `noyau` : Base et survie
- `quotidien` : Vie quotidienne
- `social` : Relations sociales
- `travail` : Travail et études
- `special` : Situations spéciales

## 🌐 Déploiement

### Développement local

```bash
python app.py
```

### Production (avec Gunicorn)

```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:8080 app:app
```

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

## 📈 Statistiques

- **Total de mots/phrases** : 200+
- **Langues supportées** : Français, Anglais, Allemand, Thaï
- **Catégories** : 5 thèmes principaux
- **Couverture conversationnelle** : ~80% des situations quotidiennes
- **Temps de génération** : ~2-3 minutes pour tous les audios

## 🔍 Exemple d'utilisation

```python
# Accès au lexique complet
curl http://localhost:5000/

# Accès à une leçon spécifique (mots 20-40)
curl http://localhost:5000/lecon/20/40

# Génération d'un audio spécifique
curl -X POST http://localhost:5000/generate_audio \
  -H "Content-Type: application/json" \
  -d '{"text": "Bonjour", "lang": "fr"}'
```

## 🤝 Contribution

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Ajoutez vos modifications
4. Testez thoroughly
5. Soumettez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

Pour des questions ou des problèmes :
1. Vérifiez les logs de l'application
2. Consultez la section troubleshooting
3. Ouvrez une issue sur GitHub

## 🔄 Versions

- **v1.0.0** : Version initiale avec lexique de base
- **v1.1.0** : Ajout anglais et allemand
- **v1.2.0** : Extension à 200+ mots avec catégories

## 🤝 Contribuer

Nous accueillons les contributions ! Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les détails.

### Types de contributions
- 🆕 **Contenu** : Ajouter des mots/phrases au lexique
- 🛠️ **Code** : Améliorer les fonctionnalités techniques
- 📚 **Documentation** : Améliorer les guides et tutoriels
- 🐛 **Bugs** : Signaler et corriger les problèmes

### Comment contribuer
1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📊 Statistiques

- **⭐ Stars** : Nombre d'étoiles sur GitHub
- **🍴 Forks** : Nombre de forks
- **👥 Contributeurs** : Voir [CONTRIBUTORS.md](CONTRIBUTORS.md)
- **📦 Téléchargements** : Via PyPI (bientôt disponible)
- **🐛 Issues ouvertes** : [GitHub Issues](https://github.com/michaelgermini/Specialized-Training-Program/issues)

## 📞 Support

- 📧 **Email** : michael@germini.info
- 💬 **Issues** : [GitHub Issues](https://github.com/michaelgermini/Specialized-Training-Program/issues)
- 📖 **Wiki** : [Documentation](https://github.com/michaelgermini/Specialized-Training-Program/wiki)
- 💭 **Discussions** : [GitHub Discussions](https://github.com/michaelgermini/Specialized-Training-Program/discussions)

## 🙏 Remerciements

- **gTTS** : Pour la génération d'audios
- **Flask** : Pour le framework web
- **Communauté open source** : Pour les outils et bibliothèques
- **Contributeurs** : Pour leur temps et leur expertise

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**🎓 Bonne apprentissage du français-thaï !** 🇫🇷🇹🇭

⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile sur GitHub !
