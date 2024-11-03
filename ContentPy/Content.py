"""prompt = "''"give me 5 multiple options based questions on indian general knowledge

Please format the results as a JSON object containing an array called "Questions". 
Each object within the array should have three keys: "Question", with the Question sentence, "Choices", which contains an array of four strings and "Answer", with the Answer.
Do not include any explanations, only provide a  RFC8259 compliant JSON response without deviation and all key value will be in double quotes"""

from g4f.client import Client
import json

def GetContent(prompt):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        # Add any other necessary parameters
    )
    cContent = response.choices[0].message.content.replace("```json", "").replace("```", "")
    print(cContent)
    JSONcontent = json.loads(cContent.replace("```json","").replace("```",""))
    return JSONcontent
