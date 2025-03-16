def create_report(data_file_name: str, report_file_name: str) -> any:
    with open(data_file_name, "r") as file:
        suma = 0
        suma_buy = 0
        for line in file:
            action, count = line.split(",")
            if action == "supply":
                suma += int(count)
            if action == "buy":
                suma_buy += int(count)
            result = suma - suma_buy
            with open(report_file_name, "w") as report_file:
                report_file.write(f"supply,{suma}\n")
                report_file.write(f"buy,{suma_buy}\n")
                report_file.write(f"result,{result}\n")
