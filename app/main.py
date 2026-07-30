def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name, "r")
    buy = 0
    supply = 0
    for line in file_data.readlines():
        temp = line.strip().split(",")
        if temp[0] == "buy":
            buy += int(temp[1])
        else:
            supply += int(temp[1])
    result = supply - buy
    file_data.close()

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
