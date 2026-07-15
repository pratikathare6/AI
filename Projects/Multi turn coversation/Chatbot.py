import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(

    api_key= os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

conversation = [

    {
        "role" : "system",
        "content" : "you are a helpfull assistant"
    }
]

print("AI ChatBot Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodby..")
        break
    
    conversation.append(
        {
            "role" : "user",
            "content" : user_input
        }
    )
    try: 

        response = client.chat.completions.create(

            model = "openai/gpt-oss-120b",
            messages= conversation,
            max_tokens= 4000
        )

        ai_reply = response.choices[0].message.content

        conversation.append(
            {
                "role": "assistant",
                "content" : ai_reply 
            }
        )

        print("AI :",ai_reply)
        print('-'*50)

    except Exception as e:
        print("Error: ",e)