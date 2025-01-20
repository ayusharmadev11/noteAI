from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the LLaMA 3.1 8B Instruct model and tokenizer (replace with your model path)
model_path = "path_to_your_llama_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")


def rewrite_text(input_text):
    """
    Rewrite the input text in a descriptive way using LLaMA 3.1 8B Instruct.

    :param input_text: The text to be rewritten.
    :return: The rewritten text.
    """
    try:
        prompt = f"Rewrite this text in a descriptive and engaging way:\n{input_text}"
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_length=512, temperature=0.7)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error: {e}"


def summarize_text(input_text):
    """
    Summarize the input text using LLaMA 3.1 8B Instruct.

    :param input_text: The text to be summarized.
    :return: The summarized text.
    """
    try:
        prompt = f"Summarize this text concisely:\n{input_text}"
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_length=512, temperature=0.7)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error: {e}"


def generate_random_idea():
    """
    Generate a random creative idea using LLaMA 3.1 8B Instruct.

    :return: A randomly generated idea.
    """
    try:
        prompt = "Generate a random creative idea."
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_length=512, temperature=1.0)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error: {e}"


# Example usage (Replace with actual model path and test inputs):
if __name__ == "__main__":
    input_text = "Artificial Intelligence is transforming industries worldwide by automating processes and enabling advanced decision-making."

    print("Rewritten Text:")
    print(rewrite_text(input_text))

    print("\nSummarized Text:")
    print(summarize_text(input_text))

    print("\nRandom Idea:")
    print(generate_random_idea())
