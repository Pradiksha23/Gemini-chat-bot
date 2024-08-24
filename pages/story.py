import os
import requests
import re
import json
import streamlit as st

apiKey = "822f1baa-fb17-41a2-a912-36fa86254e2c"

def apiFunction(usersInputObj):
    inputsArray = [{"id": "{input_1}", "label": "Enter text", "type": "text"}]
    prompt = "Generate a story from this text {input_1}"
    filesData, textData = {}, {}
    
    for inputObj in inputsArray:
        inputId = inputObj['id']
        if inputObj['type'] == 'text':
            prompt = prompt.replace(inputId, usersInputObj[inputId])
        elif inputObj['type'] == 'file':
            path = usersInputObj[inputId]
            file_name = os.path.basename(path)
            with open(path, 'rb') as f:
                filesData[inputId] = f

    textData['details'] = json.dumps({
        'appname': 'text to story generator',
        'prompt': prompt,
        'documentId': 'no-embd-type',
        'appId': '66c9245a64d827b744a2a17d',
        'memoryId': '',
        'apiKey': apiKey
    })
    
    response = requests.post('https://apiappstore.guvi.ai/api/output', data=textData, files=filesData)
    output = response.json()
    return output['output']

# Streamlit app code
st.title("Text to Story Generator")

# Get user input
user_input = st.text_input("Enter text:")

if st.button("Generate Story"):
    if user_input:
        usersInputObj = {'{input_1}': user_input}
        output = apiFunction(usersInputObj)
        url_regex = r'http://localhost:7000/'
        replaced_string = re.sub(url_regex, 'https://apiappstore.guvi.ai/', output)
        st.write(replaced_string)
    else:
        st.warning("Please enter some text to generate the story.")
