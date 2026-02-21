from openpyxl import Workbook


def create_multi_asset_excel(filename="multi_asset.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Multi Asset Data"

    # -----------------------------
    # Title / Metadata rows
    # -----------------------------
    ws.append(["ABC Power Plant - Multi Asset Daily Report"])
    ws.append(["Generated on: 2026-02-21"])
    ws.append([])
    ws.append(["All Units Operational"])
    ws.append([])

    # -----------------------------
    # Multi-Asset Headers
    # -----------------------------
    headers = [
        "Coal Consumption AFBC-1",
        "Coal Consumption AFBC-2",
        "Coal Used (MT) TG-1",
        "Steam AFBC-1",
        "Steam AFBC-2",
        "Power TG-1",
        "Power TG-2",
        "Eff % AFBC-1",
        "Eff % AFBC-2",
        "Remarks"
    ]

    ws.append(headers)

    # -----------------------------
    # Data Rows
    # -----------------------------
    data = [
        ["1,200", "1,150", "1300", "50", "48", "5,000", "4,800", "90%", "88%", "Normal"],
        ["1,300", "1,180", "1400", "52", "49", "5,100", "4,900", "92%", "89%", "Stable"],
        ["-400", "1,200", "1500", "51", "50", "5,050", "4,950", "105%", "87%", "Check AFBC-1"],
        ["1,250", "1,170", "1350", "49", "47", "4,980", "4,820", "89%", "86%", ""],
    ]

    for row in data:
        ws.append(row)

    wb.save(filename)
    print(f"Multi-asset test file created: {filename}")


if __name__ == "__main__":
    create_multi_asset_excel()