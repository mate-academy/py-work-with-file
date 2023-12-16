def create_report(data_file_name: str, report_file_name: str = "out.txt") -> None:
    with open(data_file_name, "r") as data_file, open(report_file_name, 'w') as report_file:
        results = {}
        for line in data_file.readlines():
            columns = line.rstrip("\n").split(",")
            [operation, count] = columns
            results[operation] = results.get(operation, 0) + int(count)

        results["result"] = results["supply"] - results["buy"]
        print(results)
        # for item in results:
        #     print(item)


create_report("bananas.csv")

# with open("bananas.csv", "r") as f:
#     print(f.readlines())