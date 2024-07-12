import pdfplumber
import pandas as pd
from bs4 import BeautifulSoup

def extract_table_from_pdf(pdf_path):
    
    with pdfplumber.open(pdf_path) as pdf:
        data = []
        
        for page in pdf.pages:
          
            tables = page.extract_tables()
            for table in tables:
                data.extend(table)
        return data

def pdf_table_to_html(pdf_path, html_path):
  
    data = extract_table_from_pdf(pdf_path)
    
    
    df = pd.DataFrame(data)
    
    html_table = df.to_html(index=False, header=False, border=0, classes='table table-bordered')
    
    soup = BeautifulSoup("<html><head></head><body></body></html>", "html.parser")
    body = soup.body
    
    body.append(BeautifulSoup(html_table, "html.parser"))
    
    with open(html_path, "w", encoding="utf-8") as file:
        file.write(str(soup.prettify()))

pdf_path = "catalog.pdf"  
html_path = "index.html" 
pdf_table_to_html(pdf_path, html_path)
