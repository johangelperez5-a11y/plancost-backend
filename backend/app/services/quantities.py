# backend/app/services/quantities.py

def slab_volume(area_m2, thickness_m):
    return area_m2 * thickness_m

def beam_volume(width_m, height_m, length_m):
    return width_m * height_m * length_m

def column_volume(b_m, h_m, height_m):
    return b_m * h_m * height_m
