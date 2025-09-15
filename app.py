import os
import csv
from flask import Flask, render_template, send_from_directory, request, jsonify
from gtts import gTTS
import hashlib
from config import HOST, PORT, DEBUG

app = Flask(__name__)
AUDIO_DIR = os.path.join("static", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

# Charger le lexique depuis le CSV
LEXIQUE_FILE = "lexique.csv"
entries = []

def load_lexique():
    """Charge le lexique depuis le fichier CSV"""
    global entries
    entries = []
    lex_file = "lexique_complet.csv" if os.path.exists("lexique_complet.csv") else LEXIQUE_FILE

    if os.path.exists(lex_file):
        with open(lex_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Créer des noms de fichiers uniques basés sur le contenu
                fr_hash = hashlib.md5(row["fr"].encode()).hexdigest()[:8]
                th_hash = hashlib.md5(row["th"].encode()).hexdigest()[:8]
                en_hash = hashlib.md5(row.get("en", "").encode()).hexdigest()[:8] if row.get("en") else ""
                de_hash = hashlib.md5(row.get("de", "").encode()).hexdigest()[:8] if row.get("de") else ""
                es_hash = hashlib.md5(row.get("es", "").encode()).hexdigest()[:8] if row.get("es") else ""
                it_hash = hashlib.md5(row.get("it", "").encode()).hexdigest()[:8] if row.get("it") else ""

                entry = {
                    "fr": row["fr"],
                    "th": row["th"],
                    "phon": row["phon"],
                    "fr_audio": f"fr_{fr_hash}.mp3",
                    "th_audio": f"th_{th_hash}.mp3",
                    "category": row.get("category", "other")
                }

                # Ajouter les langues supplémentaires si elles existent
                if "en" in row and row["en"]:
                    entry["en"] = row["en"]
                    entry["en_audio"] = f"en_{en_hash}.mp3"
                if "de" in row and row["de"]:
                    entry["de"] = row["de"]
                    entry["de_audio"] = f"de_{de_hash}.mp3"
                if "es" in row and row["es"]:
                    entry["es"] = row["es"]
                    entry["es_audio"] = f"es_{es_hash}.mp3"
                if "it" in row and row["it"]:
                    entry["it"] = row["it"]
                    entry["it_audio"] = f"it_{it_hash}.mp3"

                entries.append(entry)

def generate_audio(text, lang, filename):
    """Génère un fichier audio si il n'existe pas déjà"""
    filepath = os.path.join(AUDIO_DIR, filename)
    if not os.path.exists(filepath):
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(filepath)
            print(f"✅ Audio généré: {text} ({lang})")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la génération audio pour {text} ({lang}): {e}")
            return False
    return True

def ensure_audio_exists(entry):
    """S'assure que tous les audios d'une entrée existent"""
    # Générer l'audio français
    generate_audio(entry["fr"], "fr", entry["fr_audio"])

    # Générer l'audio thaï
    generate_audio(entry["th"], "th", entry["th_audio"])

    # Générer les audios pour les langues supplémentaires si elles existent
    if "en_audio" in entry and "en" in entry:
        generate_audio(entry["en"], "en", entry["en_audio"])
    if "de_audio" in entry and "de" in entry:
        generate_audio(entry["de"], "de", entry["de_audio"])
    if "es_audio" in entry and "es" in entry:
        generate_audio(entry["es"], "es", entry["es_audio"])
    if "it_audio" in entry and "it" in entry:
        generate_audio(entry["it"], "it", entry["it_audio"])

@app.route("/")
def index():
    """Page principale avec le lexique complet"""
    load_lexique()
    # Générer les audios pour les premières entrées seulement pour commencer
    for entry in entries[:20]:  # Commencer avec les 20 premiers mots
        ensure_audio_exists(entry)
    return render_template("index.html", entries=entries)

@app.route("/lecon/<int:start>/<int:end>")
def lecon(start, end):
    """Page de leçon avec une sélection de mots"""
    load_lexique()
    lecon_entries = entries[start:end] if start < len(entries) else entries[-end:]
    # Générer les audios pour cette leçon
    for entry in lecon_entries:
        ensure_audio_exists(entry)
    return render_template("lecon.html", entries=lecon_entries, start=start, end=min(end, len(entries)))

@app.route("/generate_audio", methods=["POST"])
def generate_audio_endpoint():
    """Endpoint pour régénérer les audios manuellement"""
    data = request.json
    text = data.get("text", "")
    lang = data.get("lang", "fr")

    if not text:
        return jsonify({"error": "Aucun texte fourni"}), 400

    # Créer un nom de fichier basé sur le hash du texte
    text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
    filename = f"{lang}_{text_hash}.mp3"

    success = generate_audio(text, lang, filename)
    if success:
        return jsonify({"filename": filename, "url": f"/static/audio/{filename}"})
    else:
        return jsonify({"error": "Erreur lors de la génération"}), 500

@app.route("/static/audio/<path:filename>")
def serve_audio(filename):
    """Sert les fichiers audio"""
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == "__main__":
    # Charger le lexique sans générer tous les audios au démarrage
    load_lexique()
    print(f"Chargement de {len(entries)} entrées du lexique...")

    # Démarrer immédiatement le serveur
    print(f"🚀 Démarrage du serveur sur {HOST}:{PORT}...")
    print("🎵 Les audios seront générés à la demande lors de la première visite")
    print("📱 Interface accessible sur : http://127.0.0.1:5001")
    app.run(debug=DEBUG, host=HOST, port=PORT)
