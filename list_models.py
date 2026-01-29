import google.generativeai as genai
import sys

# Get API key from command line argument
if len(sys.argv) != 2:
    print("Usage: python list_models.py <API_KEY>")
    sys.exit(1)

api_key = sys.argv[1]

try:
    genai.configure(api_key=api_key)
    
    print("Available models:")
    print("-" * 50)
    
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"Model: {model.name}")
            print(f"Display Name: {model.display_name}")
            print(f"Description: {model.description}")
            print("-" * 30)
            
except Exception as e:
    print(f"Error: {e}")