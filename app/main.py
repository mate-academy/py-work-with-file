def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        line = data_file.readline()
        calc_dict = {}
        while line:
            operation, amount = line.strip().split(",")
            calc_dict[operation] = calc_dict.get(operation, 0) + int(amount)
            line = data_file.readline()

    supply = calc_dict["supply"]
    buy = calc_dict["buy"]
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"

        )
<<<<<<< HEAD


create_report("apples.csv", "apples_report.txt")
=======
>>>>>>> 8539bddc8924a3d0ad6f6f9bb6b0f8a452d007ae
