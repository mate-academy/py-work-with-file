def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    result = 0

    file_data = open(data_file_name, "r")
    content = file_data.readlines()
    file_data.close()

    data_file = [letter.strip("\n") for letter in content]

    for data in data_file:
        name, value = data.split(",")
        if name == "supply":
            supply += int(value)
        elif name == "buy":
            buy += int(value)

    result = supply - buy

    file_data = open(report_file_name, "a")
    file_data.write(f"supply,{supply}\n")
    file_data.write(f"buy,{buy}\n")
    file_data.write(f"result,{result}\n")
    file_data.close()
