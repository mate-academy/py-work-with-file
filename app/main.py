def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as input_file,
        open(report_file_name, "w") as output_file
    ):
        supply, buy = 0, 0

        data_in_list = [
            element.split(",")
            for element in input_file.read().split("\n")
        ]

        for element in data_in_list:
            if element[0] == "supply":
                supply += int(element[1])
            elif element[0] == "buy":
                buy += int(element[1])

        output = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"

        output_file.write(output)
