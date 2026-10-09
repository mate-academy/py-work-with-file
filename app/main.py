def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:

        for item in file:
            item = item.strip("\n")
            if not item:
                continue
            pair = item.split(",")
            if pair[0] == "supply":
                result_dict["supply"] += int(pair[1])

            if pair[0] == "buy":
                result_dict["buy"] += int(pair[1])

    result = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as second_file:

        second_file.write(f"supply,{result_dict['supply']}\n")
        second_file.write(f"buy,{result_dict['buy']}\n")
        second_file.write(f"result,{result}\n")
