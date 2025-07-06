import os
import subprocess
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer once (outside the function for efficiency)
model_name = "bigcode/starcoder"  # Or another model from Hugging Face
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
except Exception as e:
    tokenizer = None
    model = None
    print(f"// Model loading error: {e}")

def send_to_llm(code, yaml_path):
    if model is None or tokenizer is None:
        return "// LLM model not loaded. Check model name and dependencies."
    with open(yaml_path) as f:
        yaml_prompt = f.read()
    prompt = f"{yaml_prompt}\n\n{code}"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    src_dir = "orgChartApi/orgChartApi/controllers"  # Updated to match actual source path
    test_dir = "tests"
    yaml_prompt = "yaml_instructions/generate_tests.yaml"
    os.makedirs(test_dir, exist_ok=True)
    for filename in os.listdir(src_dir):
        if filename.endswith(".cc") or filename.endswith(".h"):
            with open(os.path.join(src_dir, filename)) as f:
                code = f.read()
            test_code = send_to_llm(code, yaml_prompt)
            with open(os.path.join(test_dir, f"test_{filename}.cpp"), "w") as f:
                f.write(test_code)

if __name__ == "__main__":
    main()
