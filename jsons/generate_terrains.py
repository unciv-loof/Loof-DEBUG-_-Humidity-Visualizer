# number of terrains to generate >= 2
n_terrains: int = 10
rgb_final = (0, 0, 255)



terrain_entry_template = """
\t{
\t\t"name": "%s",
\t\t"type": "Land",
\t\t"RGB": [%d, %d, %d],
\t\t"uniques": [
\t\t\t"Occurs at temperature between [-1.00] and [1.00] and humidity between [%.2f] and [%.2f]"
\t\t]
\t},"""

terrain_name_prefix = "Humidity"
rgb_init = (255, 255, 255)
value_range = (0, 1)

import os
from sys import exit
target_dir = "./"
terrains_suffix_fn = "TerrainsSuffix.json"
if not os.path.isdir(target_dir):
	print(f"Directory {target_dir} does not exist - make sure you are in the correct folder")
	exit()
if not os.path.isfile(f"{target_dir}{terrains_suffix_fn}"):
	print(f"Missing file {target_dir}{terrains_suffix_fn}")
	exit()

step_size = (value_range[1] - value_range[0]) / n_terrains
values = [value_range[0] + i * step_size for i in range(n_terrains + 1)]
rgb_step_sizes = tuple((rgb_init[i] - rgb_final[i]) / (n_terrains - 1) for i in range(3))
with open(f"{target_dir}Terrains.json", "w", encoding="utf-8") as out_file:
	out_file.write("[")
	for i in range(n_terrains):
		rgb = tuple(round(255 - i * rgb_step_sizes[j]) for j in range(3))
		terrain_entry = terrain_entry_template % (
			f"{terrain_name_prefix}{i}",
			rgb[0], rgb[1], rgb[2],
			values[i], values[i + 1]
		)
		out_file.write(terrain_entry)
	with open(f"{target_dir}{terrains_suffix_fn}", "r", encoding="utf-8") as in_file:
		terrains_suffix = in_file.read()
	out_file.write(terrains_suffix)
