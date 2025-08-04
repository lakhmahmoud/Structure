# config.py
from openai import OpenAI

# 🔐 Clés API
OPENROUTER_API_KEY = "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"
SERPER_API_KEY = "a588f7b17f85808224a326d61b758b35daa9efe1"

# 🔐 TalkJS
TALKJS_SECRET_KEY = "sk_test_SjnXvj2k6nDKQmpbwiQSipWZxDwElnyg"
TALKJS_APP_ID = "tlrnXVFP"
BOT_ID = "bot_456"
USER_ID = "user_123"
CONVERSATION_ID = f"{USER_ID}__{BOT_ID}"


# 📡 LLM client
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
