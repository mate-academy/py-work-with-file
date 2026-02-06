def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f, open(report_file_name, "w") as r:
        supply = 0
        buy = 0
        text = f.read()
        items = text.split("\n")
        for item in items:
            pair = item.split(",")
            if pair[0] == "supply":
                supply += int(pair[1])
            elif pair[0] == "buy":
                buy += int(pair[1])
        r.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
