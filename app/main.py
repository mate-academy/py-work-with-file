
def create_report(date_file_name: str, report_file_name: str) -> None:
    supply_count = 0
    buy_count = 0

    with (open(date_file_name, "r") as input_file,
          open(report_file_name, "w") as output_file):

        for line in input_file:
            line = line.replace("\n", "")

            if len(line) != 0:
                list_line = line.split(",")

            if list_line[0] == "supply":
                supply_count += int(list_line[1])

            if list_line[0] == "buy":
                buy_count += int(list_line[1])

        output_file.write(
            f"supply,{supply_count}\n"
            f"buy,{buy_count}\n"
            f"result,{supply_count - buy_count}\n"
        )
