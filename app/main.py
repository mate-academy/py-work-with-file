def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            result2 = line.split(",")
            if result2[0] == "supply":
                supply += int(result2[1])
            if result2[0] == "buy":
                buy += int(result2[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
