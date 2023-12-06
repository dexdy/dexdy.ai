import re
import uuid
import datetime
import os
import requests
import tldextract
import html2text

def get_html_title(url, html_content):
    match = re.search('<title>(.*?)</title>', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        # Constructing a fallback title from the URL
        return url.split('/')[-1].replace('-', ' ').replace('_', ' ').title()

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
    frontmatter = (
        "---\n"
        f"id: {uuid.uuid4()}\n"
        f"title: {title} ({full_domain})\n"
        f"updated: {now}\n"
        f"created: {now}\n"
        "---\n\n"
    )
    url_line = f"URL :: {url}\n\n"
    return frontmatter + url_line + markdown_content

def main():
    try:
        url = input("Enter the URL of the page: ")
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
        except requests.RequestException:
            html_content = ""
        
        title = get_html_title(url, html_content)
        extracted = tldextract.extract(url)
        domain = extracted.domain
        suffix = extracted.suffix
        subdomain = extracted.subdomain

        # Forming full domain excluding 'www'
        full_domain = '.'.join(part for part in [subdomain, domain, suffix] if part and part != "www")

        print("Enter HTML content (press Ctrl+D to end input):")
        html_content_user = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            html_content_user.append(line)
        html_content_user = "\n".join(html_content_user)
        markdown_content = html2text.html2text(html_content_user) if html_content_user else ""

        file_name = create_note_filename(url, title)
        content = create_note_content(url, title, markdown_content, full_domain)
        
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"File created: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

