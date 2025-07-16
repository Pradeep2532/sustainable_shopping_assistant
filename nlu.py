# nlu.py
import re
from knowledge_base import (
    get_eco_alternatives_data,
    get_food_waste_tips_data,
    get_environmental_impact_data,
    get_general_sustainability_tips
)

def classify_intent(user_input):
    """
    Classifies the user's intent based on keywords and patterns.
    Returns a tuple: (intent_type, extracted_item)
    """
    user_input = user_input.lower()

    # --- 1. Specific Eco-friendly Alternative Query (e.g., "alternative to plastic bags") ---
    # Captures specific item requests, e.g., "alternative to plastic wrap", "eco-friendly alternative for coffee pods"
    match_specific_alternative = re.search(r"(?:eco-friendly alternative for|alternative to)\s*([a-z0-9\s]+)", user_input)
    if match_specific_alternative:
        item = match_specific_alternative.group(1).strip()
        if item and len(item) > 2: # Ensure a meaningful item was extracted
            return "eco_alternative", item

    # --- 2. Eco-friendly X (e.g., "eco-friendly plastic bottles") ---
    # Catches patterns like "eco-friendly X" where X is the item, but not "eco-friendly alternatives"
    match_eco_friendly_item = re.search(r"eco-friendly\s+([a-z0-9\s]+)", user_input)
    if match_eco_friendly_item and "alternatives" not in user_input:
        item = match_eco_friendly_item.group(1).strip()
        if item and len(item) > 2:
            return "eco_alternative", item

    # --- 3. General Eco-friendly Alternatives Query (e.g., "eco-friendly alternatives") ---
    # Broader check for general queries about alternatives without a specific item
    if "eco-friendly alternatives" in user_input or "eco alternatives" in user_input or "eco-friendly options" in user_input or "eco friendly" in user_input or "eco-friendly" in user_input:
        return "eco_alternative_general", None

    # --- 4. Environmental Impact Query (e.g., "environmental impact of beef") ---
    match_impact = re.search(r"(?:environmental impact of|impact of)\s*([a-z0-9\s]+)", user_input)
    if match_impact:
        item = match_impact.group(1).strip()
        if item and len(item) > 2:
            return "environmental_impact", item
        return "environmental_impact", None # If no item found but intent is clear

    # --- 5. Food Waste Tips Query (e.g., "food waste tips") ---
    if "food waste tips" in user_input or "reduce food waste" in user_input or "stop wasting food" in user_input:
        return "food_waste_tips", None

    # --- 6. General Sustainability Tips Query (e.g., "general sustainability tips") ---
    # Add more flexible keyword checks for general sustainability
    if "general sustainability tips" in user_input or \
       "sustainable shopping tips" in user_input or \
       "how to be more sustainable" in user_input or \
       "general sustainability" in user_input or \
       "sustainability tips" in user_input: # Added more general phrases
        return "general_sustainability_tips", None

    # --- 7. Greetings ---
    # Keep this relatively broad but less aggressive than specific queries
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        if len(user_input.split()) < 5: # If input is short and contains a greeting word
            return "greeting", None

    # --- 8. Default/Unknown Intent ---
    return "unknown", None


def get_response_for_intent(intent, item=None):
    """
    Generates a response based on the classified intent and extracted item.
    """
    if intent == "greeting":
        return "Hello there! How can I help you shop more sustainably today? You can ask about eco-friendly alternatives, food waste tips, environmental impact of items, or general sustainability tips."

    elif intent == "eco_alternative": # For specific item requests (e.g., "plastic wrap")
        if item:
            alternatives = get_eco_alternatives_data()
            for key, value in alternatives.items():
                if key in item:
                    return value
            return f"I don't have a specific eco-friendly alternative for '{item}' yet. Generally, look for items with minimal packaging or reusable options."
        else:
            # This 'else' should be less common with the improved NLU, but good to have
            return "What specific item are you looking for an eco-friendly alternative for?"

    elif intent == "eco_alternative_general": # New case for general query (e.g., "eco-friendly alternatives")
        return "Are you looking for eco-friendly alternatives for a specific item, or just general tips? For specific items, try asking 'eco-friendly alternative for plastic bags' or 'eco-friendly coffee pods'."

    elif intent == "food_waste_tips":
        tips = get_food_waste_tips_data()
        return "\n".join([f"- {tip}" for tip in tips])

    elif intent == "environmental_impact":
        if item:
            impacts = get_environmental_impact_data()
            for key, value in impacts.items():
                if key in item:
                    return value
            return f"I'm learning about the environmental impact of '{item}'. Generally, consider locally sourced and seasonal produce to reduce impact."
        else:
            return "What item's environmental impact are you curious about?"

    elif intent == "general_sustainability_tips":
        tips = get_general_sustainability_tips()
        return "\n".join([f"- {tip}" for tip in tips])

    elif intent == "unknown":
        return "I'm not sure how to help with that. Can you ask about eco-friendly alternatives, food waste tips, environmental impact, or general sustainability tips?"

    return "Something went wrong. Please try again."