import streamlit as st
import google.generativeai as genai
from google.oauth2 import service_account
import os

# Get the absolute path of the credentials file
GOOGLE_CREDENTIALS_PATH = os.path.join(os.getcwd(), "verdict.json")

# Ensure the file exists before using it
if not os.path.exists(GOOGLE_CREDENTIALS_PATH):
    raise FileNotFoundError(f"Credentials file not found at: {GOOGLE_CREDENTIALS_PATH}")

# Set the environment variable for Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CREDENTIALS_PATH

# Load the credentials from the JSON file
credentials = service_account.Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH)

# Configure the Gemini API using the credentials
def initialize_genai():
    """Initialize the Gemini API."""
    genai.configure(credentials=credentials)
    return genai

def call_gemini_api(message):
    """
    Function to interact with the Gemini API.
    
    Args:
        message (str): The input message for the chatbot
    
    Returns:
        str: The response from the Gemini API
    """
    try:
        # Send a simple message without roles
        response = genai.chat(messages=[message])  # Directly send the message text
        return response["choices"][0]["message"]  # Extract the response message
    except Exception as e:
        return f"Error communicating with Gemini API: {e}"

def app():
    """Streamlit app for the Gemini Chatbot."""
    st.title("Gemini Chatbot")
    st.write("Ask me anything! Type your message below:")

    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", placeholder="Type your message here...")
    
    if user_input:
        # Get response from Gemini
        response = call_gemini_api(user_input)
        
        # Add the current exchange to chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Gemini", response))

        # Display full chat history
        for role, message in st.session_state.chat_history:
            st.write(f"{role}: {message}")

if __name__ == "__main__":
    # Debug: Print working directory and credentials file location
    print("Current Working Directory:", os.getcwd())
    print("Google Credentials Path:", GOOGLE_CREDENTIALS_PATH)
    app()
