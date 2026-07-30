def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_in:

        for line in file_in:
            items = line.split(",")

            if items[0] == "supply":
                supply += int(items[1])
            if items[0] == "buy":
                buy += int(items[1])

        result = supply - buy

        with open(report_file_name, "w") as file_out:
            file_out.writelines(f"supply,{supply}\n")
            file_out.writelines(f"buy,{buy}\n")
            file_out.writelines(f"result,{result}\n")
