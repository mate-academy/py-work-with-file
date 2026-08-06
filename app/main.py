def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as f:
        table_data = f.read().split("\n")[0:-1]
        table_data.sort(reverse=True)

        for row in table_data:
            row = row.split(",")
            result[row[0]] = int(result.get(row[0], 0)) + int(row[1])

    with open(report_file_name, "w") as f:
        for key, value in result.items():
            f.write(f"{key},{value}\n")
        f.write(f"result,{result['supply'] - result['buy']}\n")
