# Question 2

- States: Configuration of disks on the pegs
- Initial state: All disks are on the first peg (right order)
- Goal: All disks are on the second or third peg (right order)
- Actions: Move disk from top to other free peg or peg with a bigger disk

# Question 3

The depth of the found solution is given by the step count. Because we use BFS,
we find the optimal solution with its corresponding depth.

```
depth of the optimal solution for N = (depth of the optimal solution for N - 1) * 2 + 1
```

# Question 4

The depth of the found solution is `364`. This is not equal to the optimal
solution depth we found in question 3 (which was `63`).

# Question 6

```mermaid
flowchart LR
    a[Out of memory]-->b[Personal computer]
    b[Personal computer]-->c[Typewriter]
    c[Typewriter]-->d[General Motors]
    d[General Motors]-->e[List of rooftop photovoltaic installations]
    e[List of rooftop photovoltaic installations]-->f[Solar power in Germany]
```
