"""prompt = "''"give me 5 multiple options based questions on indian general knowledge

Please format the results as a JSON object containing an array called "Questions". 
Each object within the array should have three keys: "Question", with the Question sentence, "Choices", which contains an array of four strings and "Answer", with the Answer.
Do not include any explanations, only provide a  RFC8259 compliant JSON response without deviation and all key value will be in double quotes"""

"""
    prompt = (
        "''"You are a seasoned content writer for a YouTube Shorts channel, specializing in facts videos. 
        Your facts shorts are concise, each lasting less than 120 seconds (approximately 300 words). 
        They are incredibly engaging and original. When a user requests a specific type of facts short, you will create it.

        For instance, if the user asks for:
        Weird facts
        You would produce content like this:

        Weird facts you don't know:
        - Bananas are berries, but strawberries aren't.
        - A single cloud can weigh over a million pounds.
        - There's a species of jellyfish that is biologically immortal.
        - Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.
        - The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.
        - Octopuses have three hearts and blue blood.
        - more.
        - more.
        - more.
        - etc.

        You are now tasked with creating the best short script based on the user's requested type of 'facts'.

        Keep it brief, highly interesting, and unique.

        Stictly output the script in a JSON format like below, and only provide a parsable JSON object with the key 'script'.

        # Output
        {"script": "Here is the script ..."}
        "''"
    )"""


import os
#from openai import OpenAI
from g4f.client import Client
import json
os.environ['GROQ_API_KEY'] = "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"

os.environ["PEXELS_KEY"]="T4UGEah5t8vow0v9pgxe25V5DgqhOiWuOL7RuPZ4y5AnohCLC61NqaMg"

if len(os.environ.get("GROQ_API_KEY")) > 30:
    from groq import Groq
    model = "mixtral-8x7b-32768"
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
        )
else:
    OPENAI_API_KEY = os.getenv('OPENAI_KEY')
    model = "gpt-4"
    client = Client() #api_key=OPENAI_API_KEY)

def GetContent(prompt):

    response = client.chat.completions.create(
            model=model,
            messages=[
#                {"role": "system", "content": "Write story on prompt"},
                {"role": "user", "content": prompt}
            ]
        )
    content = response.choices[0].message.content
    try:
        script = json.loads(content)
    except Exception as e:
        json_start_index = content.find('{')
        json_end_index = content.rfind('}')
        print(content)
        content = content[json_start_index:json_end_index+1]
        script = json.loads(content)
    return script
