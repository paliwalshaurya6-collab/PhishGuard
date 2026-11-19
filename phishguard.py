import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = {
    "login", "verify", "update", "secure", "account",
    "banking", "password", "signin", "confirm", "wallet"
}

def analyze_url(raw_url):
    """Return a simple rule-based phishing risk assessment for a URL."""
    url = raw_url.strip()
    if not url:
        return {"score": 0, "level": "Invalid input", "reasons": ["Please enter a URL."]}

    candidate = url if "://" in url else "http://" + url
    parsed = urlparse(candidate)
    host = parsed.hostname or ""
    full_lower = candidate.lower()

    score = 0
    reasons = []

    if parsed.scheme.lower() == "http":
        score += 1
        reasons.append("Uses HTTP rather than HTTPS.")

    if not host:
        score += 2
        reasons.append("The URL does not contain a valid hostname.")
    elif re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", host):
        score += 2
        reasons.append("Uses an IP address instead of a domain name.")

    if "@" in candidate:
        score += 2
        reasons.append("Contains '@', which can disguise the actual destination.")

    if len(candidate) > 75:
        score += 1
        reasons.append("Unusually long URL (over 75 characters).")

    if host.count("-") >= 2:
        score += 1
        reasons.append("Hostname contains multiple hyphens.")

    found_words = sorted(word for word in SUSPICIOUS_WORDS if word in full_lower)
    if found_words:
        score += 1
        reasons.append("Contains attention-grabbing terms: " + ", ".join(found_words) + ".")

    if parsed.port is not None:
        score += 1
        reasons.append("Uses a non-default port.")

    if score >= 4:
        level = "High risk"
    elif score >= 2:
        level = "Potentially suspicious"
    else:
        level = "Low risk indicators"

    if not reasons:
        reasons.append("No indicators from this basic rule set were found.")

    return {"score": score, "level": level, "reasons": reasons}


def main():
    print("=" * 48)
    print("             PHISHGUARD")
    print("       Rule-Based URL Risk Checker")
    print("=" * 48)
    print("Educational tool only. Do not treat results as proof.\n")

    while True:
        url = input("Enter a URL (or type 'exit' to quit): ").strip()
        if url.lower() == "exit":
            print("Exiting PhishGuard. Stay safe online!")
            break

        result = analyze_url(url)
        print(f"\nRisk level: {result['level']}")
        print(f"Risk score: {result['score']}")
        print("Findings:")
        for reason in result["reasons"]:
            print(f" - {reason}")
        print("\nReminder: A low score does not guarantee a website is safe.\n")


if __name__ == "__main__":
    main()
