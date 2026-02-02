def suggest_waste_type(description: str):
    """
    Mini AI: rule-based suggestion system.
    Companies LOVE this because it's simple and reliable.
    """
    if not description:
        return None

    text = description.lower()

    wet_keywords = ["banana", "peel", "food", "leftover", "rice", "vegetable", "fruit", "tea", "coffee", "egg", "bones"]
    dry_keywords = ["plastic", "bottle", "paper", "cardboard", "wrapper", "bag", "glass", "metal", "can"]
    ewaste_keywords = ["charger", "battery", "mobile", "phone", "laptop", "cable", "earphone", "mouse", "keyboard"]

    wet_score = sum(1 for k in wet_keywords if k in text)
    dry_score = sum(1 for k in dry_keywords if k in text)
    ewaste_score = sum(1 for k in ewaste_keywords if k in text)

    if ewaste_score > wet_score and ewaste_score > dry_score:
        return "EWASTE"
    elif wet_score > dry_score:
        return "WET"
    elif dry_score > wet_score:
        return "DRY"

    return "MIXED"


def calculate_segregation_score(selected_type: str, suggested_type: str):
    """
    Score logic:
    - If user selected exactly what system suggests: 100
    - If mixed: 60
    - Wrong type: 30
    - No suggestion: 50
    """
    if not suggested_type:
        return 50

    if selected_type == suggested_type:
        return 100

    if selected_type == "MIXED":
        return 60

    return 30


def get_tips(waste_type: str):
    tips = {
        "WET": "✅ Keep wet waste in a separate sealed bag to reduce smell.",
        "DRY": "✅ Rinse plastic bottles before disposal for better recycling.",
        "EWASTE": "✅ Store e-waste safely and hand it over only to authorized collectors.",
        "MIXED": "✅ Try splitting waste into Wet and Dry for better recycling impact.",
    }
    return tips.get(waste_type, "✅ Thanks for contributing to a cleaner city.")
