def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if line.split(",")[0].lower() == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0].lower() == "buy":
                buy += int(line.split(",")[1])
    data_file.close()
    with open(report_file_name, "a") as data_file_new:
        data_file_new.write(f"supply,{supply}"
                            f"\nbuy,{buy}"
                            f"\nresult,{supply-buy}\n")
