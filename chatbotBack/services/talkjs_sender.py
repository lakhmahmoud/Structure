import requests
from config import TALKJS_SECRET_KEY, TALKJS_APP_ID, USER_ID, BOT_ID, CONVERSATION_ID

def send_to_talkjs(bot_reply: str):
    headers = {
        "Authorization": f"Bearer {TALKJS_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    # Utilisateurs
    requests.put(f"https://api.talkjs.com/v1/{TALKJS_APP_ID}/users/{USER_ID}", headers=headers, json={
        "id": USER_ID, "name": "Utilisateur", "email": "user@example.com", "role": "default"
    })
    requests.put(f"https://api.talkjs.com/v1/{TALKJS_APP_ID}/users/{BOT_ID}", headers=headers, json={
        "id": BOT_ID, "name": "Chatbot IA", "email": "bot@example.com", "role": "default"
    })

    # Conversation
    conv_url = f"https://api.talkjs.com/v1/{TALKJS_APP_ID}/conversations/{CONVERSATION_ID}"
    requests.put(conv_url, headers=headers, json={
        "participants": [USER_ID, BOT_ID],
        "subject": "Chat IA"
    })

    # Message
    payload = [{
        "text": bot_reply,
        "sender": BOT_ID,
        "type": "UserMessage"
    }]
    r = requests.post(f"{conv_url}/messages", headers=headers, json=payload)
    print(f"📤 TalkJS Status: {r.status_code} | {r.text}")
