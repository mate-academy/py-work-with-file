def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        data = {"supply": 0, "buy": 0, "result": 0}

        for line in data_file:
            line = line.split(",")

            if line:
                if line[0] == "supply":
                    data["supply"] += int(line[1])
                if line[0] == "buy":
                    data["buy"] += int(line[1])

        data["result"] = data["supply"] - data["buy"]

        for key, value in data.items():
            report_file.write(f"{key},{value}\n")
