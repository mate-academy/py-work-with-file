def create_report(data_file_name: str, report_file_name: str) -> None:
    report = dict()
    report["result"] = 0
    set_keys = set()

    with open(data_file_name, "r") as sours:
        data = sours.read().split("\n")

        set_keys = set(
            elem.split(",")[0]
            for elem in data
        )

        for key in set_keys:
            report[key] = 0
            for elem in data:
                if elem == "":
                    continue
                par = elem.partition(",")
                par_key = par[0]
                par_val = par[2]

                if key == par_key:
                    report[key] += int(float(par_val))

        report["result"] = report["supply"] - report["buy"]

        with open(report_file_name, "w") as file_out:
            file_out.write(
                f"supply,{report['supply']}\n"
                f"buy,{report['buy']}\n"
                f"result,{report['result']}\n"
            )
