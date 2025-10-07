def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dictionary = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()

            if not line:
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)
            data_dictionary[operation] = data_dictionary.get(operation, 0) + amount

    if (data_dictionary["supply"] - data_dictionary["buy"]) >= 0:
        data_dictionary.get("result", 0) + (data_dictionary.get("supply", 0) - data_dictionary.get("buy", 0))

    with open(report_file_name, "a") as report_file:
        for operation, amount in data_dictionary.items():
            report_file.write(f"{operation},{amount}\n")