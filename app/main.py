def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        result = {}

        for line in data_file:
            split_line = line.split(",")
            key, value = split_line[0], int(split_line[1])
            result[key] = result.get(key, 0) + value

        report_file.write(
            "supply,{}\n"
            "buy,{}\n"
            "result,{}\n".format(
                result.get("supply", 0),
                result.get("buy", 0),
                result.get("supply", 0) - result.get("buy", 0))
        )
