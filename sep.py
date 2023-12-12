from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import PyPDF2
from PIL import Image
from docx import Document



# Load environment variables from .env file
load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set your OpenAI API key

file_path_diagnostico= '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/DIAGNOSTICO ESCOLAR MARIA IZQUIERDO 23-24.pdf'
file_path_programa= '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/GRM PROGRAMA ANÁLITICO.docx'

##read pdf files
def read_pdf(file_path_diagnostico):
    # Open the PDF file in binary read mode
    with open(file_path_diagnostico, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize a variable to store extracted text
        text = ''

        # Iterate through each page and extract text
        # Iterate through each page and extract text
        for page in pdf_reader.pages:
            text += page.extract_text()

        return text

# # Call the read_pdf function and store the returned text
# extracted_text = read_pdf(file_path_diagnostico)

# # Print the extracted text
# print(extracted_text)


##read docx file
def read_docx(file_path_programa):
    try:
        doc = Document(file_path_programa)
        full_text = []

        for para in doc.paragraphs:
            full_text.append(para.text)

        return '\n'.join(full_text)

    except Exception as e:
        return str(e)

def cost_calculator_for_GPT_3_5_turbo_1106(response):

    # These 2 values are valid only for the "gpt-3.5-turbo-1106" model.
    # Check https://openai.com/pricing for up-to-date prices
    cost_of_input_tokens = 0.001
    cost_of_output_tokens = 0.002

    completion_tokens = response.model_dump()['usage']['completion_tokens']
    prompt_tokens = response.model_dump()['usage']['prompt_tokens']

    total_cost = (
        (prompt_tokens * cost_of_input_tokens) + (completion_tokens * cost_of_output_tokens)
    ) / 1000

    return f"Total cost for API call: ${total_cost} USD"




diagnostico = read_pdf(file_path_diagnostico)
#print (diagnostico)
programa = read_docx(file_path_programa)
context = [ {'role':'system', 'content':f""" {diagnostico}"""} ]  # accumulate messages


# prompt = f"""
# Diseña un proyecto educativo comunitario para alumnos de 2do de preescolar que considere elementos del diagnóstico, \
# que favorezca procesos de desarrollo contenidos en el programa analítico, que contemple recursos educativos como videos de YouTube, \
# y otros recursos educativos de internet. Que tenga una duración promedio de 15 días y que contenga criterios y herramientas para evaluar a los alumnos.\

# diagnostico: ```{context}```
# programa analítico: ```{programa}```

# """

prompt = f"""
titulo de punto 5 del diagnostico

diagnostico: ```{context}```
programa analítico: ```{programa}```

"""




## call to openAI API
def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response
    #return response.model_dump()['choices'][0]['message']["content"]

response = get_completion(prompt)
#print(response.model_dump()['usage']['completion_tokens'])
print(cost_calculator_for_GPT_3_5_turbo_1106(response))
print(response.model_dump()['choices'][0]['message']["content"])
