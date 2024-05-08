import os
import requests
from bs4 import BeautifulSoup
import pdfkit


def fetch_webpage(url):
    response = requests.get(url)
    return response.text


def save_as_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def convert_html_to_pdf(html_file, pdf_file):
    pdfkit.from_file(html_file, pdf_file)


def get_subpage_urls(url):
    subpage_urls = []
    html_content = fetch_webpage(url)
    soup = BeautifulSoup(html_content, 'html.parser')

    for link in soup.find_all('a'):
        subpage_url = link.get('href')
        if subpage_url and subpage_url.startswith('http'):
            subpage_urls.append(subpage_url)

    return subpage_urls


def main():
    base_url = 'https://example.com'  # 替换为你要抓取的网站的基本 URL
    output_dir = 'html_files'  # 保存 HTML 文件的目录
    pdf_dir = 'pdf_files'  # 保存 PDF 文件的目录

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    subpage_urls = get_subpage_urls(base_url)

    for url in subpage_urls:
        html_content = fetch_webpage(url)
        filename = url.split('/')[-1] + '.html'
        html_file = os.path.join(output_dir, filename)
        save_as_html(html_content, html_file)

        pdf_file = os.path.join(pdf_dir, filename[:-5] + '.pdf')
        convert_html_to_pdf(html_file, pdf_file)

        print(f'Converted {url} to {pdf_file}')


if __name__ == '__main__':
    main()