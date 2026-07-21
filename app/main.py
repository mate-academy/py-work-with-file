def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    try:
        with open(data_file_name, "r") as file:
            for line in file:
                line = line.split(",")
                if line[0] in operations:
                    operations[line[0]] += int(line[1])
    except FileNotFoundError as error:
        print(error)
    operations["result"] = operations["supply"] - operations["buy"]
    try:
        with open(report_file_name, "a") as file:
            for key, value in operations.items():
                file.write(f"{key},{value}\n")

    except Exception as error:
        print(error)
