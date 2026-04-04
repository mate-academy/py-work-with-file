def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        for line in file_in:
            cell = line.strip().split(",")
            if cell[0] in result:
                result[cell[0]] += int(cell[1])
            else:
                result[cell[0]] = int(cell[1])
        file_out.writelines(f'supply,{result["supply"]}\n')
        file_out.writelines(f'buy,{result["buy"]}\n')
        file_out.writelines(f'result,{result["supply"] - result["buy"]}\n')
