import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

models = openai.models.list()

for model in models.data:
    print(model.id)


# babbage-002
# text-embedding-ada-002
# text-embedding-3-large
# gpt-4o-mini-realtime-preview-2024-12-17
# gpt-3.5-turbo-instruct-0914
# chatgpt-4o-latest
# davinci-002
# gpt-3.5-turbo-1106
# gpt-3.5-turbo-instruct
# gpt-3.5-turbo
# gpt-4o-2024-11-20
# gpt-4o-2024-05-13
# gpt-3.5-turbo-16k-0613
# gpt-3.5-turbo-16k
# text-embedding-3-small
# gpt-4o
# gpt-4o-mini
# gpt-4o-mini-2024-07-18
# o1-mini
# gpt-3.5-turbo-0125