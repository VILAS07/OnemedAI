import PyPDF2
import io

class PDFProcessor:
    """
    A class to handle PDF text extraction using PyPDF2.
    """
    
    @staticmethod
    def extract_text(pdf_file):
        """
        Extract text from a PDF file.
        
        Args:
            pdf_file: The uploaded PDF file object
            
        Returns:
            str: Extracted text from the PDF
        """
        try:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.getvalue()))
            
            # Extract text from all pages
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n\n"
            
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")