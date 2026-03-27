def create_report(data_file_name: str
                  , report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as reader:
        for data in reader:
            split_data = data.split(",")
            if split_data[0] == "supply":
                supply += int(split_data[1])
            elif split_data[0] == "buy":
                buy += int(split_data[1])
        result = supply - buy
    with open(report_file_name, "w") as writer:
        writer.writelines("supply," + str(supply) + "\n")
        writer.writelines("buy," + str(buy) + "\n")
        writer.writelines("result," + str(result) + "\n")
