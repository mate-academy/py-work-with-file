def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as first:
        save = first.read()
        save = save.replace("\n", ",")
        value = save.split(",")
        for num, operation in enumerate(value):
            if operation == "supply":
                result_dict["supply"] += int(value[num + 1])
            if operation == "buy":
                result_dict["buy"] += int(value[num + 1])
        result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as second:
        second.write(
            f'supply,{result_dict["supply"]}\n'
            f'buy,{result_dict["buy"]}\n'
            f'result,{result_dict["result"]}\n'
        )
