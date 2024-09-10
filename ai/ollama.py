import ollama

# pip install ollama
# https://github.com/ollama/ollama-python


def chat(model, prompt, image_base64_str=""):
    try:
        m = {}
        m["role"] = "user"
        m["content"] = prompt
        if image_base64_str:
            m["images"] = [image_base64_str]


        response = ollama.chat(model=model, messages=[m])

        return response["message"]["content"]

    except ollama.ResponseError as e:
        if e.status_code == 400:
            raise ValueError(
                "Bad request from Ollama: Your input may be invalid. {}".format(e)
            )
        elif e.status_code == 404:
            raise ollama.ResourceNotFoundError(
                "Resource not found on Ollama: The requested resource might not exist."
            )
        elif e.status_code == 500:
            raise ollama.InternalServerError(
                "Internal Server Error on Ollama: There might be a problem on the Ollama server."
            )
        else:
            raise ollama.OllamaUnexpectedError(
                f"Unhandled error code from Ollama: {e.status_code}"
            )
