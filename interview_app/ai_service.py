"""
AI Service for generating questions and evaluating answers using Groq API.
"""
import os
from groq import Groq
from django.conf import settings
import json


class AIInterviewService:
    """
    Service class to interact with Groq AI API for interview questions and evaluation.
    """
    
    def __init__(self):
        """Initialize Groq client with API key."""
        self.api_key = settings.GROQ_API_KEY
        if not self.api_key or self.api_key == 'your_groq_api_key_here':
            # Use fallback mode without API
            self.client = None
            self.model = "llama3-8b-8192"
        else:
            try:
                self.client = Groq(api_key=self.api_key)
                self.model = "llama3-8b-8192"
            except Exception as e:
                print(f"Error initializing Groq client: {e}")
                self.client = None
                self.model = "llama3-8b-8192"
    
    def generate_question(self, interview_type):
        """
        Generate an interview question based on the interview type.
        
        Args:
            interview_type (str): Type of interview (HR, Technical, Behavioral)
        
        Returns:
            str: Generated interview question
        """
        # If no API client, return fallback immediately
        if not self.client:
            return self._get_fallback_question(interview_type)
        
        prompt = f"""Generate a professional interview question for a {interview_type} interview.
        
The question should be:
- Clear and specific
- Relevant to {interview_type} interviews
- Professional and appropriate
- Not too easy, not too hard

Return ONLY the question, nothing else."""
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=200,
            )
            
            question = chat_completion.choices[0].message.content.strip()
            return question
        
        except Exception as e:
            print(f"Error generating question: {e}")
            return self._get_fallback_question(interview_type)
    
    def evaluate_answer(self, question, answer, interview_type):
        """
        Evaluate the user's answer using AI.
        
        Args:
            question (str): The interview question
            answer (str): User's answer
            interview_type (str): Type of interview
        
        Returns:
            dict: Evaluation results with score, strengths, weaknesses, suggestions
        """
        # If no API client, return fallback immediately
        if not self.client:
            return self._get_fallback_evaluation(answer)
        
        prompt = f"""You are an expert HR interviewer evaluating a {interview_type} interview answer.

Question: {question}

Answer: {answer}

Provide a detailed evaluation in the following JSON format:
{{
    "score": <number from 1-10>,
    "strengths": "<list 2-3 key strengths>",
    "weaknesses": "<list 2-3 areas for improvement>",
    "suggestions": "<provide specific suggestions for a better answer>",
    "confidence": "<Low/Medium/High based on answer quality>"
}}

Be constructive, specific, and professional. Return ONLY valid JSON."""
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=0.5,
                max_tokens=500,
            )
            
            response = chat_completion.choices[0].message.content.strip()
            
            # Try to parse JSON response
            try:
                # Extract JSON if wrapped in markdown code blocks
                if "```json" in response:
                    response = response.split("```json")[1].split("```")[0].strip()
                elif "```" in response:
                    response = response.split("```")[1].split("```")[0].strip()
                
                evaluation = json.loads(response)
                
                # Validate required fields
                required_fields = ['score', 'strengths', 'weaknesses', 'suggestions', 'confidence']
                for field in required_fields:
                    if field not in evaluation:
                        raise ValueError(f"Missing field: {field}")
                
                # Ensure score is within range
                evaluation['score'] = max(1, min(10, int(evaluation['score'])))
                
                return evaluation
            
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error parsing AI response: {e}")
                return self._parse_text_evaluation(response, answer)
        
        except Exception as e:
            print(f"Error evaluating answer: {e}")
            return self._get_fallback_evaluation(answer)
    
    def _parse_text_evaluation(self, response, answer):
        """Parse non-JSON AI response into structured format."""
        # Basic scoring based on answer length and content
        word_count = len(answer.split())
        score = min(10, max(3, word_count // 10))
        
        return {
            'score': score,
            'strengths': 'Your answer shows effort and engagement with the question.',
            'weaknesses': 'Consider providing more specific examples and details.',
            'suggestions': 'Structure your answer with clear points and real-world examples.',
            'confidence': 'Medium'
        }
    
    def _get_fallback_question(self, interview_type):
        """Return a fallback question if AI generation fails."""
        fallback_questions = {
            'HR': 'Tell me about yourself and why you are interested in this position.',
            'Technical': 'Explain the difference between a list and a tuple in Python.',
            'Behavioral': 'Describe a challenging situation you faced at work and how you handled it.'
        }
        return fallback_questions.get(interview_type, 'Tell me about your experience and skills.')
    
    def _get_fallback_evaluation(self, answer):
        """Return a fallback evaluation if AI evaluation fails."""
        word_count = len(answer.split())
        score = min(10, max(3, word_count // 10))
        
        return {
            'score': score,
            'strengths': 'You provided a response to the question.',
            'weaknesses': 'Try to provide more detailed and structured answers.',
            'suggestions': 'Include specific examples and elaborate on your points.',
            'confidence': 'Medium'
        }
