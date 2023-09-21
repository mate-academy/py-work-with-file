def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as file1,
          open(report_file_name, "w") as file2):
        for line in file1:
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])
        file2.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
