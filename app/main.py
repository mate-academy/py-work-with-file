def create_report(data_file_name: str, report_file_name: str) -> None:
    result_data = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as file_read:
        file_data = file_read.read().replace("\n", ",").split(",")
        for index, key in enumerate(file_data):
            if key == "supply":
                result_data["supply"] += int(file_data[index + 1])
            if key == "buy":
                result_data["buy"] += int(file_data[index + 1])
        result_data["result"] = result_data["supply"] - result_data["buy"]

    with open(report_file_name, "w") as file_write:
        file_write.write(
            f"supply,{result_data['supply']}\n"
            f"buy,{result_data['buy']}\n"
            f"result,{result_data['result']}\n"
        )
