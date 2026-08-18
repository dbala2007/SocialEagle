from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-135M-Instruct")
text = "Fine-tuning is fun!"
tokens = tokenizer.encode(text)
print(f"Text: {text}")
print(f"Tokens: {tokens}")
print(f"Back to text: {tokenizer.decode(tokens)}")

messages = [
    {"role":"user","content":"What is the capital of France?"},
    {"role":"assistant","content":"The capital of France is Paris"}
]

formatted = tokenizer.apply_chat_template(messages, tokenize=False)
print(formatted)