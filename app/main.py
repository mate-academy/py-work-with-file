def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        totals = {}
        data_file = open(data_file_name)
        for line in data_file.readlines():
            if len(line) == 0:
                continue
            parts = line.split(",")
            if totals.get(parts[0]):
                totals[parts[0]] += int(parts[1])
            else:
                totals[parts[0]] = int(parts[1])
        data_file.close()
        report_file = open(report_file_name, "w")
        report_file.write("supply," + str(totals.get("supply", 0)) + "\n")
        report_file.write("buy," + str(totals.get("buy", 0)) + "\n")
        result = totals.get("supply", 0) - totals.get("buy", 0)
        report_file.write("result," + str(result) + "\n")
        report_file.close()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except FileExistsError as e:
        print(f"File already exists: {e}")
    except Exception as e:
        print(f"Error: {e}")
