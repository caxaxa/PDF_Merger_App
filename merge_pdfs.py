import os
import PyPDF2

def merge_pdfs(input_dir: str, output_path: str) -> None:
    """
    Merges all the PDF files in the given `input_dir` (alphabetically)
    into a single file at `output_path`.
    """
    # Get a sorted list of all PDF files
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
    pdf_files.sort()
    
    # Create a PdfMerger object
    merger = PyPDF2.PdfMerger()
    
    # Append each PDF
    for pdf_file in pdf_files:
        full_path = os.path.join(input_dir, pdf_file)
        merger.append(full_path)
    
    # Write out the merged PDF
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    # Locate the `input_files` folder relative to this script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder_path = os.path.join(script_dir, 'input_files')
    
    # Define the name or path for the output file
    output_file_path = os.path.join(script_dir, 'merged.pdf')
    
    merge_pdfs(input_folder_path, output_file_path)
    print(f"PDFs merged successfully into {output_file_path}")
