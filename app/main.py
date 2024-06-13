def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        result = {}
        for line in data_file:
            temp = line.strip().split(",")
            process, count = temp[0], int(temp[1])
            if process in result:
                result[process] += count
            else:
                result[process] = count

    with open(report_file_name, "w") as result_file:
        result_count = 0
        for process, count in result.items():
            result_file.write(f"{process},{count}\n")
            if process == "supply":
                result_count += count
            elif process == "buy":
                result_count -= count
        result_file.write(f"result,{result_count}\n")
