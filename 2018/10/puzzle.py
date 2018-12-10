#!/usr/bin/python3

import numpy as np
import re
import sys


def main():
    data = [line for line in sys.stdin]

    def line_parser(s): return list(map(int, re.findall(r'-?\d+', s)))
    points = np.array(list(map(line_parser, data)))

    pos = points[:, [0, 1]]
    vel = points[:, [2, 3]]

    counter = -2
    shrinking = False
    sky_shape_prev = None

    while not shrinking:
        counter += 1

        x_min = min(pos[:, 0])
        x_max = max(pos[:, 0])

        y_min = min(pos[:, 1])
        y_max = max(pos[:, 1])

        sky_shape = (y_max - y_min + 1, x_max - x_min + 1)

        # Expansion started
        if sky_shape_prev and \
           sky_shape[0] > sky_shape_prev[0] and \
           sky_shape[1] > sky_shape_prev[1]:

            # Go back once
            pos -= vel

            # Create empty sky
            sky = np.full(sky_shape_prev, ' ', dtype=str)

            x_min = min(pos[:, 0])
            y_min = min(pos[:, 1])

            # Translate sky to positive quadrant
            if x_min != 0:
                pos[:, 0] -= x_min
            if y_min != 0:
                pos[:, 1] -= y_min

            # Mark poins in sky
            for (x, y) in pos:
                sky[y][x] = '#'

            sky_str = '\n'.join([''.join(row) for row in sky])

            print('Part 1:\n{}'.format(sky_str))
            print('Part 2: {} seconds'.format(counter))

            shrinking = True

        sky_shape_prev = sky_shape
        pos += vel


if __name__ == '__main__':
    main()
