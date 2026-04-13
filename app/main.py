def create_report(data_file_name: str, report_file_name: str) -> None:
    tab_out = {}

    with open(data_file_name) as f:
        for line in f.readlines():
            row = line.split(",")
            tab_out[row[0]] = tab_out.get(row[0], 0) + int(row[1])

    tab_out["result"] = tab_out.get("supply", 0) - tab_out.get("buy", 0)

    with open(report_file_name, "w") as f:
        for key in ("supply", "buy", "result"):
            f.write(f"{key},{tab_out.get(key, 0)}\n")
