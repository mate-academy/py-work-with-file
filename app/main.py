def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}
    try:
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                line = line.strip().split(",")
                if line[0] == "supply":
                    result_dict["supply"] += int(line[1])
                elif line[0] == "buy":
                    result_dict["buy"] += int(line[1])
            result = result_dict["supply"] - result_dict["buy"]
            str_supply = str(result_dict["supply"])
            str_buy = str(result_dict["buy"])
            str_result = str(result)
            with open(report_file_name, "a") as report_file:
                report_file.write("supply," + str_supply + "\n")
                report_file.write("buy," + str_buy + "\n")
                report_file.write("result," + str_result + "\n")
    except FileNotFoundError:
        return
