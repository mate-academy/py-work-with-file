def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            if not line.strip():
                continue
            info = line.strip().split(",")
            if info[0] == "buy":
                buy += int(info[1])
            elif info[0] == "supply":
                supply += int(info[1])
    with open(report_file_name, "w") as f:
        text = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        f.write(text)
