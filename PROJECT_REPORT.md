# Project Report: PhishGuard – Phishing URL Detector

## 1. Introduction
Phishing is a cyberattack in which an attacker tries to trick a person into revealing sensitive information, such as passwords or banking details, by pretending to be a trusted source. PhishGuard is a small educational tool that demonstrates how suspicious URL characteristics can be checked using Python.

## 2. Objective
To create a beginner-level program that accepts a URL, checks selected warning signs, and displays a risk score with understandable reasons.

## 3. Tools and technologies
- Python 3
- Python standard library (`re`, `urllib.parse`, `unittest`)
- Git and GitHub for version control and project hosting

## 4. Methodology
The program accepts a URL and parses its components. It then checks for selected indicators: HTTP scheme, IP-address hostname, `@` character, excessive URL length, multiple hyphens, suspicious words, and a non-default port. Each detected indicator adds points to a simple score.

## 5. Output
The program displays a risk category, numeric score, and a list of detected indicators. The categories are low risk indicators, potentially suspicious, and high risk.

## 6. Testing
The included unit tests check empty input, HTTP detection, IP-address detection, and a basic HTTPS domain. Run them with `python3 -m unittest -v`.

## 7. Limitations
The tool uses simple rules and cannot confirm that a website is safe or malicious. It may produce false positives and false negatives. It does not open URLs or contact external services.

## 8. Conclusion
PhishGuard demonstrates a basic cybersecurity concept through a working Python program. It provides practice with URL parsing, conditional logic, scoring, and software testing.
