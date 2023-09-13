from main import computation

import polars as pl
import matplotlib.pyplot as plt


def test_computation():
    wdi = pl.read_csv(
        "https://media.githubusercontent.com/"
        "media/nickeubank/MIDS_Data/"
        "master/World_Development_Indicators/wdi_small_tidy_2015.csv"
    )

    wdi = wdi.drop_nulls(["GDP per capita (constant 2010 US$)"])

    result = computation(wdi)
    expected_mean = sum(wdi["GDP per capita (constant 2010 US$)"]) / len(
        wdi["GDP per capita (constant 2010 US$)"]
    )
    expected_mean = round(expected_mean, 10)
    sort_wdi = sorted(wdi["GDP per capita (constant 2010 US$)"])
    n = len(sort_wdi)
    if n % 2 == 0:
        expected_median = (sort_wdi[n // 2 - 1] + sort_wdi[n // 2]) / 2
        expected_median = round(expected_median, 10)
    else:
        expected_median = sort_wdi[n // 2]
        expected_median = round(expected_median, 10)

    expected_standard_dev = 22881.31
    print(result)
    print((expected_mean, expected_median, expected_standard_dev))
    assert result == (expected_mean, expected_median, expected_standard_dev)


if __name__ == "__main__":
    test_computation()
