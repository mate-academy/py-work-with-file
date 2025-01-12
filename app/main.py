# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    old_file = open(data_file_name, "r")
    new_file = open(report_file_name, "w")

    results = {}

    for line in old_file:
        args = line.split(",")
        if args[0] not in results:
            results[args[0]] = 0
        results[args[0]] += int(args[1])

    results["result"] = results.get("supply") - results.get("buy")

    for key in ("supply", "buy", "result"):
        new_file.write(f"{key}, {results[key]}\n")
