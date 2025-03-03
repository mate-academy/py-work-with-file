def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    first_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in first_file:
        if line.split(",")[0] == "supply":
            supply += int(line.split(",")[1])
        else:
            buy += int(line.split(",")[1])
    first_file.close()
    result = supply - buy
    second_file = open(report_file_name, "w")
    second_file.write(f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{result}\n")
    second_file.close()
