def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name, "r")
    report_f = open(report_file_name, "w")
    totals = {}

    for line in read_file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 2:
            continue
        [key, value] = parts
        if key in totals:
            totals[key] += int(value)
        else:
            totals[key] = int(value)

    totals["result"] = totals["supply"] - totals["buy"]
    for key in ("supply", "buy", "result"):
        report_f.write(f"{key},{totals.get(key, 0)}\n")

    read_file.close()
    report_f.close()
