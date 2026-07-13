from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("⏳ Loading model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chat(prompt):
    messages = [{"role": "user", "content": prompt}]
    
    # ✅ FIX: Make sure output is a dictionary
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt",
        tokenize=True,
        return_dict=True  # IMPORTANT FIX
    ).to(model.device)

    # ✅ FIX: Call generate with specific arguments
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=200
    )

    reply = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return reply

# Simple loop
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("ThankYou!")
        break
    print("Bot:", chat(user))
