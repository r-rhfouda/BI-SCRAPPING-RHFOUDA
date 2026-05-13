from google_play_scraper import search, app, reviews, Sort
import json
import time
def extract_play_store_data():
    # 1. Définir notre recherche (Mental health & Wellness AI)
    query = "mental health wellness AI"
    print(f"Recherche en cours pour : '{query}'...")
    # On utilise la fonction 'search' pour trouver les applications correspondantes.
    # Pour ce lab, on limite à 5 résultats pour ne pas surcharger l'API et tester rapidement.
    search_results = search(query, lang='en', country='us', n_hits=5)
    all_extracted_data = []
    # 2. Explorer et extraire les données pour chaque application trouvée
    for result in search_results:
        app_id = result['appId']
        print(f"\nExtraction des données pour : {result['title']} ({app_id})")
        try:
            # A. Récupérer les détails complets de l'application (description, notes, développeur, etc.)
            app_details = app(app_id, lang='en', country='us')
            # B. Récupérer les avis des utilisateurs
            # On limite à 30 avis récents par application pour cet exercice.
            app_reviews, continuation_token = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=30
            )
            # C. Nettoyage des données d'avis
            # IMPORTANT : L'API renvoie des dates sous format 'datetime', qui ne sont pas
            # compatibles avec JSON. Nous devons les convertir en texte (chaînes de caractères).
            clean_reviews = []
            for r in app_reviews:
                clean_reviews.append({
                    "userName": r.get('userName'),
                    "score": r.get('score'),
                    "content": r.get('content'),
                    "date": r['at'].strftime("%Y-%m-%d %H:%M:%S") if r.get('at') else None
                })
            # D. Regrouper les métadonnées de l'app et ses avis
            app_data = {
                "app_metadata": app_details,
                "user_reviews": clean_reviews
            }
            all_extracted_data.append(app_data)
            # Pause polie d'une seconde entre chaque application pour ne pas être bloqué par Google
            time.sleep(1)
        except Exception as e:
            print(f"Erreur lors de l'extraction pour {app_id} : {e}")
    # 3. Sauvegarder les données dans un fichier JSON
    # Utilisez un chemin absolu si vous voulez être sûr de l'endroit où il s'enregistre !
    output_filename = 'mental_health_ai_apps.json'
    print("\nSauvegarde des données en cours...")
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(all_extracted_data, f, indent=4, ensure_ascii=False)
    print(f"✅ Terminé ! Les données ont été sauvegardées dans '{output_filename}'")
# Lancer la fonction
extract_play_store_data()
