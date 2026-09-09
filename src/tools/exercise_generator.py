import os
from google import genai
from db.queries import get_rand_id_subject, get_concept,save_exercise
import json

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

def generate_exercise(subject_id=None):
    # Get the informations
    if subject_id == None:
        subject_id = get_rand_id_subject()

    concept = get_concept(subject_id)

    # Create the prompt
    prompt = f"""
You are a mathematics teacher.

Generate one mathematics exercise based on the following concept:

Concept: {concept['name']}
Description: {concept['description']}

Requirements:
- The exercise must be mathematically correct.
- Difficulty must be an integer from 1 to 5.
- Provide a clear question.
- Provide the expected answer.
- Provide a concise explanation/solution.
- Do not include Markdown.
- Return ONLY valid JSON.

Required JSON format:
{{
    "question": "...",
    "expected_answer": "...",
    "explanation": "...",
    "difficulty": 1
}}
"""
    # Send the prompt to the AI 
    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=prompt
    )
    try:
            exercise = json.loads(response.text)
    except json.JSONDecodeError as error:
            raise ValueError(
                f"Gemini returned invalid JSON:\n{response.text}"
            ) from error

    # Save the exercise in the database
    save_exercise(
        concept_id=subject_id,
        question=exercise['question'],
        expected_answer=exercise['expected_answer'],
        explanation=exercise['explanation'],
        difficulty=exercise['difficulty'],
        generated_by='gemini',
        model_name='gemini-flash'
    )
    return exercise