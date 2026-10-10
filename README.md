# Management Science

A Quarto-based course teaching Python programming and management science concepts including Monte Carlo simulation, forecasting, scheduling, routing, and metaheuristics.

**Live site:** https://beyondsimulations.github.io/Management-Science

## Course Structure

- **Part 1 (Lectures 1-3):** Python Foundation - variables, functions, NumPy, Pandas
- **Part 2 (Lectures 4-9):** Management Science Tools - Monte Carlo, forecasting, greedy/local search, multi-objective optimization, metaheuristics
- **Part 3 (Lectures 10-12):** Consulting Competition - real-world project applications

## Getting Started

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Installation

```bash
git clone https://github.com/beyondsimulations/Management-Science.git
cd Management-Science
uv sync
```

### Render the Website

```bash
uv run quarto render
```

Output is generated in `_site/`, including a PDF of every slide deck. The slide PDF hook needs the sibling checkout `../Lecture-Foundations`, `uv run playwright install chromium` once per machine, and rendering through `uv run`. A deck that cannot be printed fails the render on purpose, as its page already links the PDF.

### Publish

```bash
bash ../Lecture-Foundations/scripts/publish-gh-pages.sh
```

Run it after a full render. It publishes `_site/` and keeps the `gh-pages` branch at one commit.

### Preview with Live Reload

```bash
uv run quarto preview
```

## License

CC BY-NC-SA 4.0
