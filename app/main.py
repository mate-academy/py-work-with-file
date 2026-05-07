import pandas


def create_report(data_file_name: str, report_file_name: str) -> None:
    df = pandas.read_csv(data_file_name, sep=",", header=None,
                         names=["operation", "value"])

    supply_sum = df[df["operation"] == "supply"]["value"].sum()
    buy_sum = df[df["operation"] == "buy"]["value"].sum()
    diff = supply_sum - buy_sum

    result_df = pandas.DataFrame({
        "text": ["supply", "buy", "result"],
        "value": [supply_sum, buy_sum, diff]
    })

    result_df.to_csv(report_file_name, index=False, header=False, sep=",")
