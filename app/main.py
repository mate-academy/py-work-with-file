def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in:
            str_g = line.split(",")
            if str_g[0] == "supply":
                supply += int(str_g[1])
            if str_g[0] == "buy":
                buy += int(str_g[1])

    with open(report_file_name, "w") as file_out:
        file_out.writelines(f"supply,{supply}\n")
        file_out.writelines(f"buy,{buy}\n")
        file_out.writelines(f"result,{supply - buy}\n")
