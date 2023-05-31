def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        for line in file:
            temp = line.split(",")
            if temp[0] == "supply":
                data["supply"] += int(temp[1])
            elif temp[0] == "buy":
                data["buy"] += int(temp[1])
    with open(report_file_name, "w") as file:
        file.write(f"supply,{data['supply']}\n"
                   f"buy,{data['buy']}\n"
                   f"result,{data['supply'] - data['buy']}\n")


if __name__ == "__main__":
    create_report("apples.csv", "report.csv")
