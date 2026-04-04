def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as r, open(report_file_name, "a") as a:
        output_data = {
            "supply": 0,
            "buy": 0,
            "result": 0,
        }

        for row in r:
            name, count = row.split(",")
            if name == "supply":
                output_data["supply"] += int(count)
            elif name == "buy":
                output_data["buy"] += int(count)

        output_data["result"] = output_data["supply"] - output_data["buy"]

        for el, cnt in output_data.items():
            # flake8: noqa
            a.write(f"{el},{cnt}\n")  # flake8 problem - E231 missing whitespace after ','
