import google.generativeai as gurt
from django.conf import settings

gurt.configure(api_key=settings.GEMINI_API_KEY)

def response(prompt_text):
    """
    Generates text using the Gemini API.
    """
    try:
        # Choose your model (e.g., 'gemini-pro' for text-only)
        model = gurt.GenerativeModel('gemini-2.0-flash') # Or 'gemini-pro', gemini-1.5-flash-latest, etc.
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        # Handle API errors gracefully
        print(f"Error calling Gemini API: {e}")
        return None # Or raise a custom exception

# Add other functions for different Gemini functionalities as needed