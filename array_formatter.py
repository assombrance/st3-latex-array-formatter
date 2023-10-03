# import difflib
import numpy as np

with open("input.txt", "r") as f:
    data = f.read()


cells = [
    [" ".join(cell.replace("\n", "").split()) for cell in line.split("%")[0].split("&")]
    for line in data.split("\\\\")
]

nb_cell_per_line = max(len(line) for line in cells)

for line in cells:
    line += [""] * (nb_cell_per_line - len(line))

cells = np.array(cells)

max_len_col = [
    max([len(cell) for cell in cells[:, j]]) for j in range(nb_cell_per_line)
]

for (i, j), _ in np.ndenumerate(cells):
    cells[i, j] = cells[i, j].ljust(max_len_col[j])

output = " \\\\\n".join([" & ".join(cells[i, :]) for i in range(len(cells))])


# with open("result.txt", "r") as f:
#     data = f.read()

# print("\n".join([d for d in difflib.ndiff(output, data) if d[0] != " "]))

with open("output.txt", "w") as f:
    f.write(output)
