def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        splitter = data_file.read().split("\n")
        if splitter[-1] == "":
            splitter.pop(-1)
        for i in range(len(splitter)):
            splitter[i] = splitter[i].split(",")
        supply = 0
        buy = 0
        for item in splitter:
            if item[0] == "supply":
                supply += int(item[1])
            else:
                buy += int(item[1])

        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
