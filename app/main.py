def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name) as data_file:
        for line in data_file:
            if line != "":
                if line.split(",")[0] == "buy":
                    buy += int(line.split(",")[1])
                else:
                    supply += int(line.split(",")[1])
    with open(report_file_name, "wt") as report_file:
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
