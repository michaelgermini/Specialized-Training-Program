# 🤝 Contribuer à Français-Thaï Moderne

Nous sommes ravis que vous souhaitiez contribuer à ce projet ! Voici comment vous pouvez nous aider.

## 🚀 Démarrage rapide

1. **Fork** le projet
2. **Clone** votre fork : `git clone https://github.com/michaelgermini/Specialized-Training-Program.git`
3. **Installez** les dépendances : `pip install -r requirements.txt`
4. **Testez** l'application : `python test_app.py`
5. **Lancez** l'application : `python run.py`

## 📝 Types de contributions

### 🆕 Ajouter du contenu
- **Nouveaux mots/phrases** : Ajoutez des entrées dans `lexique_complet.csv`
- **Nouvelles langues** : Support pour d'autres langues
- **Contenu éducatif** : Exercices, quiz, leçons

### 🛠️ Améliorations techniques
- **Performance** : Optimisation du chargement des audios
- **UI/UX** : Amélioration de l'interface utilisateur
- **Accessibilité** : Support pour les lecteurs d'écran
- **Mobile** : Responsive design

### 🐛 Corrections de bugs
- **Rapport de bugs** : Utilisez les Issues GitHub
- **Corrections** : Pull requests bienvenues

## 📋 Processus de contribution

### 1. Choisir une tâche
Consultez les [Issues](https://github.com/michaelgermini/Specialized-Training-Program/issues) pour voir les tâches disponibles.

### 2. Créer une branche
```bash
git checkout -b feature/ma-fonctionnalite
# ou
git checkout -b fix/mon-correctif
```

### 3. Faire vos changements
- Respectez le style de code existant
- Ajoutez des tests si nécessaire
- Mettez à jour la documentation

### 4. Tester vos changements
```bash
python test_app.py
python app.py  # Test manuel
```

### 5. Committer
```bash
git add .
git commit -m "feat: description de la fonctionnalité"
```

### 6. Push et Pull Request
```bash
git push origin feature/ma-fonctionnalite
```
Puis créez une Pull Request sur GitHub.

## 📊 Format des commits

Nous utilisons le format [Conventional Commits](https://conventionalcommits.org/) :

- `feat:` nouvelle fonctionnalité
- `fix:` correction de bug
- `docs:` changement de documentation
- `style:` formatage du code
- `refactor:` refactoring du code
- `test:` ajout/modification de tests
- `chore:` tâches de maintenance

Exemples :
- `feat: ajouter support pour le vietnamien`
- `fix: corriger génération audio pour les longues phrases`
- `docs: mettre à jour guide d'installation`

## 🎯 Standards de code

### Python
- Utilisez [PEP 8](https://pep8.org/) pour le style
- Ajoutez des docstrings aux fonctions
- Utilisez des noms descriptifs pour les variables

### HTML/CSS/JavaScript
- Indentation cohérente (2 espaces)
- Commentaires pour le code complexe
- Utilisez des classes CSS descriptives

### CSV (lexique)
Format : `fr,en,de,th,phon,category`

```csv
fr,en,de,th,phon,category
Bonjour,Hello,Hallo,สวัสดีครับ,sà-wàt-dii khráp,noyau
```

## 🧪 Tests

### Tests automatiques
```bash
python test_app.py  # Tests de base
```

### Tests manuels
1. Lancer l'application : `python run.py`
2. Tester toutes les fonctionnalités
3. Vérifier sur différents navigateurs
4. Tester sur mobile si possible

## 📖 Documentation

### Mise à jour du README
- Gardez les instructions à jour
- Ajoutez des captures d'écran si nécessaire
- Documentez les nouvelles fonctionnalités

### Commentaires dans le code
- Expliquez la logique complexe
- Documentez les paramètres des fonctions
- Ajoutez des TODO pour les améliorations futures

## 🔍 Revue de code

### Checklist pour les reviewers
- [ ] Code fonctionne-t-il correctement ?
- [ ] Tests passent-ils ?
- [ ] Documentation mise à jour ?
- [ ] Pas de régression ?
- [ ] Style de code respecté ?

### Checklist pour les contributeurs
- [ ] Description claire de la PR
- [ ] Tests ajoutés/modifiés si nécessaire
- [ ] Documentation mise à jour
- [ ] Changements testés manuellement

## 📞 Support

- **Issues GitHub** : Pour les bugs et demandes de fonctionnalités
- **Discussions GitHub** : Pour les questions générales
- **Documentation** : README et fichiers de documentation

## 🎉 Reconnaissance

Tous les contributeurs seront mentionnés dans :
- Le fichier CONTRIBUTORS.md
- Les releases notes
- La section "Contributors" du README

Merci de contribuer à Français-Thaï Moderne ! 🌟
