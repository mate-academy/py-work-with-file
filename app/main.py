def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data:
        for line in data:
            line = line.strip()
            if line:
                oper, suma = line.split(",")
                suma = int(suma)
                if oper == "supply":
                    supply += suma
                elif oper == "buy":
                    buy += suma
    result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
