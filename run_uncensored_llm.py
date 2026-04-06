import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Modelo uncensored pequeño para hardware limitado
model_name = "jondurbin/airoboros-l2-1.3b"

print("Cargando modelo... Esto puede tomar tiempo en CPU.")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Usar float16 para ahorrar memoria
    device_map="auto"  # Automático: CPU o GPU si disponible
)

print("Modelo cargado. ¡Sin límites! Habla de lo que quieras.")

while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["exit", "salir"]:
        break

    inputs = tokenizer(user_input, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=inputs['input_ids'].shape[1] + 100,  # Generar hasta 100 tokens adicionales
        temperature=0.8,  # Creatividad
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"AI: {response}")