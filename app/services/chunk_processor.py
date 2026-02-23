from app.services.value_parser import parse_value


def process_chunks(ws, header_row_index, headers, llm_mapping, chunk_size=500):
    parsed_data = []
    unmapped_columns = []
    warnings = []
    human_review_required = []

    column_mapping = {}

    # Build mapping from LLM output
    for item in llm_mapping:
        column_mapping[item["column_index"]] = {
            "param_name": item.get("param_name"),
            "asset_name": item.get("asset_name"),
            "confidence": item.get("confidence", "low")
        }

    # Detect unmapped columns
    for idx in range(len(headers)):
        if idx not in column_mapping:
            unmapped_columns.append({
                "column_index": idx,
                "column_name": headers[idx]
            })

    current_chunk = []

    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i <= header_row_index:
            continue

        current_chunk.append((i, row))

        if len(current_chunk) >= chunk_size:
            chunk_results, chunk_warnings, chunk_review = process_chunk(
                current_chunk, column_mapping
            )
            parsed_data.extend(chunk_results)
            warnings.extend(chunk_warnings)
            human_review_required.extend(chunk_review)
            current_chunk = []

    if current_chunk:
        chunk_results, chunk_warnings, chunk_review = process_chunk(
            current_chunk, column_mapping
        )
        parsed_data.extend(chunk_results)
        warnings.extend(chunk_warnings)
        human_review_required.extend(chunk_review)

    return {
        "status": "success",
        "header_row": header_row_index,
        "parsed_data": parsed_data,
        "unmapped_columns": unmapped_columns,
        "warnings": warnings,
        "human_review_required": human_review_required
    }


def process_chunk(chunk, column_mapping):
    results = []
    warnings = []
    human_review_required = []

    for row_index, row in chunk:
        for col_index, cell in enumerate(row):
            mapping = column_mapping.get(col_index)

            if not mapping:
                continue

            param_name = mapping.get("param_name")
            asset_name = mapping.get("asset_name")
            confidence = mapping.get("confidence", "low")

            parsed = parse_value(cell)

            entry = {
                "row": row_index,
                "col": col_index,
                "param_name": param_name,
                "asset_name": asset_name,
                "raw_value": cell,
                "parsed_value": parsed,
                "confidence": confidence
            }

            # Validation Rules
            if parsed is not None:

                # Coal consumption cannot be negative
                if param_name == "coal_consumption" and parsed < 0:
                    warnings.append({
                        "row": row_index,
                        "param_name": param_name,
                        "issue": "Negative coal consumption"
                    })

                # Efficiency must be <= 1 (100%)
                if param_name == "efficiency" and parsed > 1:
                    warnings.append({
                        "row": row_index,
                        "param_name": param_name,
                        "issue": "Efficiency greater than 100%"
                    })

            # Human Review Rule
            if param_name is None:
                human_review_required.append(entry)

            elif confidence == "low":
                human_review_required.append(entry)

            else:
                results.append(entry)

    return results, warnings, human_review_required