# 🔒 Politique de Sécurité

## 🔍 Rapport de Vulnérabilités

Nous prenons la sécurité très au sérieux. Si vous découvrez une vulnérabilité de sécurité dans Français-Thaï Moderne, veuillez nous en informer de manière responsable.

### 🚨 Comment signaler une vulnérabilité

**Ne créez pas d'Issue publique** pour les vulnérabilités de sécurité.

Au lieu de cela :

1. **Envoyez un email** à : michael@germini.info
2. **Utilisez le formulaire** : [GitHub Security Advisories](https://github.com/michaelgermini/Specialized-Training-Program/security/advisories/new)

### 📝 Informations à inclure

Dans votre rapport, veuillez inclure :

- **Description détaillée** de la vulnérabilité
- **Étapes de reproduction** avec exemples de code
- **Impact potentiel** sur les utilisateurs
- **Environnement de test** (OS, version Python, etc.)
- **Suggestions de correction** si vous en avez

### ⏰ Délais de réponse

- **Accusé de réception** : Dans les 24 heures
- **Mise à jour régulière** : Au moins une fois par semaine
- **Correction** : Selon la criticité (de quelques jours à quelques semaines)

## 🛡️ Mesures de Sécurité

### 🔐 Données Utilisateur
- **Aucune collecte de données personnelles** : L'application fonctionne localement
- **Pas de base de données externe** : Toutes les données restent sur votre machine
- **Pas de tracking** : Aucun suivi d'utilisation

### 🌐 Sécurité Web
- **HTTPS recommandé** : Utilisez HTTPS en production
- **Headers de sécurité** : Configuration recommandée pour les déploiements
- **Dépendances sécurisées** : Mises à jour régulières des bibliothèques

### 📦 Sécurité des Dépendances
- **Audit régulier** : Vérification des vulnérabilités connues
- **Mises à jour** : Application rapide des correctifs de sécurité
- **Minimalisme** : Nombre réduit de dépendances externes

## 🔧 Configuration de Sécurité Recommandée

### Pour le Développement
```bash
# Utilisez un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installez uniquement les dépendances nécessaires
pip install -r requirements.txt
```

### Pour la Production
```python
# Dans config.py, ajustez pour la production
DEBUG = False
SECRET_KEY = "votre-cle-secrete-unique"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
```

### Configuration Nginx (recommandé)
```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    # Redirection HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name votre-domaine.com;

    # SSL configuration
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 🚨 Vulnérabilités Connues

### Aucune vulnérabilité connue actuellement

Nous maintenons une liste à jour des vulnérabilités connues et de leur statut de correction.

| Vulnérabilité | Découverte | Statut | Correction |
|---------------|------------|--------|-----------|
| Aucune | - | - | - |

## 📞 Contact

- **Sécurité** : michael@germini.info
- **Général** : michael@germini.info
- **GitHub** : [Security Advisories](https://github.com/michaelgermini/Specialized-Training-Program/security/advisories)

## 🙏 Reconnaissance

Nous remercions tous les chercheurs en sécurité qui nous aident à maintenir Français-Thaï Moderne sécurisé pour tous les utilisateurs.

---

**🔒 La sécurité est une responsabilité partagée. Merci de nous aider à maintenir ce projet sécurisé !**
