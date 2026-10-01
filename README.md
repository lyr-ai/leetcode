# LeetCode

About 660 Python solutions (plus a few SQL ones), grouped by topic, with company sets for Airbnb and Meta.

## Airbnb Algorithm Stepper

**[▶ Open the visualizer](https://lyr-ai.github.io/leetcode/airbnb/)**

Step-through animations for 8 high-frequency Airbnb problems that are not yet solved in this repo, plus
solved ones for review. Every
frame highlights the matching line of Python and shows the variables at that moment. Use `←` `→` to step
and `Space` to play or pause.

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

Also included for review: [1109 Corporate Flight Bookings](https://lyr-ai.github.io/leetcode/airbnb/#p1109)
(difference array), animated from this repo's own solution in `airbnb/1109_corp_flight_bookings.py`.

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
