def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            if "supply" in line:
                supply += int(line.replace("\n", "").split(",")[1])
            if "buy" in line:
                buy += int(line.replace("\n", "").split(",")[1])
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
