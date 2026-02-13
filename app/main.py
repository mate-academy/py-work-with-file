def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    data = data_file.readlines()
    lista = [item.strip() for item in data]
    buy = 0
    supply = 0
    for data in lista:
        key = (data.split(",")[0])
        if key == "buy":
            buy += int(data.split(",")[1])
        if key == "supply":
            supply += int(data.split(",")[1])

    with open(report_file_name, "w") as final:
        final.write(f"supply,{supply}\n")
        final.write(f"buy,{buy}\n")
        final.write(f"result,{supply - buy}\n")
