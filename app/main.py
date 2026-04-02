def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as input_data,\
         open(report_file_name, "w") as result_file:
        reading = input_data.readlines()
        for string in reading:
            string = string.split(",")
            if string[0] == "supply":
                supply += int(string[1])
            if string[0] == "buy":
                buy += int(string[1])
        result_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
