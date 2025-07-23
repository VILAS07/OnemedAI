import PyPDF2
import io
import pytesseract
from PIL import Image

class FileProcessor:
    """
    A class to handle text extraction from various file types including PDFs and images.
    """
    
    @staticmethod
    def extract_text(file):
        """
        Extract text from a file (PDF or image).
        
        Args:
            file: The uploaded file object
            
        Returns:
            str: Extracted text from the file
        """
        try:
            # Get file extension
            file_name = file.name.lower()
            
            # Process PDF files
            if file_name.endswith('.pdf'):
                return FileProcessor._extract_from_pdf(file)
            
            # Process image files
            elif file_name.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')):
                return FileProcessor._extract_from_image(file)
            
            else:
                raise Exception(f"Unsupported file type: {file_name}")
                
        except Exception as e:
            raise Exception(f"Error extracting text from file: {str(e)}")
    
    @staticmethod
    def _extract_from_pdf(pdf_file):
        """
        Extract text from a PDF file.
        """
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.getvalue()))
        
        # Extract text from all pages
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + "\n\n"
        
        return text
    
    @staticmethod
    def _extract_from_image(image_file):
        """
        Extract text from an image file using OCR.
        """
        # Open the image using PIL
        image = Image.open(io.BytesIO(image_file.getvalue()))
        
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(image)
        
        return text