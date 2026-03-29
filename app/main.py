def create_report(data_file_name: str, report_file_name: str) -> None:
    first_file = open(data_file_name, "r")
    supply_list = []
    buy_list = []
    for line in first_file:
        list_line = line.split(",")
        if list_line[0] == "supply":
            supply_list.append(int(list_line[1]))
        elif list_line[0] == "buy":
            buy_list.append(int(list_line[1]))

    sum_s = sum(supply_list)
    sum_b = sum(buy_list)
    result = sum_s - sum_b
    first_file.close()
    second_file = open(report_file_name, "w")
    second_file.write("supply")
    second_file.write(",")
    second_file.write(str(sum_s))
    second_file.write("\nbuy")
    second_file.write(",")
    second_file.write(str(sum_b))
    second_file.write("\nresult")
    second_file.write(",")
    second_file.write(str(result))
    second_file.write("\n")
    second_file.close()
