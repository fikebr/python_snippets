import google.generativeai as genai
import PIL.Image
import re

# https://pyimagesearch.com/2024/02/12/image-processing-with-gemini-pro/
# https://aistudio.google.com/app/apikey
# https://ai.google.dev/tutorials/python_quickstart

# pip install -q -U google-generativeai
# pip install pillow

def extract_between_tags(tag: str, string: str):
    pattern = f"<{tag}>(.+?)</{tag}>"
    # print("pattern = " + pattern)
    match = re.search(pattern, string, flags=re.DOTALL)
    if match:
        metadata_block = match.group(1)  # Extract the captured group (content between tags)
        return(metadata_block)
    else:
        return(string)

def analyze_image(google_api_key, model, file, prompt):
    try:
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel(model)
        img = PIL.Image.open(file)
        response = model.generate_content([prompt, img], stream=True)
        response.resolve()
        answer = response.text
        # print("answer = " + answer)
        j = extract_between_tags("metadata", answer)
        return(j)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        raise e

def parse_description(google_api_key, model, prompt, desc, parts):
    """
Parse the description using the Google Generative AI API.

Args:
    google_api_key (str): The API key for accessing the Google Generative AI API.
    model (str): The name of the generative model to use.
    prompt (str): The prompt to use for generating the content.
    desc (str): The description to include in the prompt.
    parts (list): A list of parts to generate content for.

Returns:
    parsed: A dictionary containing the generated content for each part.

Raises:
    Exception: If there is an error while parsing the description.

"""
    try:
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel(model)
        parsed = {}

        for part in parts:
            prompt1 = prompt.format(part=part, desc=desc)
            response = model.generate_content(prompt1)
            response.resolve()
            parsed[part] = response.text

        return parsed

    except Exception as e:
        raise e

