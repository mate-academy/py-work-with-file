def create_report(data_file_name: str, report_file_name: str) -> None:
    character_separator = ","

    result = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "rt") as file_obj:
        for line in file_obj.readlines():
            if line:
                data = line.rstrip("\n").split(character_separator)
                if len(data) >= 2:
                    result[data[0]] += int(data[1])

    result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "wt") as file_obj:
        for key, value in result.items():
            file_obj.write(character_separator.join((key, str(value))) + "\n")


if __name__ == "__main__":
    create_report("..\\apples.csv", "report.txt")
