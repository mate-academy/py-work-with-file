def create_report(data_file_name: str, report_file_name: str) -> str:
    with open(data_file_name, "r") as data_file:
        report = open(report_file_name, "a")
        data_list = [element for element in data_file.readlines()]
        supply_list = [element for element
                       in data_list if element[:6] == "supply"]
        buy_list = [element for element
                    in data_list if element[:3] == "buy"]
        supply_sum = sum([int(element[7:-1])
                          for element in supply_list])
        buy_sum = sum([int(element[4:-1])
                       for element in buy_list])
        result = supply_sum - buy_sum
        report.write((f"supply, {supply_sum}\n"
                     f"buy, {buy_sum}\n"
                     f"result, {result}\n").replace(" ", ""))
        report.close()
