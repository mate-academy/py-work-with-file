def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as file_read:
        for line in file_read:
            key, value = line.strip().split(",")
            data[key] += int(value)
    with open(report_file_name, "a") as file_write:
        supply = "supply," + str(data["supply"]) + "\n"
        buy = "buy," + str(data["buy"]) + "\n"
        result = "result," + str(data["supply"] - data["buy"]) + "\n"
        file_write.write(supply)
        file_write.write(buy)
        file_write.write(result)
