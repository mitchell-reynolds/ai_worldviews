import os
import openai
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

def testing():
    openai.api_key = os.environ.get("hackathon_gpt4_key")
    print(openai.api_key)

    response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
    print(response)

if __name__ == '__main__':

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    testing()