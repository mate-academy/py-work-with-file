def create_report(data_file_name: str, report_file_name: str) -> None:
    sup = 0
    bu = 0
    res = 0

    with open(data_file_name, "r") as file:
        for line in file:
            parts = line.split(",")
            option = parts[0]
            am = int(parts[1])

            if option == "supply":
                sup += am
            elif option == "buy":
                bu += am

        res = sup - bu

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{sup}\n")
        report_file.write(f"buy,{bu}\n")
        report_file.write(f"result,{res}\n")
