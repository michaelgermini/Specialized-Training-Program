"""
Configuration du logiciel Français-Thaï Moderne
"""

import os

# Configuration de base
APP_NAME = "Méthode Français-Thaï Moderne"
VERSION = "1.2.0"

# Configuration Flask
DEBUG = True
HOST = "0.0.0.0"
PORT = 5001

# Chemins des fichiers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEXIQUE_FILE = "lexique_complet.csv"
BACKUP_LEXIQUE_FILE = "lexique.csv"
AUDIO_DIR = os.path.join(BASE_DIR, "static", "audio")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Configuration TTS (Text-to-Speech)
TTS_CONFIG = {
    "fr": {
        "lang": "fr",
        "slow": False,
        "description": "Français"
    },
    "en": {
        "lang": "en",
        "slow": False,
        "description": "English"
    },
    "de": {
        "lang": "de",
        "slow": False,
        "description": "Deutsch"
    },
    "th": {
        "lang": "th",
        "slow": False,
        "description": "ไทย"
    }
}

# Configuration des leçons
LESSON_SIZE = 20  # Nombre de mots par leçon
CATEGORIES = {
    "noyau": {
        "name": "🔹 Noyau (Base & Survie)",
        "description": "Mots essentiels pour la survie et la communication de base"
    },
    "quotidien": {
        "name": "🔵 Quotidien",
        "description": "Vie de tous les jours : nourriture, transport, logement"
    },
    "social": {
        "name": "🟣 Vie Sociale",
        "description": "Famille, amis, émotions, sorties, technologies"
    },
    "travail": {
        "name": "🟠 Travail & Études",
        "description": "Bureau, école, professions, apprentissage"
    },
    "special": {
        "name": "🔴 Situations Spéciales",
        "description": "Urgences, voyage, culture, religion"
    }
}

# Configuration audio
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = {
    "slow": False,  # Vitesse normale
    "tld": None     # Domain par défaut
}

# Statistiques du lexique
LEXIQUE_STATS = {
    "total_entries": 200,
    "categories_count": len(CATEGORIES),
    "languages": ["fr", "en", "de", "th"],
    "conversation_coverage": 80  # Pourcentage
}

# Configuration de l'interface web
WEB_CONFIG = {
    "theme": "modern",
    "responsive": True,
    "audio_preload": False,
    "show_phonetic": True,
    "enable_filtering": True,
    "enable_search": True
}

# Messages d'interface
MESSAGES = {
    "loading": "Génération des audios en cours...",
    "generation_complete": "Tous les audios ont été générés !",
    "no_audio_found": "Aucun audio trouvé pour cette langue.",
    "playback_complete": "Lecture terminée !",
    "server_started": "Serveur démarré avec succès",
    "lexique_loaded": "Lexique chargé : {count} entrées"
}

# Configuration de débogage
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "app.log"
}
