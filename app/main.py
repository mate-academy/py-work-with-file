def create_report(data_file_name: str, report_file_name: str) -> None:
    source_file = open(data_file_name, "r")
    target_file = open(report_file_name, "w")

    supply = 0
    buy = 0
    for line in source_file.readlines():
        value = int(line.split(",")[1])
        if "supply" in line:
            supply += value
        if "buy" in line:
            buy += value
    target_file.write(f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{supply - buy}\n")

    source_file.close()
    target_file.close()
