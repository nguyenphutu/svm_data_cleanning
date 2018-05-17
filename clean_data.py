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

# Chuyen doi ky tu chu cai thanh dang so

list_classes = list(data_frame['classes'])

classes = {'e': -1, 'p': 1}
for k, v in classes.items():
    for index, bruise in enumerate(list_classes):
        if bruise == k:
            list_classes[index] = v

data_frame['classes'] = list_classes

# =====================

list_cap_shape = list(data_frame['cap-shape'])

cap_shape = {'b': 1, 'c': 2, 'x': 3, 'f': 4, 'k': 5, 's': 6}
for k, v in cap_shape.items():
    for index, bruise in enumerate(list_cap_shape):
        if bruise == k:
            list_cap_shape[index] = v

data_frame['cap-shape'] = list_cap_shape

# =====================

list_cap_surface = list(data_frame['cap-surface'])

cap_surface = {'f': 1, 'g': 2, 'y': 3, 's': 4}
for k, v in cap_surface.items():
    for index, bruise in enumerate(list_cap_surface):
        if bruise == k:
            list_cap_surface[index] = v

data_frame['cap-surface'] = list_cap_surface

# =====================

list_cap_color = list(data_frame['cap-color'])
cap_color = {'n': 1, 'b': 2, 'c': 3, 'g': 4, 'r': 5, 'p': 6, 'u': 7, 'e': 8, 'w': 9, 'y': 0}
for k, v in cap_color.items():
    for index, bruise in enumerate(list_cap_color):
        if bruise == k:
            list_cap_color[index] = v

data_frame['cap-color'] = list_cap_color

# =====================

list_bruises = list(data_frame['bruises'])

bruises = {'t': 1, 'f': 0}
for k, v in bruises.items():
    for index, bruise in enumerate(list_bruises):
        if bruise == k:
            list_bruises[index] = v

data_frame['bruises'] = list_bruises

# =====================

list_odor = list(data_frame['odor'])
odor = {'a': 1, 'l': 2, 'c': 3, 'y': 4, 'f': 5, 'm': 6, 'n': 7, 'p': 8, 's': 9}
for k, v in odor.items():
    for index, bruise in enumerate(list_odor):
        if bruise == k:
            list_odor[index] = v

data_frame['odor'] = list_odor

# =====================

list_gill_attachment = list(data_frame['gill-attachment'])
gill_attachment = {'a': 1, 'd': 2, 'f': 3, 'n': 4}
for k, v in gill_attachment.items():
    for index, bruise in enumerate(list_gill_attachment):
        if bruise == k:
            list_gill_attachment[index] = v

data_frame['gill-attachment'] = list_gill_attachment

# =====================

list_gill_spacing = list(data_frame['gill-spacing'])
gill_spacing = {'c': 1, 'w': 2, 'd': 3}
for k, v in gill_spacing.items():
    for index, bruise in enumerate(list_gill_spacing):
        if bruise == k:
            list_gill_spacing[index] = v

data_frame['gill-spacing'] = list_gill_spacing

# =====================

list_gill_size = list(data_frame['gill-size'])
gill_size = {'b': 1, 'n': 2}
for k, v in gill_size.items():
    for index, bruise in enumerate(list_gill_size):
        if bruise == k:
            list_gill_size[index] = v

data_frame['gill-size'] = list_gill_size

# =====================

list_gill_color = list(data_frame['gill-color'])
gill_color = {'k': 1, 'n': 2, 'b': 3, 'h': 4, 'g': 5, 'r': 6, 'o': 7, 'p': 8, 'u': 9, 'e': 10, 'w': 11, 'y': 12}
for k, v in gill_color.items():
    for index, bruise in enumerate(list_gill_color):
        if bruise == k:
            list_gill_color[index] = v

data_frame['gill-color'] = list_gill_color

# =====================

list_stalk_shape = list(data_frame['stalk-shape'])
stalk_shape = {'e': 1, 't': 2}
for k, v in stalk_shape.items():
    for index, bruise in enumerate(list_stalk_shape):
        if bruise == k:
            list_stalk_shape[index] = v

data_frame['stalk-shape'] = list_stalk_shape

# =====================

list_stalk_root = list(data_frame['stalk-root'])
stalk_root = {'b': 1, 'c': 2, 'u': 3, 'e': 4, 'z': 5, 'r': 6, '?': None}
for k, v in stalk_root.items():
    for index, bruise in enumerate(list_stalk_root):
        if bruise == k:
            list_stalk_root[index] = v

data_frame['stalk-root'] = list_stalk_root

# =====================

list_stalk_surface_above_ring = list(data_frame['stalk-surface-above-ring'])
stalk_surface_above_ring = {'f': 1, 'y': 2, 'k': 3, 's': 4}
for k, v in stalk_surface_above_ring.items():
    for index, bruise in enumerate(list_stalk_surface_above_ring):
        if bruise == k:
            list_stalk_surface_above_ring[index] = v

data_frame['stalk-surface-above-ring'] = list_stalk_surface_above_ring

# =====================

list_stalk_surface_below_ring = list(data_frame['stalk-surface-below-ring'])
stalk_surface_below_ring = {'f': 1, 'y': 2, 'k': 3, 's': 4}
for k, v in stalk_surface_below_ring.items():
    for index, bruise in enumerate(list_stalk_surface_below_ring):
        if bruise == k:
            list_stalk_surface_below_ring[index] = v

data_frame['stalk-surface-below-ring'] = list_stalk_surface_below_ring

# =====================

list_stalk_color_above_ring = list(data_frame['stalk-color-above-ring'])
stalk_color_above_ring = {'n': 1, 'b': 2, 'c': 3, 'g': 4, 'o': 5, 'p': 6, 'e': 7, 'w': 8, 'y': 9}
for k, v in stalk_color_above_ring.items():
    for index, bruise in enumerate(list_stalk_color_above_ring):
        if bruise == k:
            list_stalk_color_above_ring[index] = v

data_frame['stalk-color-above-ring'] = list_stalk_color_above_ring

# =====================

list_stalk_color_below_ring = list(data_frame['stalk-color-below-ring'])
stalk_color_below_ring = {'n': 1, 'b': 2, 'c': 3, 'g': 4, 'o': 5, 'p': 6, 'e': 7, 'w': 8, 'y': 9}
for k, v in stalk_color_below_ring.items():
    for index, bruise in enumerate(list_stalk_color_below_ring):
        if bruise == k:
            list_stalk_color_below_ring[index] = v

data_frame['stalk-color-below-ring'] = list_stalk_color_below_ring

# =====================

list_veil_type = list(data_frame['veil-type'])
veil_type = {'p': 1, 'u': 2}
for k, v in veil_type.items():
    for index, bruise in enumerate(list_veil_type):
        if bruise == k:
            list_veil_type[index] = v

data_frame['veil-type'] = list_veil_type

# =====================

list_veil_color = list(data_frame['veil-color'])
veil_color = {'n': 1, 'o': 2, 'w': 3, 'y': 4}
for k, v in veil_color.items():
    for index, bruise in enumerate(list_veil_color):
        if bruise == k:
            list_veil_color[index] = v

data_frame['veil-color'] = list_veil_color

# =====================

list_ring_number = list(data_frame['ring-number'])
ring_number = {'n': 1, 'o': 2, 't': 3}
for k, v in ring_number.items():
    for index, bruise in enumerate(list_ring_number):
        if bruise == k:
            list_ring_number[index] = v

data_frame['ring-number'] = list_ring_number

# =====================

list_ring_type = list(data_frame['ring-type'])
ring_type = {'c': 1, 'e': 2, 'f': 3, 'l': 4, 'n': 5, 'p': 6, 's': 7, 'z': 8}
for k, v in ring_type.items():
    for index, bruise in enumerate(list_ring_type):
        if bruise == k:
            list_ring_type[index] = v

data_frame['ring-type'] = list_ring_type

# =====================

list_spore_print_color = list(data_frame['spore-print-color'])
spore_print_color = {'k': 1, 'n': 2, 'b': 3, 'h': 4, 'r': 5, 'o': 6, 'u': 7, 'w': 8, 'y': 9}
for k, v in spore_print_color.items():
    for index, bruise in enumerate(list_spore_print_color):
        if bruise == k:
            list_spore_print_color[index] = v

data_frame['spore-print-color'] = list_spore_print_color

# =====================

list_population = list(data_frame['population'])
population = {'a': 1, 'c': 2, 'n': 3, 's': 4, 'v': 5, 'y': 6}
for k, v in population.items():
    for index, bruise in enumerate(list_population):
        if bruise == k:
            list_population[index] = v

data_frame['population'] = list_population

# =====================

list_habitat = list(data_frame['habitat'])
habitat = {'g': 1, 'l': 2, 'm': 3, 'p': 4, 'u': 5, 'w': 6, 'd': 7}
for k, v in habitat.items():
    for index, bruise in enumerate(list_habitat):
        if bruise == k:
            list_habitat[index] = v

data_frame['habitat'] = list_habitat
print(data_frame)

data_frame.to_csv('data_number.csv')
