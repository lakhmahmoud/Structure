from config import client
from datetime import datetime

def reformulate_answer(user_question: str, web_data: dict) -> str:
    if any(word in user_question.lower() for word in ["heure", "time", "what time", "date", "weather"]):
        now = datetime.now()
        heure = now.strftime("%H:%M")
        return f"Il est actuellement {heure} (heure locale)."

    if "organic" in web_data and len(web_data["organic"]) > 0:
        top = web_data["organic"][0]
        title = top.get("title", "")
        snippet = top.get("snippet", "")
        prompt = f"""
Tu es un assistant intelligent capable de générer une réponse claire, actuelle, fiable et pédagogique à partir d’une information issue d’une recherche web.

Voici les informations issues de cette recherche :
🔹 Titre : {title}
🔹 Résumé : {snippet}

Ta tâche est de répondre à la question suivante :
👉 {user_question}

### ✅ Consignes essentielles :
1. Reformule entièrement la réponse **avec tes propres mots** (pas de copier-coller).
2. Donne une réponse **structurée** : utilise des paragraphes clairs ou des puces si le sujet est complexe.
3. Adopte un **ton neutre, professionnel et accessible** à tous publics.
4. Si la réponse concerne une actualité, la météo, un événement, une statistique ou une date :
   ➤ Commence par : **“📅 En août 2025,”** ou par la date extraite si disponible.
5. **Ne complète pas avec des données anciennes** ou inventées non présentes dans le résumé.
6. Résume les **faits principaux**, puis ajoute les **conséquences, implications ou tendances** si elles sont présentes.
7. **N’inclus aucun lien, source ou citation externe** (ex. : pas de "selon ce site" ou "voir ce lien").

### 🎯 Objectif :
Fournir une réponse **exacte, à jour et bien formulée**, basée uniquement sur la recherche web ci-dessus, sans extrapolation.

"""


        try:
            reformulation = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=300
            )
            return reformulation.choices[0].message.content.strip()
        except Exception as e:
            print("❌ Erreur reformulation:", str(e))
            return snippet
    return "Je n’ai trouvé aucun résultat pertinent."