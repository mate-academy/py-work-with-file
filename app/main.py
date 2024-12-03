def create_report(data_file_name: str, report_file_name: str) -> None:
    file1 = open(data_file_name, "r")

    data_file = {"supply": 0, "buy": 0}
    for line in file1.readlines():
        text, value = line.split(",")
        if text == "supply":
            data_file["supply"] += int(value)
        elif text == "buy":
            data_file["buy"] += int(value)

    file1.close()
    file2 = open(report_file_name, "w")
    for text, value in data_file.items():
        file2.write(f"{text},{value}\n")
    file2.write(f"result,{data_file["supply"] - data_file["buy"]}\n")
