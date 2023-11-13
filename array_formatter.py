import difflib
import numpy as np

with open("input.txt", "r") as f:
    data = f.read()

no_comments_data = "\n".join([line.split("%")[0] for line in data.split("\n")])

cells = [
    [" ".join(cell.replace("\n", "").split()) for cell in line.split("&")]
    for line in no_comments_data.split("\\\\")
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

output = " \\\\\n".join([" & ".join(cells[i, :]) for i in range(len(cells))]) + " \\\\"


with open("expected_output.txt", "r") as f:
    data = f.read()

print("\n".join([d for d in difflib.ndiff(output, data) if d[0] != " "]))

with open("output.txt", "w") as f:
    f.write(output)
