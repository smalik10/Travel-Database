import pytest
import pandas as pd
import travel_doc

def test_filter_distance(capsys):
     """Does it print the correct dataframe"""
    test = travel_doc.Travel("travel_dest.csv")
    test.filter_distance(1040)
    outerr = capsys.readouterr()
    out = outerr.out
    testdf = pd.read_csv('travel_dest.csv')
    filter = testdf[testdf["Distance'] == 1034].groupby("Country")["Rank"].min()
    assert out == filter
