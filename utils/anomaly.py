import re

def detect_anomalies(text):

    anomalies = []

    years = re.findall(r'20\d{2}', text)

    for year in years:

        if int(year) > 2030:

            anomalies.append(
                f"Future suspicious year: {year}"
            )

    if "invoice" in text.lower():

        if "invoice number" not in text.lower():

            anomalies.append(
                "Invoice number missing"
            )

    return anomalies