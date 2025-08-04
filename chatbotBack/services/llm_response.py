from config import client

def generate_standard_response(user_input: str, history: list) -> str:
    history.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4.1",
            messages=history,
            temperature=0.7,
            max_tokens=400
        )
    except Exception as e:
        print("❌ GPT-4 indisponible :", str(e))
        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct:free",
            messages=history,
            temperature=0.7,
            max_tokens=400
        )
    bot_reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": bot_reply})
    return bot_reply
