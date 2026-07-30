def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:

        save_data = {}

        for data in file.readlines():
            split_data = data.split(",")
            if split_data[0] not in save_data:
                save_data[split_data[0]] = int(split_data[1])
            else:
                save_data[split_data[0]] += int(split_data[1])

    with open(report_file_name, "a") as file_report:
        file_report.write(f"supply,{save_data['supply']}\n"
                          f"buy,{save_data['buy']}\n"
                          f"result,{save_data['supply'] - save_data['buy']}\n")
