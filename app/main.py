def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as f:
        for line in f:
            value = line.split(",")
            if value[0] == "supply":
                supply += int(value[1])
            else:
                buy += int(value[1])
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
        f.close()
