import sys
import re
import uuid
import datetime
import os
import requests
import tldextract
import html2text

def get_html_title(html_content):
    match = re.search('<title>(.*?)</title>', html_content, re.IGNORECASE)
    return match.group(1).strip() if match else 'Unknown Title'

def create_note_filename(url, title):
    extracted = tldextract.extract(url)
    domain = extracted.domain
    suffix = extracted.suffix.replace('.', '-')
    subdomain = extracted.subdomain

    # Excluding 'www' subdomain from filename
    subdomain_part = "" if subdomain == "www" else f".{subdomain}"

    domain_part = f"{domain}-{suffix}" if suffix else domain
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    base_filename = f"notes/lib.web.{domain_part}{subdomain_part}.{slug}"

    # Adding a suffix if the file already exists
    filename = base_filename + ".md"
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_filename}-{counter}.md"
        counter += 1

    return filename

def create_note_content(url, title, markdown_content, full_domain):
    now = int(datetime.datetime.now().timestamp() * 1000)
    content = (
        "---\n"
        f"id: {uuid.uuid4()}\n"
        f"title: {title} ({full_domain})\n"
        f"updated: {now}\n"
        f"created: {now}\n"
        f"url: {url}\n"
        "---\n\n"
    )
    return content + markdown_content if markdown_content else content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/create.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        extracted = tldextract.extract(url)
        domain = extracted.domain
        suffix = extracted.suffix
        subdomain = extracted.subdomain

        # Forming full domain excluding 'www'
        full_domain = '.'.join(part for part in [subdomain, domain, suffix] if part and part != "www")

        html_content = sys.stdin.read() if not sys.stdin.isatty() else requests.get(url).text
        title = get_html_title(html_content)
        markdown_content = html2text.html2text(html_content) if not sys.stdin.isatty() else ""

        file_name = create_note_filename(url, title)
        content = create_note_content(url, title, markdown_content, full_domain)
        
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"File created: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

