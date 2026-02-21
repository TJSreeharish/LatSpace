def parse_value(raw):
    if raw is None:
        return None

    s = str(raw).strip()

    if s.upper() in ["N/A", "NA", "NULL", ""]:
        return None

    if s.upper() in ["YES", "TRUE"]:
        return 1.0

    if s.upper() in ["NO", "FALSE"]:
        return 0.0

    if "%" in s:
        try:
            return float(s.replace("%", "").replace(",", "")) / 100
        except:
            return None

    try:
        return float(s.replace(",", ""))
    except:
        return None