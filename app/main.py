def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name, "r") as first_file,\
         open(report_file_name, "w") as second_file:
        read = first_file.readlines()
        for string in read:
            string = string.split(",")
            if string[0] == "supply":
                supply += int(string[1])
            if string[0] == "buy":
                buy += int(string[1])
            result = supply - buy
        second_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{result}\n")
