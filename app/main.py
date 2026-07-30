def create_report(data_file_name: str, report_file_name: str) -> None:
    analise_data = open(data_file_name)
    analized_data = {"supply": 0, "buy": 0}
    for line in analise_data:
        if line.strip():
            operation, amount = line.strip().split(",")
            amount = int(amount)
            analized_data[operation] += amount
    result = analized_data["supply"] - analized_data["buy"]
    analise_data.close()
    report_file = open(report_file_name, "w")
    for key, value in analized_data.items():
        report_file.write(f"{key},{value}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
