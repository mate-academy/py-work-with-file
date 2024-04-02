def create_report(data_file_name: str, report_file_name: str):
    operations = [0, 0]
    with open(data_file_name, "r") as input_file, open(report_file_name, "w") as output_file:
        data = input_file.read().split("\n")
        for line in data:
            if line:
                operation_type, amount = line.split(",")
                if operation_type == "supply":
                    operations[0] += int(amount)
                elif operation_type == "buy":
                    operations[1] -= int(amount)
        output_file.write(f"supply,{operations[0]}\n"
                          f"buy,{abs(operations[1])}\n"
                          f"result,{sum(operations)}\n")
