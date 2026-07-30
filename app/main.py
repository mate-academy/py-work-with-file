def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0

        for line in file.read().split("\n"):
            if len(line):
                list_from_line = line.split(",")
                name = list_from_line[0]
                num = list_from_line[1]

                if name == "supply":
                    supply += int(num)
                if name == "buy":
                    buy += int(num)

    with open(report_file_name, "w") as file:
        file.write(
            "supply" + "," + f"{supply}\n"
            + "buy" + "," + f"{buy}\n"
            + "result" + "," + f"{supply - buy}\n"
        )
