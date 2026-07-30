def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data_file.readlines():
        if line.strip():
            tipo, valor = line.split(",")
            if tipo == "supply":
                supply += int(valor)
            else:
                buy += int(valor)
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")
    report_file.close()
