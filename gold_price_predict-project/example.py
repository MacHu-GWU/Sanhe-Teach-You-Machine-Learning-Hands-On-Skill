#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import fix_yahoo_finance
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def read_data(start, end):
    """
    Read GLD (The largest Exchange-Traded Fund) Gold data from yahoo finance.

    :param start: datetime in str.
    :param end: datetime in str.
    :return:
    """
    df = fix_yahoo_finance.download("GLD", start="2008-01-01", end="2017-12-31")
    df = df[["Close"]].dropna()
    return df


f1_mean_last3 = "f1_mean_last3"
f2_mean_last9 = "f2_mean_last9"
features = [f1_mean_last3, f2_mean_last9]


def derive_feature(df, able_to_predict_n_days=3):
    """
    In order to predict gold price up to ``n`` days, you need

    :param df:
    :param able_to_predict_n_days:
    :return:
    """
    df[f1_mean_last3] = df["Close"].shift(able_to_predict_n_days).rolling(
        window=3).mean()
    df[f2_mean_last9] = df["Close"].shift(able_to_predict_n_days).rolling(
        window=9).mean()
    df = df.dropna()
    return df


if __name__ == "__main__":
    df = read_data(start="2008-01-01", end="2017-12-31")
    df = derive_feature(df, able_to_predict_n_days=1)

    t = 0.8
    breakpoint_ind = int(df.shape[0] * t)
    train_data = df[features][:breakpoint_ind]
    train_label = df["Close"][:breakpoint_ind]
    test_data = df[features][breakpoint_ind:]
    test_label = df["Close"][breakpoint_ind:]

    model = LinearRegression().fit(train_data, train_label)
    test_predict = model.predict(test_data)
    test_predict = pd.Series(test_predict, index=test_label.index)

    test_label.plot()
    test_predict.plot()
    plt.legend(["actual", "predict"])
    plt.ylabel("Gold Price")
    plt.show()
