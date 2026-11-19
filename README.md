# PhishGuard – Phishing URL Detector

## Project overview
PhishGuard is a beginner-friendly Python cybersecurity project. It checks a URL for common suspicious indicators and reports a simple risk score with explanations.

## Features
- Detects HTTP URLs (rather than HTTPS)
- Flags IP addresses used as hosts
- Checks for the `@` character
- Checks unusually long URLs
- Looks for multiple hyphens in the hostname
- Checks for common attention-grabbing words
- Reports a risk level and the reasons behind it

## Requirements
- Python 3
- No external Python packages required

## How to run
1. Open a terminal in this project folder.
2. Run:

   ```bash
   python3 phishguard.py
   ```

3. Enter a URL when prompted.
4. Type `exit` to close the program.

## Run the tests
```bash
python3 -m unittest -v
```

## Example
Input:
```text
http://192.168.1.10/login
```

The tool should flag the use of HTTP, an IP address, and a suspicious word.

## How it works
The program parses the URL and checks it against a small set of rules. Each matching rule adds points to a risk score. The score is mapped to one of three labels:
- 0–1: Low risk indicators
- 2–3: Potentially suspicious
- 4 or more: High risk

## Limitations
- This is a rule-based educational demonstration, not a production security product.
- It does not visit websites, inspect page content, or query threat-intelligence services.
- Legitimate websites can trigger warnings (false positives).
- Phishing websites can avoid these rules (false negatives).
- A low score does not mean a website is safe. Never enter passwords or payment details on a site just because this tool gives it a low score.

## Future improvements
- Add a graphical user interface
- Integrate a reputable threat-intelligence API
- Add domain age and reputation checks
- Improve URL normalization and validation

## Author
Name: Shaurya Paliwal
Course: B.Tech CSE
Specialization: Cybersecurity
University: JECRC University
