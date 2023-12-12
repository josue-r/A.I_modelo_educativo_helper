import PyPDF2
from PIL import Image
import pytesseract
import pdfplumber

#file_path= '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/DIAGNOSTICO ESCOLAR MARIA IZQUIERDO 23-24.pdf'

#file_path= '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/GRM PROGRAMA ANÁLITICO.pdf'


#####
# def read_pdf(file_path):
#     # Open the PDF file in binary read mode
#     with open(file_path, 'rb') as file:
#         # Create a PDF reader object
#         pdf_reader = PyPDF2.PdfReader(file)

#         # Initialize a variable to store extracted text
#         text = ''

#         # Iterate through each page and extract text
#         # Iterate through each page and extract text
#         for page in pdf_reader.pages:
#             text += page.extract_text()

#         return text

# # Call the read_pdf function and store the returned text
# extracted_text = read_pdf(file_path)

# # Print the extracted text
# print(extracted_text)



####this is to read images

# def ocr_pdf(file_path):
#     # Open the image file
#     img = Image.open(file_path)
    
#     # Use Tesseract to do OCR on the image
#     text = pytesseract.image_to_string(img, lang='spa')  # specify the language if necessary

#     return text

# # Assuming the function ocr_pdf is defined as shown above

# # Specify the path to your image file
# image_file_path = '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/GRM PROGRAMA ANÁLITICO .pdf'  # Change this to your image file path

# # Call the ocr_pdf function and store the returned text
# extracted_text = ocr_pdf(image_file_path)

# # Print the extracted text
# print(extracted_text)



# def read_pdf_columns(file_path):
#     text_by_column = []
#     with pdfplumber.open(file_path) as pdf:
#         for page in pdf.pages:
#             # Split the page into a grid of rectangles and extract text from each
#             # Adjust the parameters based on the actual layout of your PDF
#             columns = page.extract_table({
#                 "vertical_strategy": "lines", 
#                 "horizontal_strategy": "text"
#             })
#             text_by_column.append(columns)
#     return text_by_column

# # The path to the PDF file
# pdf_file_path = '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/GRM PROGRAMA ANÁLITICO .pdf'

# # Extract text by columns from the PDF
# columns_text = read_pdf_columns(pdf_file_path)

# # Print the extracted text by columns
# for page in columns_text:
#     for column in page:
#         print(column)


def extract_tables_from_pdf(pdf_path):
    all_tables = []  # List to store all tables from each page

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        first_page=pdf.pages[0]
        tables= first_page.extract_tables()
        
        
        # # Loop over each page in the PDF
        # for page in pdf.pages:
        #     # Attempt to extract a table from the page
        #     current_page_tables = page.extract_tables()

            # # If tables are found, add them to the list
            # for table in current_page_tables:
            #     all_tables.append(table)
    
    return tables

# Path to your PDF file
pdf_file_path = '/Users/josue.ruiz/Documents/Projects/code/AI_Playground/proyecto-SEP/GRM PROGRAMA ANÁLITICO .pdf'

# Extract tables from the PDF
tables = extract_tables_from_pdf(pdf_file_path)

# Now, you can print the tables or process them further
for table in tables:
    for row in table:
        print(row)