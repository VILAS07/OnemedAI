from file_processor import FileProcessor
from ollama_client import OllamaClient

class ReportComparator:
    """
    Class to handle the comparison of radiology reports.
    """
    
    def __init__(self, model="llama3:latest"):
        """
        Initialize the report comparator.
        
        Args:
            model: The Ollama model to use
        """
        self.file_processor = FileProcessor()
        self.ollama_client = OllamaClient(model=model)
    
    def compare(self, original_file, ai_file):
        """
        Compare the original and AI-generated reports.
        
        Args:
            original_file: The uploaded original file
            ai_file: The uploaded AI-generated file
            
        Returns:
            dict: A dictionary containing the extracted texts and comparison results
        """
        # Extract text from both files
        original_text = self.file_processor.extract_text(original_file)
        ai_text = self.file_processor.extract_text(ai_file)
        
        # Get comparison from Ollama
        comparison_result = self.ollama_client.compare_reports(original_text, ai_text)
        
        return {
            "original_text": original_text,
            "ai_text": ai_text,
            "comparison": comparison_result
        }
    
    def ask_question(self, original_file, ai_file, question):
        """
        Ask a specific question about the reports.
        
        Args:
            original_file: The uploaded original file
            ai_file: The uploaded AI-generated file
            question: The user's question about the reports
            
        Returns:
            str: The answer from the LLM
        """
        # Extract text from both files
        original_text = self.file_processor.extract_text(original_file)
        ai_text = self.file_processor.extract_text(ai_file)
        
        # Get answer from Ollama
        answer = self.ollama_client.ask_question(original_text, ai_text, question)
        
        return answer