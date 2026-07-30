def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as f:
        for line in f:
            if line == "":
                break
            line = line.split(",")
            if line[0] == "buy":
                buy += int(line[1])
            elif line[0] == "supply":
                supply += int(line[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
