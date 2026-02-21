from openpyxl import Workbook


def create_messy_excel(filename="messy_data.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Plant Data"

    # -----------------------------
    # Title / Metadata rows
    # -----------------------------
    ws.append(["ABC Power Plant - Daily Performance Report"])
    ws.append(["Generated on: 2026-02-21"])
    ws.append([])
    ws.append(["Confidential Document"])
    ws.append([])

    # -----------------------------
    # Messy Headers (abbreviations, typos, assets inside)
    # -----------------------------
    headers = [
        "COAL CONSMPTN AFBC1",     # typo
        "Steam (Boiler 2)",        # alternate asset naming
        "Eff %",                   # abbreviated
        "Power TG1",               # asset reference
        "Coal Used (MT)",          # fuzzy variant
        "YES/NO Flag",             # boolean column
        "Random Notes"             # unmapped column
    ]

    ws.append(headers)

    # -----------------------------
    # Mixed Format Data Rows
    # -----------------------------
    data = [
        ["1,200", "50", "90%", "5,000", "1300", "YES", "Normal"],
        ["1,150.50", "48", "0.88", "4,800", "1,250", "NO", "Minor delay"],
        ["-500", "47", "105%", "4,700", "N/A", "YES", "Sensor issue"],
        ["1,300", "49", "92%", "4,900", "1400", "", ""],
        ["N/A", "50", "85%", "5,100", "1350", "YES", "Maintenance"],
        ["1,100", "", "89%", "4,850", "1250", "NO", None],
    ]

    for row in data:
        ws.append(row)

    wb.save(filename)
    print(f"Messy test file created: {filename}")


if __name__ == "__main__":
    create_messy_excel()