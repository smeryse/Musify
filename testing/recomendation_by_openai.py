import openai

from Musify.config import OPENAI_TOKEN

openai.api_key = OPENAI_TOKEN


def ask_openai(question):
    model_engine = "text-davinci-003"
    prompt = f'I liked the track {question}. Could you recommend something similar? Please send me the names of five tracks without numbering, each on a new line. The tracks should not repeat. Dont recommend something to me that doesnt exist'

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message


answer = ask_openai('Komarovo (DVRST Phonk Remix)')
print(answer)
