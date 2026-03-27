def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (open(data_file_name, "r") as file_to_read,
          open(report_file_name, "w") as file_to_write):
        result = {"supply": 0, "buy": 0}
        for line in file_to_read.readlines():
            if line:
                key, value = line.split(",")
                result[key] += int(value)

        file_to_write.write(f"supply,{result['supply']}\n")
        file_to_write.write(f"buy,{result['buy']}\n")
        file_to_write.write(f"result,{result['supply'] - result['buy']}\n")
