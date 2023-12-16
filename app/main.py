class TransactionTypes:
    SUPPLY = "supply"
    BUY = "buy"
    RESULT = "result"


def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):

        results = {}
        for line in data_file.readlines():
            columns = line.rstrip("\n").split(",")
            [operation, count] = columns
            results[operation] = results.get(operation, 0) + int(count)

        results[TransactionTypes.RESULT] = results[TransactionTypes.SUPPLY] - \
            results[TransactionTypes.BUY]

        report_file.write(
            f"{TransactionTypes.SUPPLY},{results[TransactionTypes.SUPPLY]}\n")
        report_file.write(
            f"{TransactionTypes.BUY},{results[TransactionTypes.BUY]}\n")
        report_file.write(
            f"{TransactionTypes.RESULT},{results[TransactionTypes.RESULT]}\n")
