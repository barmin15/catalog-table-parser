
# Catalog Table Parser

This project contains python scripts to read pdfs tables (mostly for catalogs) and parse them into the selected format.

### excel preview
![alt text](https://github.com/barmin15/catalog-table-parser/blob/main/result_images/xlsx_result.png?raw=true)

### Html preview
![alt text](https://github.com/barmin15/catalog-table-parser/blob/main/result_images/html_result.png?raw=true)
## File Structure

```
├── extracted_files/
│ ├── index.html
│ └── extracted_tables_with_headers.xlsx
├── result_images/
├── html_result.png
│ ├── xlsx_result.png
│ └── html_result.png
├── catalog.pdf
├── pdfToExcel.py
├── pdfToHtml.py
├── README.md
├── style.css
```
## Setup

1. Clone the repository or download the files to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required packages:

    ### Packages

    run the following command to install the required packages
    
    for html parser

    ```
    pip install pdfplumber pandas beautifulsoup4
    ```

    for excel parser 

    ```
    pip install fitz pandas
    ```
## Code Explanation

### pdfToExcel.py

1. This file uses `fitz` to read, and iterate over the pages in the pdf file. With the help of the `find_tables` built in method, we look for table structures, and extract all the data from the table cells. After the table data is extracted, we look for the title for the table above the by finding the first text element before the table. 

2. After the data is extracted, be insert it into the excel using `panda`.

3. we save the excel with the given name `extracted_tables_with_headers.xlsx`.

### pdfToHtml.py

1. We open the pdf using `pdfplumber` and iterate over the data.

2. We create a html structure, and apppend the pdf data into Html table tags, inside the Html. 

3. We save the Html file with the given name `index.html`.