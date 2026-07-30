import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(data_file_name, "r") as fruits:
        for row in fruits:
            status = row.split(",")[0]
            num = int(row.split(",")[1])
            result[status] += num

        result["result"] = str(result["supply"] - result["buy"])

    with open(report_file_name, "w") as result_scv:
        result_scv_writer = csv.writer(result_scv)
        for action, total in result.items():
            result_scv_writer.writerow([action, total])
