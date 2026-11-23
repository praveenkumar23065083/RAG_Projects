
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "openai/gpt-oss-120b"


def generate_answer(query, retrieved_chunks):

    if not retrieved_chunks:
        return (
            "I could not find enough information "
            "in the provided papers."
        )

    context = ""

    for i, chunk in enumerate(retrieved_chunks, start=1):

        context += f"""
[Source {i}]

Paper:
{chunk["document_name"]}

Page:
{chunk["page_number"]}

Content:
{chunk["text"]}

"""

    prompt = f"""
You are a research paper assistant.

Answer the user's question using ONLY the information
contained in the provided sources.

IMPORTANT RULES:

1. Do not use outside knowledge.
2. Do not invent or assume information.
3. Every factual claim in your answer must have a source citation.
4. Cite sources using [Source X].
5. If multiple sources support a claim, cite all relevant sources.
6. If the question involves multiple research papers,
   use information from all relevant papers.
7. When comparing papers, clearly identify which information
   belongs to which paper.
8. If the provided sources do not contain enough information,
   say exactly:

"I could not find enough information in the provided papers."

User question:
{query}

Provided sources:
{context}

Give a clear and concise answer with citations.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=700,
        temperature=0.1
    )

    return response.choices[0].message.content
