# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        file_content = file.read()
        file_array = file_content.split()
        supply_res = 0
        buy_res = 0
        for pair in file_array:
            key, value = pair.split(",")
            if key == "supply":
                supply_res += int(value)
            if key == "buy":
                buy_res += int(value)
        supply = f"supply,{supply_res}"
        buy = f"buy,{buy_res}"
        result = f"result,{supply_res - buy_res}"

    with open(report_file_name, "w") as file:
        file.write(supply + "\n")
        file.write(buy + "\n")
        file.write(result + "\n")
