def create_report(data_file_name: str, report_file_name: str) -> None:
    dictionary = {"supply": 0, "buy": 0}

    with open(data_file_name, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            dictionary[operation] += int(amount)

    result = dictionary["supply"] - dictionary["buy"]

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        for key, value in dictionary.items():
            report_file.write(f"{key},{value}\n")
        report_file.write(f"result,{result}\n")
