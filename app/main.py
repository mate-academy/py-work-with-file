from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_pointer:
        content = file_pointer.readlines()

    result = defaultdict(int)
    for line in content:
        line_parts = line.strip().split(",")
        result[line_parts[0]] += int(line_parts[1])

    result["result"] = result["supply"] - result["buy"]
    result_dict = dict(result)

    with open(report_file_name, "w") as file_pointer:
        file_pointer.write(f"supply,{result_dict['supply']}\n")
        file_pointer.write(f"buy,{result_dict['buy']}\n")
        file_pointer.write(f"result,{result_dict['result']}\n")
