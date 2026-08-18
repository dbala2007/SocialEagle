# from transformers import pipeline

# chat = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")
# messages = [{"role":"user", "content":"Say Hello to a new student"}]
# out = chat(messages, max_new_tokens=40)
# print(out[0]["generated_text"][-1]["content"])

# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# total = sum(p.numel() for p in model.parameters())
# print(f"Model: {model_name}")
# print(f"Parameters: {total, } (~{total/1e6:.0f} millioin)")

from datasets import load_dataset

dataset = load_dataset("json", data_files="test_data.jsonl", split="train")
print(dataset)
print(dataset[0])