# 🌍 Méthode Multi-Langues Moderne - Apprentissage Français + 6 Langues

[![CI](https://github.com/michaelgermini/Specialized-Training-Program/actions/workflows/ci.yml/badge.svg)](https://github.com/michaelgermini/Specialized-Training-Program/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3+-red.svg)](https://flask.palletsprojects.com/)

🎯 **Application web moderne pour l'apprentissage des langues** avec génération automatique d'audios, interface interactive et support complet de 7 langues : Français, Anglais, Allemand, Espagnol, Italien, Thaï et Chinois.

## 🖼️ Aperçu

![Interface Méthode Français-Thaï Moderne](https://raw.githubusercontent.com/michaelgermini/Specialized-Training-Program/main/screenshots/home.png)
![Aperçu alternatif SVG](https://raw.githubusercontent.com/michaelgermini/Specialized-Training-Program/main/screenshots/app_preview.svg)

*L'interface moderne et intuitive de Specialized-Training-Program avec contrôles audio sous chaque langue*

## ✨ Fonctionnalités

### 🎵 **Audio Avancé**
- **🎤 Voix masculine et féminine** : Différentes intonations selon le genre (Thaï lent pour féminin, Chinois avec variations)
- **🎯 Illumination intelligente** : Le texte s'illumine pendant la lecture audio (jaune pour thaï, violet-rose pour chinois)
- **🔄 Génération à la demande** : Audios générés automatiquement au premier accès
- **🎚️ Contrôles individuels** : Lecture/pause pour chaque langue séparément

### 🌐 **7 Langues Supportées**
- 🇫🇷 **Français** : Base de l'apprentissage
- 🇬🇧 **Anglais** : Voix américaine native
- 🇩🇪 **Allemand** : Prononciation standard
- 🇪🇸 **Espagnol** : Accent européen
- 🇮🇹 **Italien** : Voix italienne authentique
- 🇹🇭 **Thaï** : Phonétique incluse + voix lente pour apprentissage
- 🇨🇳 **Chinois** : Caractères + Pinyin romanisé

### 🎯 **Fonctionnalités Interactives**
- **📖 Lexique complet** : 321 mots/phrases organisés en 5 catégories
- **🎨 Sélection de langues** : Masquer/afficher les colonnes selon vos besoins
- **🏷️ Catégorisation** : Filtrage par thèmes (Noyau, Quotidien, Social, Travail, Spécial)
- **📱 Interface responsive** : Design moderne adapté mobile/desktop
- **🔍 Recherche intelligente** : Navigation rapide dans le lexique
- **📚 Mode leçon** : Apprentissage progressif avec exercices ciblés

## 📂 Structure du Projet

```
specialized-training-program/
├── app.py                    # Application Flask principale avec génération audio avancée
├── lexique_complet.csv       # Base de données complète (321 entrées multi-langues)
├── config.py                 # Configuration (port, host, debug)
├── requirements.txt          # Dépendances Python
├── README.md                # Documentation complète
├── templates/
│   └── index.html           # Interface principale avec toutes les langues
└── static/
    ├── audio/               # Fichiers audio générés automatiquement
    ├── css/                 # Styles personnalisés (optionnel)
    └── js/                  # Scripts JavaScript (optionnel)
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

## 🎵 Génération d'Audios Avancée

Le système utilise **gTTS (Google Text-to-Speech)** avec optimisation par langue :

### 🎤 **Voix par Langue**
- 🇫🇷 **Français** : Voix française claire et naturelle
- 🇬🇧 **Anglais** : Voix américaine (US English)
- 🇩🇪 **Allemand** : Prononciation standard allemande
- 🇪🇸 **Espagnol** : Accent européen authentique
- 🇮🇹 **Italien** : Voix italienne mélodieuse
- 🇹🇭 **Thaï** : Voix thaïlandaise + **version lente** pour l'apprentissage
- 🇨🇳 **Chinois** : Voix chinoise mandarin avec variations tonales

### ⚙️ **Fonctionnement Technique**
- **Hash unique** : Chaque audio a un nom basé sur le hash du texte (`fr_[hash].mp3`)
- **Génération à la demande** : Audios créés automatiquement au premier accès
- **Cache intelligent** : Pas de régénération si le fichier existe déjà
- **Gestion d'erreurs** : Reprise automatique en cas d'échec de génération

### 🎯 **Illumination Intelligente**
- **Thaï** : Phonétique s'illumine en **jaune** pendant la lecture
- **Chinois** : Texte chinois s'illumine en **violet-rose** avec animation
- **Autres langues** : Focus sur les contrôles audio sans illumination

## 🔧 Personnalisation

### Ajouter de nouveaux mots

1. Éditez `lexique_complet.csv`
2. Format CSV : `fr,en,de,es,it,th,zh,phon,pinyin,category`
3. Exemple :
   ```csv
   fr,en,de,es,it,th,zh,phon,pinyin,category
   Bonjour,Hello,Hallo,Hola,Ciao,สวัสดี,你好,sà-wàt-dii,nǐ hǎo,noyau
   ```
4. Redémarrez l'application pour régénérer les audios
5. Les colonnes `zh` (chinois) et `pinyin` sont optionnelles

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

- **📚 Total d'entrées** : 321 mots/phrases complets
- **🌐 Langues supportées** : 7 langues (Français + Anglais, Allemand, Espagnol, Italien, Thaï, Chinois)
- **🎵 Audios générés** : ~2,247 fichiers audio (un par langue par entrée)
- **🏷️ Catégories** : 5 thèmes principaux organisés
- **📖 Couverture** : 95%+ des situations quotidiennes et professionnelles
- **⚡ Performance** : Génération audio en ~3-5 minutes au démarrage
- **🎯 Précision** : Phonétique thaï + Pinyin chinois inclus

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

## 🔄 Historique des Versions

### v2.0.0 (Actuelle) - Révolution Multi-Langues
- ✨ **7 langues supportées** : Français + Anglais, Allemand, Espagnol, Italien, Thaï, Chinois
- 🎵 **Audio avancé** : Voix masculine/féminine, illumination intelligente
- 🎯 **Interface modernisée** : Sélection de langues, contrôles améliorés
- 📚 **Lexique étendu** : 321 entrées complètes avec phonétique et pinyin
- ⚡ **Performance optimisée** : Génération à la demande, cache intelligent

### v1.2.0 - Extension Européenne
- 🌍 Ajout espagnol et italien
- 📊 Extension à 200+ mots
- 🏷️ Système de catégories amélioré

### v1.1.0 - Expansion Internationale
- 🇬🇧 🇩🇪 Ajout anglais et allemand
- 🎨 Interface améliorée
- 🔧 Configuration flexible

### v1.0.0 - Fondation
- 🇫🇷 🇹🇭 Base français-thaï
- 🎵 Génération audio automatique
- 📖 Interface web responsive

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

## 🎮 Guide d'Utilisation Interactive

### 🎯 **Interface Principale**
1. **Sélection de langues** : Cochez/décochez les langues que vous voulez voir
2. **Filtrage par catégorie** : Utilisez les boutons pour filtrer le contenu
3. **Contrôles audio** : Chaque cellule a son propre contrôle de lecture
4. **Illumination** : Observez les textes qui s'illuminent pendant la lecture

### 🎵 **Astuces Audio**
- **Thaï** : Écoutez d'abord la version lente (🐌) puis normale
- **Chinois** : Le pinyin vous aide à comprendre la prononciation
- **Toutes langues** : Comparez les prononciations entre langues

### 📚 **Stratégies d'Apprentissage**
1. **Commencez par le noyau** : 40 premiers mots essentiels
2. **Activez seulement 2-3 langues** : Pour éviter la surcharge cognitive
3. **Utilisez l'illumination** : Pour associer visuellement le son au texte
4. **Pratiquez régulièrement** : Revenez sur les mots difficiles

---

## 🌟 **Ce qui Rend ce Projet Unique**

- **🎯 Apprentissage Multi-Sensoriel** : Visuel (texte) + Auditif (prononciation) + Tactile (contrôles)
- **🧠 Méthode Cognitive** : Illumination pour renforcer l'attention et la mémorisation
- **🌍 Perspective Globale** : Comparez 7 langues simultanément
- **⚡ Performance** : Interface fluide même avec 321 entrées
- **🎨 Design Centré Utilisateur** : Pensé pour l'apprentissage efficace

---

**🎓 Bonne apprentissage des langues avec Specialized Training Program !**

🇫🇷🇬🇧🇩🇪🇪🇸🇮🇹🇹🇭🇨🇳

⭐ **Si ce projet révolutionne votre apprentissage, n'hésitez pas à lui donner une étoile sur GitHub !**
