def create_report(data_file_name: str, report_file_name: str) -> None:
    dictionary = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as input_file:

        for line in input_file:
            parts = line.split(",")
            if parts[0] == "supply":
                dictionary["supply"] += int(parts[1])
            else:
                dictionary["buy"] += int(parts[1])

    with open(report_file_name, "w") as output_file:

        result = dictionary["supply"] - dictionary["buy"]

        for key, value in dictionary.items():
            output_file.write(f"{key},{value}\n")  # noqa: E231
        output_file.write(f"result,{result}\n")  # noqa: E231
