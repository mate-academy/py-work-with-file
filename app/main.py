def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as infile, \
            open(report_file_name, "a") as outfile:
        count = {}
        for x in infile.read().split():
            key, value = x.split(",")[0], int(x.split(",")[1])
            if key in count:
                count[key] += value
            else:
                count.update({key: value})
        count.update({"result": count["supply"] - count["buy"]})
        outfile.write(
            f"{'supply'},{count['supply']}\n"
            f"{'buy'},{count['buy']}\n"
            f"{'result'},{count['result']}\n")
