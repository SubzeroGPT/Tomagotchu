import os
import requests
from bs4 import BeautifulSoup

class BigBankLittleBankAdvanced:
    def __init__(self, target_url):
        self.target_url = target_url
        self.mirror_directory = "mirrored_site"

    def mirror_site(self):
        print("[*] Mirroring the website...")
        os.system(f"wget --mirror --convert-links --adjust-extension --page-requisites --no-parent -P {self.mirror_directory} {self.target_url}")

    def static_analysis(self):
        # Python-specific with Bandit
        print("[*] Running static code analysis with Bandit...")
        result = os.popen(f"bandit -r {self.mirror_directory}").read()
        print(result)

        # Assuming SonarQube is pre-configured
        print("[*] Running static code analysis with SonarQube...")
        os.system(f"sonar-scanner -Dsonar.projectKey=BBLB -Dsonar.sources={self.mirror_directory}")

    def dynamic_analysis(self):
        print("[*] Running dynamic analysis with OWASP ZAP...")
        # Placeholder. Replace with ZAP command or API call.

    def sql_injection_check(self):
        print("[*] Running SQLmap for potential SQL injection points...")
        os.system(f"sqlmap -u {self.target_url} --batch")

    def fuzz_test(self):
        print("[*] Fuzz testing the website...")
        # Placeholder. Replace with fuzzing logic or tool command.

    def chat_with_gpt3(self, prompt_text):
        OPENAI_API_URL = "https://api.openai.com/v2/engines/davinci/completions"
        HEADERS = {
            "Authorization": f"Bearer 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",
            "Content-Type": "application/json",
        }
        data = {
            "prompt": prompt_text,
            "max_tokens": 150
        }
        response = requests.post(OPENAI_API_URL, headers=HEADERS, json=data)
        message_content = response.json().get("choices")[0].get("text").strip()
        return message_content

    def fetch_cve_details(self, cve_id):
        url = f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        cve_summary = soup.find("div", {"id": "GeneratedTable"}).text.strip()
        return cve_summary

    def analyze_vulnerability(self, vulnerability_name):
        gpt_response = self.chat_with_gpt3(f"Tell me more about {vulnerability_name} vulnerability.")
        print(f"GPT-3 says: {gpt_response}")

        if "CVE-" in gpt_response:
            cve_id = gpt_response.split("CVE-")[1].split()[0]
            cve_details = self.fetch_cve_details(cve_id)
            print(f"CVE Details: {cve_details}")

    def run(self):
        self.mirror_site()
        self.static_analysis()
        self.dynamic_analysis()
        self.sql_injection_check()
        self.fuzz_test()
        # As an example, we'll analyze a vulnerability called "SQL Injection"
        # Replace with actual vulnerabilities found.
        self.analyze_vulnerability("SQL Injection")

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    tool = BigBankLittleBankAdvanced(target_url)
    tool.run()
