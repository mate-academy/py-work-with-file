def create_report(data_file_name: str, report_file_name: str) -> None:

    result = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        for line in file:
            list_items = line.split(",")
            result[list_items[0]] += int(list_items[1].strip("\n"))

    with open(report_file_name, "w") as new_file:
        new_file.write("supply," + str(result["supply"]) + "\n"
                       + "buy," + str(result["buy"]) + "\n"
                       + "result," + str(result["supply"] - result["buy"])
                       + "\n")
