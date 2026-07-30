def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            po = parts[0].strip()
            if po == "supply":
                supply += int(parts[1].strip())
            elif po == "buy":
                buy += int(parts[1].strip())
    result = supply - buy

    with open(report_file_name, "w", encoding="utf-8") as out:
        out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
