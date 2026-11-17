"""
Import du jeu de données de démonstration (entièrement fictif) dans campus.db.

Le fichier data/seed_demo.sql contient des comptes, questions, consentements et
demandes RGPD inventés (domaine example.com). Mot de passe de démonstration des
comptes : voir le README (empreintes bcrypt ; la connexion réelle passe par
Keycloak, ces empreintes ne servent pas à se connecter).

Usage : python scripts/import_ensa_data.py
"""
import sqlite3
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DB_PATH = BASE / "data" / "campus.db"
SEED_PATH = BASE / "data" / "seed_demo.sql"

# S'assurer que les tables existent avant d'insérer
sys.path.insert(0, str(BASE / "backend"))
from database import init_db  # noqa: E402

init_db()

sql = SEED_PATH.read_text(encoding="utf-8")

with sqlite3.connect(DB_PATH) as conn:
    conn.executescript(sql)

# Vérification
cur = conn.cursor()
tables = ["users", "ensa_queries", "consent_records", "rgpd_requests", "audit_logs"]
print("Résultat de l'import :")
for t in tables:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        print(f"  {t:<20} {cur.fetchone()[0]} lignes")
    except sqlite3.OperationalError as e:
        print(f"  {t:<20} ERREUR : {e}")
conn.close()

print("\nImport terminé.")
