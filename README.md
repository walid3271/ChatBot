To Run:

git clone https://github.com/walid3271/ChatBot.git

pest your hugging-face API Key in the .env file

Open Command Prompt in LLAMA Directory

code . (to open the in vs-code)

Open the Command Prompt in the vs-code terminal

python -m venv venv (Create virtual environment)

.\venv\Scripts\activate.bat

pip install requirements.txt

python -m uvicorn app:app --reload

streamlit run client.py
