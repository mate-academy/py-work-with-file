def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as file:
        for user in file.readlines():
            user_data = user.split(",")
            if user_data[0] == "supply":
                supply += int(user_data[1])
            if user_data[0] == "buy":
                buy += int(user_data[1])
        result = str(supply - buy)

    with open(report_file_name, "w") as file2:
        file2.write("supply,{}\n".format(supply)
                    + "buy,{}\n".format(buy)
                    + "result,{}\n".format(result))
