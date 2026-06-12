from groq import Groq

client = Groq(
    api_key="your_groq_api_key_here"
)

def ask_ai(question):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are APEX, a smart AI assistant. "
                    "Give short answers in 2 to 4 sentences only."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {e}"