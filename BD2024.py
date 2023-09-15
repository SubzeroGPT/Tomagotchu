import requests
import time
import openai

# Initializing ChatGPT API
openai.api_key = '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'

class BD2024:

    def __init__(self):
        self.target_url = ""
        self.base_url = "http://localhost:8080"

    def banner(self):
        print("################################")
        print("#         BD2024 - v2.0        #")
        print("#  Ethical Hacking Toolkit     #")
        print("################################")
        print()

    def set_target(self):
        self.target_url = input("Enter target URL: ")

    def chat_gpt_query(self, query):
        response = openai.Completion.create(prompt=query, max_tokens=150)
        return response.choices[0].text.strip()

    def zap_spider_url(self):
        print("Spidering target...")
        spider_url = f"{self.base_url}/JSON/spider/action/scan/?url={self.target_url}"
        requests.get(spider_url)
        time.sleep(10)

    def zap_start_scan(self):
        print("Starting ZAP scan...")
        scan_url = f"{self.base_url}/JSON/ascan/action/scan/?url={self.target_url}&recurse=true"
        requests.get(scan_url)

    def zap_scan_status(self):
        status_url = f"{self.base_url}/JSON/ascan/view/status/?baseurl={self.target_url}"
        status = requests.get(status_url).json()['status']
        while int(status) < 100:
            print(f"Scan progress: {status}%")
            time.sleep(10)
            status = requests.get(status_url).json()['status']
        print("Scan completed!")

    def zap_fetch_results(self):
        report_url = f"{self.base_url}/JSON/core/view/alerts/?baseurl={self.target_url}&endurl={self.target_url}&riskId=0"
        results = requests.get(report_url).json()
        return results

    def save_report(self, report_content):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        with open(f"scan_report_{timestamp}.txt", "w") as file:
            file.write(str(report_content))
        print(f"Report saved as scan_report_{timestamp}.txt")

    def run(self):
        self.banner()
        mode = input("Choose a mode (express/advanced/full): ").lower()
        self.set_target()

        if mode == "express":
            self.zap_spider_url()
            self.zap_start_scan()
            self.zap_scan_status()
            results = self.zap_fetch_results()
            exploit_info = self.chat_gpt_query("Provide exploit details for: " + str(results))
            print(exploit_info)
            self.save_report(results)

        elif mode == "advanced":
            # Incorporate additional tools or deeper scans here
            pass

        elif mode == "full":
            # Incorporate all tools for a comprehensive assessment
            pass

        else:
            print("Invalid mode selected!")

if __name__ == "__main__":
    app = BD2024()
    app.run()
