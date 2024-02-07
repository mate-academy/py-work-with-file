def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as input_file:
        for line in input_file:
            if len(line) == 0:
                break
            list_value = line.split(",")
            if list_value[0] == "supply":
                total_supply += int(list_value[1])
            elif list_value[0] == "buy":
                total_buy += int(list_value[1])
    result = total_supply - total_buy
    with open(report_file_name, "a") as output_file:
        output_file.write(f"{"supply,"}{total_supply}\n")
        output_file.write(f"{"buy,"}{total_buy}\n")
        output_file.write(f"{"result,"}{result}\n")
