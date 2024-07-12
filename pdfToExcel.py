import fitz
import pandas as pd

doc = fitz.open("catalog.pdf")

all_tables = []

for page_num in range(len(doc)):
    page = doc[page_num]

    tabs = page.find_tables()

    for tab_index, tab in enumerate(tabs):
     
        table_data = [line for line in tab.extract()]

       
        table_bbox = tab.bbox
        top_margin = table_bbox[1] - 50 

        text_above_table = ""
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if span["bbox"][3] < table_bbox[1] and span["bbox"][3] > top_margin:
                        text_above_table = span["text"]
                        break

        table_data.insert(0, [text_above_table] + [''] * (len(table_data[0]) - 1))

        df = pd.DataFrame(table_data[1:], columns=table_data[0])

        all_tables.append((page_num, tab_index, df))

with pd.ExcelWriter("extracted_tables_with_headers.xlsx") as writer:
    for page_num, tab_index, df in all_tables:
        sheet_name = f"Page{page_num+1}_Table{tab_index+1}"
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("All tables and headers saved to extracted_tables_with_headers.xlsx")
