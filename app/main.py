def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    new_text = {}
    with open(data_file_name, "r") as data_file:
        for item in data_file.readlines():
            item_list = item.split(",")
            key = item_list[0]
            number = int(item_list[1].replace("\n", ""))

            if key not in new_text:
                new_text[key] = number
            else:
                new_text[key] += number

    with open(report_file_name, "w") as report_file:
        result = new_text["supply"] - new_text["buy"]

        report_file.write(f"supply,{new_text['supply']}\n")
        report_file.write(f"buy,{new_text['buy']}\n")
        report_file.write(f"result,{result}\n")
