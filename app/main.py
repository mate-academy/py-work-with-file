# If you're reviewing this code - thank you <3
def create_report(data_file_name: str, report_file_name: str):
    buy_result = 0
    supply_result = 0

    with open(data_file_name, "r") as file_read:
        for line in file_read:
            line = list(line.split(","))
            if line[0] == "supply":
                supply_result += int(line[1])
            if line[0] == "buy":
                buy_result += int(line[1])

    with open(report_file_name, "w") as file_write:
        file_write.write(f"supply,{supply_result}\n"
                         f"buy,{buy_result}\n"
                         f"result,{supply_result - buy_result}\n")
