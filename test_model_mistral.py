#!/usr/bin/env python
"""Quick test to verify Mistral-7B can load on this hardware with 4-bit quantization."""

import torch
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

try:
    print("Testing Mistral-7B-Instruct-v0.1 loading...")
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    
    print(f"✓ Tokenizer: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, trust_remote_code=True)
    print(f"✓ Tokenizer loaded successfully")
    
    print(f"✓ Model: {model_name} with 4-bit quantization")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_fp32_cpu_offload=True,  # Enable CPU offloading for 4-bit
    )
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto",
        low_cpu_mem_usage=True,
        max_memory={
            0: "2GB",  # GPU
            "cpu": "8GB"  # CPU offload
        },
    )
    print(f"✓ Model loaded successfully with 4-bit quantization")
    
    # Quick inference test
    prompt = "¿Hola, cómo estás?"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"\n✓ Generated response:")
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("\n✅ SUCCESS: Mistral-7B can run on this hardware!")
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
