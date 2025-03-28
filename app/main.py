def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dct = {}
    with open(data_file_name, "r") as data_file:
        content = str(data_file.read()).strip()
    content_list = [elem.split(",") for elem in content.split("\n")]
    for key, value in content_list:
        result_dct[key] = result_dct.get(key, 0) + int(value)
    result_dct["result"] = result_dct["supply"] - result_dct["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{result_dct['supply']}\n"
            f"buy,{result_dct['buy']}\n"
            f"result,{result_dct['result']}\n"
        )
