import os
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

def send_to_llm(test_code, yaml_path):
    if model is None or tokenizer is None:
        return "// LLM model not loaded. Check model name and dependencies."
    with open(yaml_path) as f:
        yaml_prompt = f.read()
    prompt = f"{yaml_prompt}\n\n{test_code}"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    test_dir = "../tests"
    yaml_prompt = "../yaml_instructions/refine_tests.yaml"
    for filename in os.listdir(test_dir):
        if filename.startswith("test_") and filename.endswith(".cpp"):
            with open(os.path.join(test_dir, filename)) as f:
                test_code = f.read()
            refined_code = send_to_llm(test_code, yaml_prompt)
            with open(os.path.join(test_dir, filename), "w") as f:
                f.write(refined_code)

if __name__ == "__main__":
    main()
