"""第1回: 素のLLMに会話形式で質問するスクリプト。

使い方:
    uv run python -m app.ask

ツールは使わず、会話履歴を保って続けて質問できる。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key


def main() -> None:
    print(f"[model] {MODEL}")
    try:
        client = genai.Client(api_key=get_api_key())
        chat = client.chats.create(model=MODEL)

        while True:
            question = input("質問 (終了は quit): ")
            if question in ("quit", "終了"):
                break

            response = chat.send_message(question)
            print(response.text)
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
