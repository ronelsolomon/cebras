import os
from cerebras.cloud.sdk import Cerebras

client = Cerebras(
    # This is the default and can be omitted
    api_key="csk-y933tjkj4d4fct3jr2xny2yp9k8xkx4kh3rk2d6e59kywpk3"
    #os.environ.get("csk-y933tjkj4d4fct3jr2xny2yp9k8xkx4kh3rk2d6e59kywpk3")
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "What is a Rock"
        }
    ],
    model="llama-4-scout-17b-16e-instruct",
    stream=True,
    max_completion_tokens=2048,
    temperature=0.2,
    top_p=1
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")