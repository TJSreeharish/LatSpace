from openpyxl import Workbook
import random


def random_percentage():
    base = random.randint(85, 95)
    # Occasionally inject bad efficiency
    if random.random() < 0.05:
        return f"{random.randint(101,110)}%"
    return f"{base}%"


def random_coal():
    value = random.randint(1100, 1500)
    # Occasionally inject negative
    if random.random() < 0.05:
        return str(-random.randint(100, 500))
    return f"{value:,}"


def random_power():
    return f"{random.randint(4800, 5200):,}"


def random_steam():
    return str(random.randint(45, 55))


def random_remark():
    remarks = [
        "Normal",
        "Stable",
        "Minor fluctuation",
        "Check AFBC-1",
        "",
        None
    ]
    return random.choice(remarks)


def create_multi_asset_excel(filename="multi_asset.xlsx", num_rows=50):
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
    # Generate Random Data
    # -----------------------------
    for _ in range(num_rows):
        row = [
            random_coal(),
            random_coal(),
            random_coal(),
            random_steam(),
            random_steam(),
            random_power(),
            random_power(),
            random_percentage(),
            random_percentage(),
            random_remark()
        ]
        ws.append(row)

    wb.save(filename)
    print(f"Multi-asset test file created with {num_rows} rows: {filename}")


if __name__ == "__main__":
    create_multi_asset_excel(num_rows=50)