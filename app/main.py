def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_of_report = {"supply": 0, "buy": 0}
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        for line in file_in:
            list_of_information = line.split(",")
            if list_of_information[0] == "supply":
                dict_of_report["supply"] += int(list_of_information[1])
            if list_of_information[0] == "buy":
                dict_of_report["buy"] += int(list_of_information[1])
        dict_of_report["result"] = (
            dict_of_report["supply"] - dict_of_report["buy"]
        )

        file_out.write(
            f"supply,{dict_of_report['supply']}\n"
            f"buy,{dict_of_report['buy']}\n"
            f"result,{dict_of_report['result']}\n"
        )
