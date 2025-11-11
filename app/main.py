def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as read_file:
        create_copy = read_file.read().splitlines()
        result_data = {}
        for el in create_copy:
            data_list = el.strip().split(",")
            action = data_list[0]
            value = int(data_list[1])
            if action in result_data:
                result_data[action] += value
            else:
                result_data[action] = value
    with open(report_file_name, "w") as write_result:
        supply = result_data.get("supply", 0)
        buy = result_data.get("buy", 0)
        write_result.write(f"supply,{supply}" + "\n")
        write_result.write(f"buy,{buy}" + "\n")
        write_result.write(f"result,{supply - buy}")
