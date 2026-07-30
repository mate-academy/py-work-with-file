def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum: int = 0
    buy_sum: int = 0
    with open(data_file_name, "r") as file:
        while True:
            data_str: str = file.readline()
            if data_str == "":
                break
            data: list = data_str.split(",")
            if data[0] == "supply":
                supply_sum += int(data[1])
            elif data[0] == "buy":
                buy_sum += int(data[1])
    with open(report_file_name, "a") as report:
        supply: str = "supply,"
        buy: str = "buy,"
        result: str = "result,"
        report.write(supply + f"{supply_sum}\n")
        report.write(buy + f"{buy_sum}\n")
        report.write(result + f"{supply_sum - buy_sum}\n")


if __name__ == "__main__":
    create_report("apples.csv", "apple1.csv")
