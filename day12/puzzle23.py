import sys

SHAPES = 6


def main(infile):
    output = 0
    shape_mass = [0] * SHAPES
    ambiguities = 0
    with open(infile) as f:
        shape = 0
        mode = 'shapes'
        region_count = 0
        for line in f:
            if mode == 'shapes':
                if line == '\n':
                    shape += 1
                    if shape == SHAPES:
                        mode = 'regions'
                else:
                    shape_mass[shape] += line.count('#')

            elif mode == 'regions':
                region_count += 1
                size_str, rest = line.split(':')
                M, N = size_str.split('x')
                M, N = int(M), int(N)
                shape_reqs = [int(x) for x in rest.strip().split(' ')]

                total_mass = 0
                for i, shape in enumerate(shape_reqs):
                    total_mass += shape * shape_mass[i]
                shape_count = sum(shape_reqs)

                if total_mass > M * N:
                    print(f"{region_count}: Impossible!")
                elif shape_count <= (M // 3) * (N // 3):
                    print(f"{region_count}: Guaranteed with naive solution")
                    output += 1
                else:
                    print(f"{region_count}: !! UNKNOWN !!")
                    output += 1
                    ambiguities += 1
    print(f"{output} with {ambiguities} ambiguities")


if __name__ == '__main__':
    main(sys.argv[1])