import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/ask/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']

# Initialize history if not already done
if 'history' not in st.session_state:
    st.session_state.history = []

# Clear history function
def clear_history():
    st.session_state.history = []

# Delete individual history entry
def delete_history(index):
    del st.session_state.history[index]

# Streamlit UI
st.title('Ask With LLAMA')
input_text1 = st.text_input("Write a topic name")

if input_text1:
    response = get_ollama_response(input_text1)
    st.session_state.history.append({'input': input_text1, 'response': response})
    st.write(response)

# Sidebar with history and clear button
st.sidebar.title("History")
if st.sidebar.button("Clear History"):
    clear_history()

# Display history in sidebar
for i, entry in enumerate(st.session_state.history):
    with st.sidebar.expander(f"{entry['input']}"):
        st.write(f"**Input:** {entry['input']}")
        st.write(f"**Response:** {entry['response']}")
        if st.button(f"Delete", key=f"delete_{i}"):
            delete_history(i)
            st.experimental_rerun()  # Refresh the app to update the history
            
# streamlit run client.py