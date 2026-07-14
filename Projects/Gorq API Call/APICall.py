import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(

        api_key = os.getenv('GROQ_API_KEY'),
        base_url= 'https://api.groq.com/openai/v1'
)

try: 
        response = client.chat.completions.create(

                model = 'openai/gpt-oss-120b',
                messages = [
                    {
                        "role" : "user",
                        "content" : 'hello whats your name'
                    }
                ]
        )

        print(response.choices[0].message.content)

except Exception as e:
        print("Error -  ",e)