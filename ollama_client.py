import requests
import json

class OllamaClient:
    """
    Client for interacting with locally running Ollama LLM.
    """
    
    def __init__(self, base_url="http://localhost:11434", model="llama3:latest"):
        """
        Initialize the Ollama client.
        
        Args:
            base_url: URL where Ollama is running
            model: The model to use for generation
        """
        self.base_url = base_url
        self.model = model
        self.api_endpoint = f"{base_url}/api/generate"
    
    def compare_reports(self, original_text, ai_text):
        """
        Send both reports to Ollama for comparison.
        
        Args:
            original_text: Text from the original (human) report
            ai_text: Text from the AI-generated report
            
        Returns:
            dict: The parsed response from Ollama
        """
        prompt = self._create_comparison_prompt(original_text, ai_text)
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(self.api_endpoint, json=payload)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with Ollama: {str(e)}")
    
    def _create_comparison_prompt(self, original_text, ai_text):
        """
        Create a prompt for the LLM to compare the two reports.
        
        Args:
            original_text: Text from the original (human) report
            ai_text: Text from the AI-generated report
            
        Returns:
            str: The formatted prompt
        """
        return f"""You are a medical reviewer. Compare the following two radiology reports.

Original Report:
{original_text}

AI-Generated Report:
{ai_text}

List any significant differences between the two.
- Mention if any key finding is missing in the AI report.
- Mention if anything is added or changed.
- Focus on clinical relevance.
- Categorize differences as "Critical", "Moderate", or "Minor".
Respond as a bullet list in plain text.
"""

    def ask_question(self, original_text, ai_text, question):
        """
        Send a specific question about the reports to Ollama.
        
        Args:
            original_text: Text from the original (human) report
            ai_text: Text from the AI-generated report
            question: The user's question
            
        Returns:
            str: The response from Ollama
        """
        prompt = self._create_question_prompt(original_text, ai_text, question)
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(self.api_endpoint, json=payload)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with Ollama: {str(e)}")
    
    def _create_question_prompt(self, original_text, ai_text, question):
        """
        Create a prompt for the LLM to answer a specific question about the reports.
        
        Args:
            original_text: Text from the original (human) report
            ai_text: Text from the AI-generated report
            question: The user's question
            
        Returns:
            str: The formatted prompt
        """
        return f"""You are a medical reviewer. Analyze the following two radiology reports and answer the specific question.

Original Report:
{original_text}

AI-Generated Report:
{ai_text}

Question: {question}

Provide a detailed and accurate answer to the question based on the information in both reports.
"""