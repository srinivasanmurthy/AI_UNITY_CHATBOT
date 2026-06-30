from transformers import pipeline

class HealthcareChatbot:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def get_response(self, user_input):
        # Generate the response
        response = self.generator(user_input, max_length=50, num_return_sequences=1)
        generated_text = response[0]["generated_text"]
        
        # Remove the input from the generated text to avoid repetition
        if generated_text.startswith(user_input):
            response_text = generated_text[len(user_input):].strip()
        else:
            response_text = generated_text
        
        return response_text

if __name__ == "__main__":
    chatbot = HealthcareChatbot()
    user_input = "What are the symptoms of flu?"
    print(chatbot.get_response(user_input))
