def create_report(data_file_name: str, report_file_name: str) -> None:
    content_summary: dict = {}

    with open(f"{data_file_name}", "r") as file_in:
        lines = file_in.readlines()

        for line in lines:
            if not line:
                continue

            data = line.split(",")

            if data[0] in content_summary:
                content_summary[data[0]] += int(data[1].strip())
            else:
                content_summary[data[0]] = int(data[1].strip())

    content_summary["result"] = (content_summary["supply"]
                                 - content_summary["buy"])

    with (open(report_file_name, "w") as file_out):
        report_content = (f"supply,{content_summary['supply']}\n"
                          + f"buy,{content_summary['buy']}\n"
                          + f"result,{content_summary['result']}\n")

        file_out.write(report_content)
