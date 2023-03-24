# CORS-inator 🧪
The CORS-inator is a Python tool that checks a list of URLs for Cross-Origin Resource Sharing (CORS) misconfigurations and generates an HTML report of the results. The report includes information on each URL's vulnerability status and the confidence level of the vulnerability.

# Requirements 🔑

The CORS-inator tool requires Python 3.x and the following Python packages:

    argparse
    csv
    requests

To install the required packages using pip, run the following command in your terminal:

```terminal
pip install argparse csv requests
```

# Installation 🔓
To install the CORS-inator tool, clone this repository.

# Usage 🔫
To use the CORS-inator tool, follow these steps:

1. Create a CSV file containing a list of URLs to check. Each row should contain a single URL.

2. Open a terminal or command prompt and navigate to the directory containing the corsinator.py script.

3. Run the following command:
```python 
corsinator.py INPUT_FILE [-t TIMEOUT]
```
Replace `INPUT_FILE` with the path to your CSV file. The `-t` option specifies the timeout in seconds for the HTTP requests (default: 5 seconds).

4. Wait for the tool to finish checking each URL. The tool will print a message for each URL indicating its status.

5. Once the tool has finished, it will generate an HTML report named report.html in the current directory. The report includes a table with the URL, vulnerability status, and confidence level for each URL.

6. Open the report in a web browser to view the results.

# Conclusion 📖

CORS-inator tool is a simple yet effective way to check for CORS misconfigurations in a list of URLs.
