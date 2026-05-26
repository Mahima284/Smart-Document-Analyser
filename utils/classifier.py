def classify_document(text):

    text = text.lower()

    if "invoice" in text:
        return "Financial"

    elif "contract" in text:
        return "Legal"

    elif "abstract" in text:
        return "Academic"

    return "Unknown"