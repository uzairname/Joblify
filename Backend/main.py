
import cohere
co = cohere.Client('uY0ZdCM1A165gyUg8RNIqc1kv7N5uj1uwAWOh7Cb')

response = co.embed(
  texts=[
    "abc"
  ]
)

print(response)

