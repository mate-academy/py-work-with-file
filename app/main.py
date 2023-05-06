# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_result = 0
    buy_result = 0

    with open(data_file_name, "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            if "supply" in line:
                supply_result += int(line.split(",")[1])
            if "buy" in line:
                buy_result += int(line.split(",")[1])

    total_result = supply_result - buy_result

    with open(report_file_name, "w") as output_file:
        (output_file.write
         (f"supply,{supply_result}\nbuy,{buy_result}\nresult,{total_result}\n")
         )
