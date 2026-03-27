def create_report(data_file_name: str, report_file_name: str):
    reports = dict()
    with open(data_file_name, "r") as d:
        with open(report_file_name, "w") as r:
            d_ls = "".join(d.readlines()).split()
            for data in d_ls:
                if data.split(",")[0] in reports:
                    reports[data.split(",")[0]] += int(data.split(",")[1])
                else:
                    reports[data.split(",")[0]] = int(data.split(",")[1])

            result = reports["supply"] - reports["buy"]

            r.write(
                f"{'supply'},{reports['supply']}\n"
                f"{'buy'},{reports['buy']}\n"
                f"result,{result}\n"
            )
