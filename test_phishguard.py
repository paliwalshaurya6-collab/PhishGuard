import unittest
from phishguard import analyze_url

class PhishGuardTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(analyze_url("")["level"], "Invalid input")

    def test_http_is_flagged(self):
        result = analyze_url("http://example.com")
        self.assertIn("Uses HTTP rather than HTTPS.", result["reasons"])

    def test_ip_address_is_flagged(self):
        result = analyze_url("http://192.168.1.10/login")
        self.assertTrue(any("IP address" in reason for reason in result["reasons"]))

    def test_https_domain_has_low_indicators(self):
        result = analyze_url("https://example.com")
        self.assertEqual(result["level"], "Low risk indicators")

if __name__ == "__main__":
    unittest.main()
