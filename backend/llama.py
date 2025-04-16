# from llama_cpp import Llama

# # Load LLaMA model (path to consolidated.00.pth or ideally .gguf file)
# MODEL_PATH = "./Llama-3.1-8B/original/consolidated.00.pth"


# Initialize LLaMA
# llm = Llama(model_path=MODEL_PATH, n_ctx=2048)  # You can adjust context size as needed

llm = None


def rewrite_text(input_text):
    """
    Rewrite the input text in a descriptive and engaging way using LLaMA.
    """
    try:
        prompt = f"Rewrite this text in a descriptive and engaging way:\n{input_text}"
        output = llm(prompt, max_tokens=256, temperature=0.7, stop=["</s>"])
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Error: {e}"


def summarize_text(input_text):
    """
    Summarize the input text concisely using LLaMA.
    """
    try:
        prompt = f"Summarize this text concisely:\n{input_text}"
        output = llm(prompt, max_tokens=256, temperature=0.7, stop=["</s>"])
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Error: {e}"

def generate_random_idea():
    """
    Generate a random creative idea using LLaMA.
    """
    try:
        prompt = "Generate a random creative idea:"
        output = llm(prompt, max_tokens=256, temperature=1.0, stop=["</s>"])
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    input_text = "Artificial Intelligence is transforming industries worldwide by automating processes and enabling advanced decision-making."

    print("Rewritten Text:")
    print(rewrite_text(input_text))

    print("\nSummarized Text:")
    print(summarize_text(input_text))

    print("\nRandom Idea:")
    print(generate_random_idea())
