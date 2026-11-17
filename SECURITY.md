# Politique de sécurité

## Périmètre

Ce dépôt est un **projet académique** : un prototype d'assistant pédagogique IA local, sans
déploiement en production ni support garanti. Il est publié tel quel, sous licence MIT.

| Version | Suivie |
| --- | --- |
| `main` (dernier commit) | oui, au mieux |

Sont dans le périmètre :

- l'API FastAPI (`backend/`) : authentification Keycloak, sessions, rôles, rate limiting,
  filtrage anti-injection, anonymisation ;
- l'interface web (`frontend/`) et le script d'import (`scripts/`) ;
- toute donnée personnelle ou tout secret publié par erreur, y compris dans l'historique.

Hors périmètre : Keycloak, Ollama, le modèle Gemma et les autres dépendances (à signaler à leurs
mainteneurs), ainsi que les limites déjà décrites dans le [README](README.md#limites).

## Signaler une vulnérabilité

Ne pas ouvrir d'issue publique. Utiliser le signalement privé de GitHub : onglet **Security**,
puis **Report a vulnerability**. Indiquer le fichier ou le commit concerné, les étapes pour
reproduire et l'impact attendu. Ne pas joindre la valeur complète d'un secret : son emplacement
suffit.

Projet personnel : la réponse se fait au mieux, sans délai garanti.

## Rappels pour les utilisateurs

- Ne jamais committer de fichier `.env` ; seul `.env.example` (valeurs factices) est suivi.
- Changer `APP_SESSION_SECRET` avant tout usage réel.
- Les données de `data/seed_demo.sql` sont fictives ; ne jamais y placer de données réelles
  d'étudiants.
