import openai


# Set your OpenAI API key
openai.api_key = "your_openai_api_key"


def rewrite_text(input_text):
    """
    Rewrite the input text in a descriptive way using GPT-4.

    :param input_text: The text to be rewritten.
    :return: The rewritten text.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in rewriting text in a descriptive and engaging way."},
                {"role": "user", "content": f"Rewrite this text: {input_text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"


def summarize_text(input_text):
    """
    Summarize the input text using GPT-4.

    :param input_text: The text to be summarized.
    :return: The summarized text
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in summarizing text into concise and clear summaries."},
                {"role": "user", "content": f"Summarize this text: {input_text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"


def generate_random_idea():
    """
    Generate a random creative idea using GPT-4.

    :return: A randomly generated idea.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant generating unique and innovative ideas."},
                {"role": "user", "content": "Generate a random creative idea."}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"


# Example usage (Replace with actual API key and test inputs):
if __name__ == "__main__":
    input_text = "Artificial Intelligence is transforming industries worldwide by automating processes and enabling advanced decision-making."

    print("Rewritten Text:")
    print(rewrite_text(input_text))

    print("\nSummarized Text:")
    print(summarize_text(input_text))

    print("\nRandom Idea:")
    print(generate_random_idea())

