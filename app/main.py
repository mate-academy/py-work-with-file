def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as input_file,
        open(report_file_name, "w") as report_file
    ):
        strings = input_file.read().split("\n")
        buy = 0
        supply = 0

        for string in strings:
            items = string.split(",")
            if items[0] == "buy":
                buy += int(items[1])
            if items[0] == "supply":
                supply += int(items[1])

        result = supply - buy

        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
