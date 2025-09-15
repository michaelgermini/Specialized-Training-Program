#!/usr/bin/env python3
"""Test de connectivité du serveur"""

import time
import urllib.request
import sys

def test_connection(port=5001, max_attempts=3):
    """Test la connectivité du serveur"""
    url = f"http://127.0.0.1:{port}/"

    for attempt in range(max_attempts):
        try:
            print(f"🔍 Tentative {attempt + 1}/{max_attempts} - Test de {url}")
            response = urllib.request.urlopen(url, timeout=5)
            print(f"✅ Serveur accessible sur le port {port} - Status: {response.status}")
            return True
        except Exception as e:
            print(f"❌ Tentative {attempt + 1} échouée: {str(e)}")
            if attempt < max_attempts - 1:
                print("⏳ Nouvelle tentative dans 2 secondes...")
                time.sleep(2)

    return False

if __name__ == "__main__":
    print("🧪 Test de connectivité du serveur Français-Thaï Moderne")
    print("=" * 60)

    # Attendre que le serveur démarre
    print("⏳ Attente du démarrage du serveur...")
    time.sleep(3)

    # Tester différents ports
    ports_to_test = [5001, 8080, 3000, 5000]

    for port in ports_to_test:
        if test_connection(port):
            print(f"\n🎉 Serveur trouvé sur le port {port} !")
            print(f"🌐 Accédez à l'application : http://127.0.0.1:{port}")
            sys.exit(0)

    print("\n❌ Aucun serveur trouvé sur les ports testés")
    print("💡 Essayez de lancer l'application avec : python run.py")
    sys.exit(1)
