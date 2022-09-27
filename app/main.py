def create_report(data_file_name: str, report_file_name: str):

    with open(data_file_name, "r") as file_in:
        supply = 0
        buy = 0
        for line in file_in.readlines():
            if "supply" in line:
                supply += int(line.split(",")[1])
            if "buy" in line:
                buy += int(line.split(",")[1])

    with open(report_file_name, "w") as file_out:
        file_out.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
