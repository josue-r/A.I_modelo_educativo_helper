from flask import Flask, render_template, request,jsonify
import os
from sep import read_pdf, read_docx, get_completion  # Import functions from your script

app = Flask(__name__)

@app.route('/')
def index():
    #prompt = get_current_prompt()
    return render_template('index.html')  # Renders the front-end HTML

@app.route('/process', methods=['POST'])
def process_files():
    if request.method == 'POST':
        # Process the uploaded files
        pdf_file = request.files['pdfDiagnostico']
        docx_file = request.files['docxPrograma']
        user_prompt = request.form['promptInput']

        # # Save files to a temporary directory
        # pdf_file = os.path.join('temp', pdfDiagnostico.filename)
        # docx_file = os.path.join('temp', docxPrograma.filename)
        # pdfDiagnostico.save(pdfDiagnostico)
        # docxPrograma.save(docxPrograma)

        # Use your existing functions to process the files
        diagnostico = read_pdf(pdf_file)
        programa = read_docx(docx_file)

        context = [{'role':'system', 'content': diagnostico}]
        # Construct the full prompt
        prompt = f"{user_prompt}\n\nDiagnostico: {context} \n Programa: {programa}"

        # Call the get_completion function
        response = get_completion(prompt)
        response_content = response.model_dump()['choices'][0]['message']["content"]

        # Return the response content to the frontend
        return jsonify({"response": response_content})


if __name__ == '__main__':
    app.run(debug=True)
