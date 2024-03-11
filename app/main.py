def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        for line in file_in.readlines():
            splitted_line = line.split(",")
            if "supply" in splitted_line:
                supply += int(splitted_line[1])
            elif "buy" in splitted_line:
                buy += int(splitted_line[1])
        file_out.write(f"supply,{supply}\n")  # noqa
        file_out.write(f"buy,{buy}\n")  # noqa
        file_out.write(f"result,{supply - buy}\n")  # noqa
