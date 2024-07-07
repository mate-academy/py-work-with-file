from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = defaultdict(int)

    with (
        open(data_file_name, "r") as file,
        open(report_file_name, "w") as report_file,
    ):
        for line in file:
            key, value = line.strip().split(",")
            result[key] += int(value)
        result["result"] = result["supply"] - result["buy"]

        report_file.write(
            f"supply,{result['supply']}\n"
            f"buy,{result['buy']}\n"
            f"result,{result['result']}\n"
        )
