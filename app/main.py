def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_data,
          open(report_file_name, "w") as file_result):
        data = {}
        for line in file_data:
            if "," in line:
                value, count = line.split(",")
                count = int(count)
                if value in data:
                    data[value] += count
                else:
                    data[value] = count
        supply = data["supply"]
        buy = data["buy"]
        result = supply - buy
        file_result.write(f"supply,{str(supply)}\n")
        file_result.write(f"buy,{str(buy)}\n")
        file_result.write(f"result,{str(result)}\n")
