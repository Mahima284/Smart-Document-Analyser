def summarize_text(text, word_limit):

    words = text.split()

    summary = " ".join(words[:word_limit])

    return summary