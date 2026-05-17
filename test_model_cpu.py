#!/usr/bin/env python
"""Test model loading - CPU only, no GPU available."""

import torch
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM

try:
    print("No GPU detected. Loading model for CPU inference...")
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    
    print(f"✓ Tokenizer: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, trust_remote_code=True)
    print(f"✓ Tokenizer loaded successfully")
    
    print(f"\nWARNING: No GPU available.")
    print("Loading Mistral-7B on CPU will be VERY SLOW but should work.")
    print("Model size: ~14GB unquantized - may run out of memory or be extremely slow.")
    print("Recommendation: Use a smaller model or a quantized version with `llama-cpp-python`.")
    
    print(f"\n✓ Attempting to load model for CPU...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        device_map="cpu",
        low_cpu_mem_usage=True,
    )
    print(f"✓ Model loaded successfully on CPU")
    
    # Quick inference test
    prompt = "¿Hola?"
    inputs = tokenizer(prompt, return_tensors="pt")
    print(f"\nGenerating response (this will be SLOW on CPU)...")
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=30,
            temperature=0.8,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"\n✓ Generated response:")
    print(f"Response: {response}")
    print("\n✅ Model can load and generate, but inference will be slow on CPU.")
    sys.exit(0)
    
except OutOfMemoryError as e:
    print(f"\n❌ OUT OF MEMORY: {e}")
    print("Mistral-7B is too large for CPU memory. Use a smaller model instead.")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
