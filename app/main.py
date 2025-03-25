def create_report(data_file_name: str, report_file_name: str) -> None:
    obj = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name) as file:
        for line in file:
            str_line = line.split(",")
            type_str = str_line[0]
            number = int(str_line[1])

            obj[type_str] = obj.get(type_str, 0) + number

        obj["result"] = obj["supply"] - obj["buy"]
        result = "\n".join([
            ",".join((key, str(value)))
            for (key, value) in obj.items()
        ])

        with open(report_file_name, "w") as write_file:
            write_file.write(f"{result}\n")
