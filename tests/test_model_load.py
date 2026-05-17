import os
import pytest
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from app import sanitize_model_name

SMALL_MODEL = "distilgpt2"


def test_sanitize_model_name_replaces_gguf():
    bad_model = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"
    sanitized = sanitize_model_name(bad_model)
    assert sanitized == "mistralai/Mistral-7B-Instruct-v0.1"


@pytest.mark.slow
def test_small_model_generates_response():
    tokenizer = AutoTokenizer.from_pretrained(SMALL_MODEL, use_fast=False)
    model = AutoModelForCausalLM.from_pretrained(
        SMALL_MODEL,
        torch_dtype=torch.float16,
        device_map="auto",
        low_cpu_mem_usage=True,
    )

    prompt = "Hola, ¿cómo estás?"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=32,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    assert response and response.strip() != ""
    assert "Hola" in response or len(response.split()) > 1
