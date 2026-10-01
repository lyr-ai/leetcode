# LeetCode

About 660 Python solutions (plus a few SQL ones), grouped by topic, with company sets for Airbnb and Meta.

## Airbnb Algorithm Stepper

**[▶ Open the visualizer](https://lyr-ai.github.io/leetcode/airbnb/)**

Step-through animations for 8 high-frequency Airbnb problems that are not yet solved in this repo, plus the 11
already solved in `airbnb/` for review. Every frame highlights the matching line of Python and shows the variables at that
moment. Use `←` `→` to step and `Space` to play or pause.

| # | Problem | Difficulty | Airbnb frequency |
|---|---|---|---|
| 751 | [IP to CIDR](https://lyr-ai.github.io/leetcode/airbnb/#p751) ★ | Medium | 71% |
| 1058 | [Minimize Rounding Error to Meet Target](https://lyr-ai.github.io/leetcode/airbnb/#p1058) ★ | Medium | 69% |
| 756 | [Pyramid Transition Matrix](https://lyr-ai.github.io/leetcode/airbnb/#p756) ★ | Medium | 69% |
| 1557 | [Minimum Number of Vertices to Reach All Nodes](https://lyr-ai.github.io/leetcode/airbnb/#p1557) ★ | Medium | 69% |
| 1235 | [Maximum Profit in Job Scheduling](https://lyr-ai.github.io/leetcode/airbnb/#p1235) | Hard | 92% |
| 1257 | [Smallest Common Region](https://lyr-ai.github.io/leetcode/airbnb/#p1257) | Medium | 85% |
| 1298 | [Maximum Candies You Can Get from Boxes](https://lyr-ai.github.io/leetcode/airbnb/#p1298) | Hard | 84% |
| 631 | [Design Excel Sum Formula](https://lyr-ai.github.io/leetcode/airbnb/#p631) | Hard | 76% |

### Review set: already solved in `airbnb/`

Animated from this repo's own solutions (docstrings removed). Notes mark where the page deviates.

| # | Problem | Difficulty | Airbnb frequency | Note |
|---|---|---|---|---|
| 251 | [Flatten 2D Vector](https://lyr-ai.github.io/leetcode/airbnb/#p251) | Medium | 86% |  |
| 336 | [Palindrome Pairs](https://lyr-ai.github.io/leetcode/airbnb/#p336) | Hard | 85% | Python 2 `/` shown as `//` |
| 755 | [Pour Water](https://lyr-ai.github.io/leetcode/airbnb/#p755) | Medium | 79% |  |
| 773 | [Sliding Puzzle](https://lyr-ai.github.io/leetcode/airbnb/#p773) | Hard | 78% | BFS layers + shortest-path replay |
| 269 | [Alien Dictionary](https://lyr-ai.github.io/leetcode/airbnb/#p269) | Hard | 75% | Shows standard Kahn topological sort; the repo version only works when constraints form a single chain |
| 787 | [Cheapest Flights Within K Stops](https://lyr-ai.github.io/leetcode/airbnb/#p787) | Medium | 71% |  |
| 1166 | [Design File System](https://lyr-ai.github.io/leetcode/airbnb/#p1166) | Medium | 69% |  |
| 1109 | [Corporate Flight Bookings](https://lyr-ai.github.io/leetcode/airbnb/#p1109) | Medium | — | Difference array |
| 295 | [Find Median from Data Stream](https://lyr-ai.github.io/leetcode/airbnb/#p295) | Hard | — | Relies on Python 2 `None < int`; page shows the Python 3 fix |
| 374 | [Guess Number Higher or Lower](https://lyr-ai.github.io/leetcode/airbnb/#p374) | Easy | — | Python 2 `/` shown as `//` |
| 1500 | [Design a File Sharing System](https://lyr-ai.github.io/leetcode/airbnb/#p1500) | Medium | — |  |

Frequencies come from LeetCode company-tag statistics ([codejeet](https://codejeet.com/company/airbnb)).
★ means the problem also appears in the most widely shared list of Airbnb interview questions
([airbnb-1](https://github.com/kanglicheng/airbnb-1)).

### Updating the page

The source is [`airbnb/visualizer.html`](airbnb/visualizer.html). GitHub Pages serves the `docs/` folder on
`main`, so after editing the source, rebuild the Pages copy and push:

```bash
python3 airbnb/build_page.py      # writes docs/airbnb/index.html
git add airbnb docs && git commit -m "..." && git push
```

The site updates about a minute after the push.

## Layout

| Folder | Contents |
|---|---|
| `airbnb/`, `meta/` | Company sets (`meta/` is split further by topic) |
| `search_arrays/`, `strings/`, `matrix/`, `tree/`, `graphs/` | The largest topic folders |
| `dp/`, `backtracking/`, `greedy/`, `binary_search/`, `heap/`, `stack/`, `trie/`, `interval/`, `linked_lists/` | Classic technique groups |
| `calculations/`, `integers/`, `parentheses/`, `n_sums/`, `robber/`, `coin_change/`, `climb_stairs/`, `optimization/`, `binary/` | Smaller themed groups |
| `system_design/` | Design-style problems (LRU cache, underground system, …) |
| `sql/` | SQL problems |
| `docs/` | GitHub Pages site (generated; do not edit by hand) |

File names start with the LeetCode problem number, e.g. `755_pour_water.py`.
