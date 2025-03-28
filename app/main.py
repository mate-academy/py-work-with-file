def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with (open(data_file_name, "r") as file_from,
          open(report_file_name, "w") as file_to):
        for line in file_from:
            line = line.strip().split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])
        file_to.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
