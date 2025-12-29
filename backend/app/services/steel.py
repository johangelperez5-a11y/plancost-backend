# backend/app/services/steel.py

KG_PER_M = {
    "#3": 0.560,
    "#4": 0.994,
    "#5": 1.552,
    "#6": 2.235,
    "#7": 3.042,
    "#8": 3.973
}

def steel_by_bars(total_length_m, bar_type):
    return total_length_m * KG_PER_M[bar_type]

def steel_by_ratio(concrete_m3, ratio_kg_m3):
    return concrete_m3 * ratio_kg_m3
