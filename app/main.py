def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as read_data:
        for line in read_data.readlines():
            word = line.strip().split(",")
            data = {word[0]: int(word[1])}
            for operation, amount in data.items():
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
        result = supply - buy

    with open(report_file_name, "w") as write_result:
        write_result.write("supply" + "," + str(supply) + "\n")
        write_result.write("buy" + "," + str(buy) + "\n")
        write_result.write("result" + "," + str(result) + "\n")
