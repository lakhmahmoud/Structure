from flask import Blueprint, request, jsonify
from services.intent_detector import detect_intent
from services.web_search import perform_web_search
from services.reformulation import reformulate_answer
from services.llm_response import generate_standard_response
from services.talkjs_sender import send_to_talkjs

chat_blueprint = Blueprint("chat", __name__)

conversation_history = []

@chat_blueprint.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    print(f"\n🔹 Message utilisateur : {user_message}")
    intent = detect_intent(user_message)
    print(f"🧠 Intention : {intent}")

    if "oui" in intent:
        web_data = perform_web_search(user_message)
        bot_reply = reformulate_answer(user_message, web_data)
    else:
        bot_reply = generate_standard_response(user_message, conversation_history)

    print(f"🤖 Réponse finale : {bot_reply}")
    send_to_talkjs(bot_reply)
    return jsonify({"reply": bot_reply})
