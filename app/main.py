def create_report(data_file_name: str, report_file_name: str):
    supply, buy = 0, 0

    with open(data_file_name, "r") as data_file:
        for operation_type in data_file.read().split():
            if "supply" in operation_type:
                supply += int(operation_type.split(',')[1])
            else:
                buy += int(operation_type.split(',')[1])

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply}\n"
                              f"buy,{buy}\n"
                              f"result,{supply - buy}\n")
