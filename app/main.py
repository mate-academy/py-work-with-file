SRC = "C:\\Users\\Admin\\ProjectsGit\\PythonCore\\py-work-with-file\\"


def create_report(data_file_name: str, report_file_name: str) -> None:
    process_total = {"supply": 0, "buy": 0}
    with (open(f"{SRC}{data_file_name}", "r") as file_data,
          open(report_file_name, "w") as report_file):
        for line in file_data:
            name_process, count = line.strip().split(",")
            process_total[name_process] += int(count)
        result = process_total["supply"] - process_total["buy"]
        report_file.write(f"supply,{process_total['supply']}\n")
        report_file.write(f"buy,{process_total['buy']}\n")
        report_file.write(f"result,{result}\n")
