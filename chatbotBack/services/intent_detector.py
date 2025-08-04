from config import client

def detect_intent(question: str) -> str:
    prompt = f"""
Tu es un détecteur d’intention. Réponds uniquement par "OUI" ou "NON", sans autre texte.

Voici la consigne :
→ Si la question demande une information qui dépend du temps réel (heure, météo, date, événements récents, actualité),
OU qui pourrait nécessiter une recherche Web pour être correctement répondue,
alors réponds : OUI

Sinon, réponds : NON

Question : {question}
Réponse :
"""
    try:
        detection = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=5,
        )
        return detection.choices[0].message.content.strip().lower()
    except Exception as e:
        print("⚠️ Erreur détection intention:", str(e))
        return "non"
