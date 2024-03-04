def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0
    with open(data_file_name, "r") as read_file:

        temp_string = read_file.read()
        string_list = temp_string.split("\n")

        for line in string_list:
            list_line = line.split(",")
            if list_line[0] == "supply":
                supply_sum += int(list_line[1])
            elif list_line[0] == "buy":
                buy_sum += int(list_line[1])

        result = supply_sum - buy_sum
        message = f"supply,{supply_sum}\nbuy,{buy_sum}\nresult,{result}\n"

    with open(report_file_name, "w") as write_file:
        write_file.write(message)
