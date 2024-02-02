def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            if len(line) > 0:
                if line.split(",")[0] == "supply":
                    supply += int(line.split(",")[1])
                if line.split(",")[0] == "buy":
                    buy += int(line.split(",")[1])
        report_file.write(f"supply,{supply}\nbuy,{buy}\n"
                          f"result,{supply - buy}\n")
