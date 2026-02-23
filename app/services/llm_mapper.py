import json
from google import genai
from app.models.registries import PARAMETER_REGISTRY, ASSET_REGISTRY
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def map_headers_with_llm(headers):

    prompt = f"""
                You are an industrial ESG data mapping agent.

                Map the given Excel headers to canonical parameter names and asset names.

                Rules:
                - Only use parameters from PARAMETER_REGISTRY.
                - Only use assets from ASSET_REGISTRY.
                - If no match, return null.
                - Provide confidence: high, medium, low.
                Return STRICT JSON list like:

                [
                {{
                    "column_index": 0,
                    "header": "Coal Used AFBC-1",
                    "param_name": "coal_consumption",
                    "asset_name": "AFBC-1",
                    "confidence": "high"
                }}
                ]

                HEADERS:
                {headers}
                PARAMETER_REGISTRY:
                {PARAMETER_REGISTRY}

                ASSET_REGISTRY:
                {ASSET_REGISTRY}
            """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
    )

    text = response.text

    # Gemini may wrap JSON in markdown — clean it
    text = text.strip().replace("```json", "").replace("```", "")

    try:
        return json.loads(text)
    except:
        return []