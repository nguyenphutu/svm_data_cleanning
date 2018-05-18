import numpy as np
import pandas as pd

f = open("agaricus-lepiota.data.txt", 'r')

data = f.read().split("\n")

result_data = []

for row in data:
    result_data.append(row.split(','))

data_frame = pd.DataFrame(result_data,
                          columns=['classes', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
                                   'gill-attachment',
                                   'gill-spacing',
                                   'gill-size', 'gill-color', 'stalk-shape',
                                   'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring',
                                   'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type',
                                   'veil-color', 'ring-number', 'ring-type',
                                   'spore-print-color', 'population', 'habitat'])


def convert_alpha_to_int(colume, dick_convert):
    list_data_colume = list(data_frame[colume])
    for k, v in dick_convert.items():
        for index, bruise in enumerate(list_data_colume):
            if bruise == k:
                list_data_colume[index] = v

    data_frame[colume] = list_data_colume


# Chuyen doi ky tu chu cai thanh dang so
classes = {'e': -1, 'p': 1}
cap_shape = {'b': 1, 'c': 2, 'x': 3, 'f': 4, 'k': 5, 's': 6}
cap_surface = {'f': 1, 'g': 2, 'y': 3, 's': 4}
cap_color = {'n': 1, 'b': 2, 'c': 3, 'g': 4, 'r': 5, 'p': 6, 'u': 7, 'e': 8, 'w': 9, 'y': 0}
bruises = {'t': 1, 'f': 0}
odor = {'a': 1, 'l': 2, 'c': 3, 'y': 4, 'f': 5, 'm': 6, 'n': 7, 'p': 8, 's': 9}
gill_attachment = {'a': 1, 'd': 2, 'f': 3, 'n': 4}
gill_spacing = {'c': 1, 'w': 2, 'd': 3}
gill_size = {'b': 1, 'n': 2}
gill_color = {'k': 1, 'n': 2, 'b': 3, 'h': 4, 'g': 5, 'r': 6, 'o': 7, 'p': 8, 'u': 9, 'e': 10, 'w': 11, 'y': 12}
stalk_shape = {'e': 1, 't': 2}
stalk_root = {'b': 1, 'c': 2, 'u': 3, 'e': 4, 'z': 5, 'r': 6, '?': None}
stalk_surface_above_ring = {'f': 1, 'y': 2, 'k': 3, 's': 4}
stalk_surface_below_ring = {'f': 1, 'y': 2, 'k': 3, 's': 4}
stalk_color_above_ring = {'n': 1, 'b': 2, 'c': 3, 'g': 4, 'o': 5, 'p': 6, 'e': 7, 'w': 8, 'y': 9}
stalk_color_below_ring = {'n': 1, 'b': 2, 'c': 3, 'g': 4, 'o': 5, 'p': 6, 'e': 7, 'w': 8, 'y': 9}
veil_type = {'p': 1, 'u': 2}
veil_color = {'n': 1, 'o': 2, 'w': 3, 'y': 4}
ring_number = {'n': 1, 'o': 2, 't': 3}
ring_type = {'c': 1, 'e': 2, 'f': 3, 'l': 4, 'n': 5, 'p': 6, 's': 7, 'z': 8}
spore_print_color = {'k': 1, 'n': 2, 'b': 3, 'h': 4, 'r': 5, 'o': 6, 'u': 7, 'w': 8, 'y': 9}
population = {'a': 1, 'c': 2, 'n': 3, 's': 4, 'v': 5, 'y': 6}
habitat = {'g': 1, 'l': 2, 'm': 3, 'p': 4, 'u': 5, 'w': 6, 'd': 7}

convert_alpha_to_int('classes', classes)
convert_alpha_to_int('cap-shape', cap_shape)
convert_alpha_to_int('cap-surface', cap_surface)
convert_alpha_to_int('cap-color', cap_color)
convert_alpha_to_int('bruises', bruises)
convert_alpha_to_int('odor', odor)
convert_alpha_to_int('gill-attachment', gill_attachment)
convert_alpha_to_int('gill-spacing', gill_spacing)
convert_alpha_to_int('gill-size', gill_size)
convert_alpha_to_int('gill-color', gill_color)
convert_alpha_to_int('stalk-shape', stalk_shape)
convert_alpha_to_int('stalk-root', stalk_root)
convert_alpha_to_int('stalk-surface-above-ring', stalk_surface_above_ring)
convert_alpha_to_int('stalk-surface-below-ring', stalk_surface_below_ring)
convert_alpha_to_int('stalk-color-above-ring', stalk_color_above_ring)
convert_alpha_to_int('stalk-color-below-ring', stalk_color_below_ring)
convert_alpha_to_int('veil-type', veil_type)
convert_alpha_to_int('veil-color', veil_color)
convert_alpha_to_int('ring-number', ring_number)
convert_alpha_to_int('ring-type', ring_type)
convert_alpha_to_int('spore-print-color', spore_print_color)
convert_alpha_to_int('population', population)
convert_alpha_to_int('habitat', habitat)

print(data_frame)

data_frame.to_csv('data_number.csv')
