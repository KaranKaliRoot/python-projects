import PyPDF2
import os

def list_pdf_files(folder_path):
    pdf_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(folder_path, file))
    return pdf_files

def merge_pdfs(pdf_files, output_file):
    merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as f:
            merger.append(f)

    with open(output_file, 'wb') as f:
        merger.write(f)

if __name__ == "__main__":
    # Ask for folder path
    folder_path = input("Enter the folder path containing the PDF files: ")

    # List PDF files
    pdf_files_list = list_pdf_files(folder_path)

    if not pdf_files_list:
        print("No PDF files found in the specified folder.")
    else:
        # Generate comma-separated string
        pdf_files_string = ", ".join(pdf_files_list)

        print("List of PDF files:")
        print(pdf_files_string)

        # Ask for output path and name
        output_path = input("Enter the output folder path for the merged PDF: ")
        output_name = input("Enter the name for the merged PDF file (without extension): ")
        output_file = os.path.join(output_path, output_name + ".pdf")

        # Merge PDFs
        merge_pdfs(pdf_files_list, output_file)

        print("PDF files merged successfully!")
