def create_report(data_file_name: str, report_file_name: str) -> None:
    accumulate = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            if line:
                name, value = line.split(",")
                accumulate[name] += int(value)

        accumulate["result"] = accumulate["supply"] - accumulate["buy"]

    with open(report_file_name, "w") as file:
        for name, value in accumulate.items():
            file.write(f"{name},{value}\n")  # noqa: E231
