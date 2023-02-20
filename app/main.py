from csv import reader, writer


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as input_data:
        data_reader = reader(input_data)
        for data in data_reader:
            operation, amount = data

            if operation == "supply":
                total_supply += int(amount)

            if operation == "buy":
                total_buy += int(amount)

    with open(report_file_name, "w") as output_data:
        data_writer = writer(output_data, delimiter=",")
        data_writer.writerow(["supply", str(total_supply)])
        data_writer.writerow(["buy", str(total_buy)])
        data_writer.writerow(["result", str(total_supply - total_buy)])
