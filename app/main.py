def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    input_file = open(data_file_name, "r")
    for line in input_file:
        line = line.strip()
        if line == "":
            continue
        comma_index = line.find(",")
        operation = line[:comma_index]
        amount = int(line[comma_index + 1:])
        if operation == "supply":
            total_supply += amount
        elif operation == "buy":
            total_buy += amount
    input_file.close()

    output_file = open(report_file_name, "w")
    output_file.write("supply," + str(total_supply) + "\n")
    output_file.write("buy," + str(total_buy) + "\n")
    output_file.write("result," + str(total_supply - total_buy) + "\n")
    output_file.close()


create_report("data_file_name.csv", "report_file_name.csv")
