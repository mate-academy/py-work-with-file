def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input_file:
        data = input_file.readlines()
        supply = 0
        buy = 0
        for string in data:
            if string.split(",")[0] == "supply":
                supply += int(string.split(",")[1])
            if string.split(",")[0] == "buy":
                buy += int(string.split(",")[1])

    with open(report_file_name, "w+") as output_file:
        output_file.write(f"supply,{supply}\n")
        output_file.write(f"buy,{buy}\n")
        output_file.write(f"result,{supply - buy}\n")
