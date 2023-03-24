import argparse
import csv
import requests
from urllib.parse import urlparse
import matplotlib.pyplot as plt

# Constants
VULNERABLE_HEADERS = [
    'Access-Control-Allow-Origin',
    'Access-Control-Allow-Methods',
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Credentials'
]


def check_cors_vulnerability(url, timeout):
    """Checks if the specified URL has a CORS vulnerability."""
    headers = requests.head(url, timeout=timeout).headers
    is_vulnerable = False
    for header in VULNERABLE_HEADERS:
        if header in headers:
            is_vulnerable = True
            break
    return is_vulnerable, confidence_level(headers)


def confidence_level(headers):
    """Calculates the confidence level of the vulnerability's existence."""
    num_vulnerable_headers = 0
    for header in VULNERABLE_HEADERS:
        if header in headers:
            num_vulnerable_headers += 1
    return round(num_vulnerable_headers / len(VULNERABLE_HEADERS), 2)


def generate_report(data, timeout):
    """Generates an HTML report with the results of checking the specified URLs for CORS vulnerabilities."""
    report = "<html><head><style>table, th, td {border: 1px solid black;}</style></head><body><h2>CORS Vulnerability Report | CORS-inator by theAce</h2><table><tr><th>URL</th><th>Is Vulnerable</th><th>Confidence Level</th></tr>"
    for row in data:
        url = row[0]
        if not url.startswith('http'):
            url = 'https://' + url
        is_vulnerable, confidence = check_cors_vulnerability(url, timeout)
        report += f"<tr><td>{url}</td><td>{is_vulnerable}</td><td>{confidence}</td></tr>"
    report += "</table></body></html>"
    num_vulnerable = sum(1 for row in data if row[-2])
    num_non_vulnerable = len(data) - num_vulnerable
    report += f"<p>Number of vulnerable URLs: {num_vulnerable}</p>"
    report += f"<p>Number of non-vulnerable URLs: {num_non_vulnerable}</p>"
    # Create bar chart
    labels = ['Vulnerable', 'Non-vulnerable']
    counts = [num_vulnerable, num_non_vulnerable]
    fig, ax = plt.subplots()
    ax.bar(labels, counts)
    ax.set_title('CORS Vulnerability Report')
    ax.set_ylabel('Number of URLs')
    # Save chart to file
    chart_filename = 'chart.png'
    plt.savefig(chart_filename)
    # Embed chart in report
    report += f"<img src='{chart_filename}'/>"
    return report


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='CORS-inator by theAce')
    parser.add_argument('input', metavar='INPUT', help='path to input CSV file')
    parser.add_argument('-t', metavar='TIMEOUT', type=int, default=5, help='timeout in seconds (default: 5)')
    args = parser.parse_args()

    # Load data from CSV file
    with open(args.input, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    # Check each URL for CORS vulnerability
    for i, row in enumerate(data):
        url = row[0]
        if not url.startswith('http'):
            url = 'https://' + url
        print(f"Checking {url} ({i+1}/{len(data)})")
        is_vulnerable, confidence = check_cors_vulnerability(url, timeout=args.t)
        row.append(is_vulnerable)
        row.append(confidence)

    # Generate report
    report = generate_report(data, args.t)

    # Write report to file
    with open('report.html', 'w') as f:
        f.write(report)

    print("Aced! Report saved to report.html")


if __name__ == '__main__':
    main()
