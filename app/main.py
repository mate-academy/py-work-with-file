def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
            open(report_file_name, "w") as file_out):
        supply, buy = 0, 0
        for data in file_in:
            line, value = data.split(",")
            if line == "supply":
                supply += int(value)
            if line == "buy":
                buy += int(value)
        file_out.write(
            f"supply, {supply}\n"
            f"buy, {buy}\n"
            f"result, {supply - buy}\n"
            .replace(" ", "")
        )
