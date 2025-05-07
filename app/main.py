def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {}

    try:
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                print(line)
                operation, amount = line.split(",")
                if operation not in operations:
                    operations[operation] = int(amount)
                else:
                    operations[operation] += int(amount)

        with open(report_file_name, "w") as report_file:
            result = operations["supply"] - operations["buy"]

            report_file.write(
                "supply," + str(operations["supply"]) + "\n"
                + "buy," + str(operations["buy"]) + "\n"
                + "result," + str(result) + "\n"
            )
    except ValueError as error:
        print(error)
