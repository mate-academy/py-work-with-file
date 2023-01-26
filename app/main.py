def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"./{data_file_name}", "r") as file:
        context = file.readlines()
        report_data = {}
        for line in sorted(context, reverse=True):
            operation, number = line[:-1].split(",")
            number = int(number)
            if operation not in report_data:
                report_data[operation] = number
            else:
                report_data[operation] += number
    with open(f"./{report_file_name}", "w") as report_file:
        preparation_to_write = ""
        for operation, number in report_data.items():
            preparation_to_write += f"{operation},{number}\n"
        report_file.write(
            f"{preparation_to_write}result,"
            f"{report_data['supply'] -report_data['buy']}\n"
        )
