def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        file_lines = [
            item.rstrip("\n").split(",") for item in file.readlines()
        ]
        result_dict = {}
        for item in file_lines:
            if item[0]:
                if item[0] not in result_dict:
                    result_dict[item[0]] = int(item[1])
                else:
                    result_dict[item[0]] += int(item[1])
        supply = result_dict.get("supply", 0)
        buy = result_dict.get("buy", 0)
        result = supply - buy
        new_file_lines = [
            f"supply,{supply}\n",
            f"buy,{buy}\n",
            f"result,{result}\n",
        ]

    with open(report_file_name, "w") as file:
        file.write("".join(new_file_lines))
