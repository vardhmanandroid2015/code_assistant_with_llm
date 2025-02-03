import ollama

response = ollama.list()

print(response)

# == Chat example ==
res = ollama.chat(
    model="qwen2.5-coder:1.5b",
    messages=[
        {"role": "user", "content": "What is Restful API web server?"},
    ],
)
print(res["message"]["content"])

# == Chat example streaming ==
res = ollama.chat(
    model="qwen2.5-coder:1.5b",
    messages=[
        {
            "role": "user",
            "content": "what is microservice? What are the methods of building microservices?",
        },
    ],
    stream=True,
)

for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)


# ==================================================================================
# ==== The Ollama Python library's API is designed around the Ollama REST API ====
# ==================================================================================

# == Generate example ==
# res = ollama.generate(
#     model="qwen2.5-coder:1.5b",
#     prompt="What is gRPC server? How to build microservice with gRPC in python",
# )

# show
# print(ollama.show("qwen2.5-coder:1.5b"))


# Create a new model with modelfile
# modelfile = """
# FROM qwen2.5-coder:1.5b
# SYSTEM You are coder, a very smart code assistant who helps to write software applications with efficiency.
# PARAMETER temperature 0.1
# """
#
# ollama.create(model="codeassistant", modelfile=modelfile)
#
# res = ollama.generate(model="codeassistant", prompt="what is microservice?")
# print(res["response"])
#
#
# # delete model
# ollama.delete("codeassistant")