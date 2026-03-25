import streamlit as st
import pandas as pd
import clean_currency from check_functions

def detect_whale(
        items_per_person: float,
        price_per_person: float,
        items_per_person_75th_pctile: float,
        price_per_person_75_pctile: float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    return ''


def detect_tipper(tip_pct: float, tip_pct_75th_pctile: float, tip_pct_25_pctile: float) -> str:
    if tip_pct > tip_pct_75th_pctile:
        return 'heavy'
    if tip_pct < tip_pct_25_pctile:
        return 'light'
    return ''


if __name__ == '__main__':
    assert clean_currency('$1,000.00') == 1000.00
    assert clean_currency('$1,000') == 1000.00
    assert clean_currency('1,000') == 1000.00
    assert clean_currency('$1000') == 1000.00

    assert detect_whale(5, 250, 3, 175) == 'whale'
    assert detect_whale(5, 100, 3, 175) == 'big eater'
    assert detect_whale(1, 250, 3, 175) == 'big spender'
    assert detect_whale(1, 100, 3, 175) == ''

    assert detect_tipper(35, 30, 20) == 'heavy'
    assert detect_tipper(15, 30, 20) == 'light'
    assert detect_tipper(25, 30, 20) == ''

    print("All tests passed!")