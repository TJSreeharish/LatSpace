def detect_header_row(ws, max_scan=10):
    best_row = None
    best_score = 0

    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i >= max_scan:
            break

        non_empty = sum(1 for cell in row if cell is not None)
        if non_empty > best_score:
            best_score = non_empty
            best_row = (i, row)

    header_index, header_row = best_row
    headers = [str(cell).strip() if cell else "" for cell in header_row]

    return header_index, headers