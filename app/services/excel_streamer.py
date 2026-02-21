from openpyxl import load_workbook
from tempfile import NamedTemporaryFile
from app.services.header_detect import detect_header_row
from app.services.llm_mapper import map_headers_with_llm
from app.services.chunk_processor import process_chunks

async def process_excel(upload_file):
    # Save temp file
    with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        content = await upload_file.read()
        tmp.write(content)
        tmp_path = tmp.name

    # Load in streaming mode
    wb = load_workbook(tmp_path, read_only=True)
    ws = wb.active

    # Detect header row
    header_row_index, headers = detect_header_row(ws)
    header_row_index, headers = detect_header_row(ws)

    llm_mapping = map_headers_with_llm(headers)

    result = process_chunks(ws, header_row_index, headers, llm_mapping)

    return result