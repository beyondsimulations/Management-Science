# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Quarto-based educational website for a **Management Science** course. The site includes lectures, interactive Python tutorials, and assignments that teach Python programming and management science concepts (Monte Carlo simulation, scheduling, routing, metaheuristics). The course is structured in three parts: Python Foundation (Lectures 1-3), Management Science Tools (Lectures 4-9), and a Consulting Competition (Lectures 10-12).

## Build and Development Commands

### Building the Website

```bash
quarto render
```

This renders all `.qmd` files in the project and generates the website in `_site/`.

### Preview the Website

```bash
quarto preview
```

This starts a local development server with live reload.

### Render Specific Files

```bash
quarto render tutorials/nb_01_01_variables_data_types.qmd
quarto render lectures/lec_01_introduction.qmd
```

### Python Environment Setup

The project uses `uv` for Python package management:

```bash
# Install dependencies
uv sync

# Run Python scripts with uv
uv run python main.py
```

### Post-Render Processing

The build automatically runs two post-render scripts (configured in `_quarto.yml`):

1. `helpers/convert_pypercent.py` - Converts Jupyter notebooks in `_site/tutorials/` to `.py` files in percent format
2. `helpers/convert_qmd_to_md.py` - Moves all `.md` files from `_site/` to `_repo-md/` maintaining directory structure

## Project Structure

### Content Organization

```
/
├── general/          # Course information (syllabus, FAQ, installation guides)
├── lectures/         # Lecture slides in Quarto reveal.js format
├── tutorials/        # Interactive Python notebooks (prefixed with nb_)
├── assignments/      # Student assignments
├── helpers/          # Post-render conversion scripts
└── _repo-md/         # Generated markdown files from rendered site
```

### Key Files

- `_quarto.yml` - Main Quarto configuration with website structure, sidebar navigation, and format settings
- `_brand.yml` - Brand configuration for colors, typography, and fonts (Gelasio, Reddit Sans, Google Sans Code)
- `pyproject.toml` - Python dependencies (jupyter, jupytext, matplotlib, numpy, pandas)
- `Literature.bib` - Bibliography file for academic citations
- `styles.scss` - Custom SCSS styles for the website
- `_metadata.yml` - Directory-level metadata files (found in tutorials/, lectures/, etc.) that set default options for all files in that directory

### Content Formats

The project uses Quarto (`.qmd`) files that support:
- **HTML output** - Primary format for the website
- **Typst (PDF) output** - Available via format links on pages
- **Hugo markdown** - For secondary distribution
- **Jupyter notebooks** - Tutorials also output to `.ipynb` format
- **reveal.js slides** - Lectures render as interactive presentations

Tutorials are executable Python notebooks embedded in `.qmd` files using `{python}` code blocks.

## Content Architecture

### Tutorial Numbering System

Tutorials follow the pattern `nb_XX_YY_topic.qmd`:
- `XX` = Lecture number
- `YY` = Tutorial sequence within lecture
- Example: `nb_01_01_variables_data_types.qmd` is the first tutorial of lecture 1

### Lecture Format

Lectures use Quarto's reveal.js format for slides:
- Source: `lec_01_introduction.qmd`
- HTML output: `lec_01_introduction.html` (readable format)
- Slides output: `lec_01_introduction-revealjs.html` (presentation format)

### Post-Render Workflow

After rendering, the build system:
1. **Converts notebooks to Python scripts** - Tutorial notebooks are converted to `.py` files in percent format for easy code distribution
2. **Archives markdown versions** - All `.md` files are moved to `_repo-md/` to provide plain markdown versions of content

This allows students to access content in multiple formats (HTML, PDF via Typst, Python scripts, Markdown).

## Styling and Branding

The site uses a custom brand system defined in `_brand.yml`:
- **Color palette**: oneDark/oneLight, twoDark/twoLight, threeDark/threeLight
- **Fonts**: Gelasio (headings), Reddit Sans (body), Google Sans Code (monospace)
- **Code highlighting**: GitHub style with custom background color (`codeline: #FFEEE2`)

## Python Dependencies

Core dependencies (from `pyproject.toml`):
- `jupyter` - Notebook infrastructure
- `jupytext` - Notebook format conversion
- `matplotlib` - Plotting and visualization
- `numpy` - Numerical computing
- `pandas` - Data analysis
- `scikit-learn` - Machine learning algorithms
- `scipy` - Scientific computing
- `seaborn` - Statistical data visualization
- `statsmodels` - Statistical modeling

Dev dependencies:
- `ipykernel` - IPython kernel for Jupyter
- `imageio` - Image I/O library for reading and writing images

## Quarto Execution Model

The project uses `freeze: auto` mode:
- Code cells are only re-executed when source files change
- Results are cached in `_freeze/` directory
- This speeds up incremental builds significantly

When modifying tutorial code blocks, the cached results in `_freeze/` will be invalidated and re-executed on next render.

## Website Features

- **Embedded chat assistant** - Course assistant chatbot using a custom model proxy at `https://model-proxy.vlcek-4b4.workers.dev`
- **Code links** - Tutorials include download links to Python scripts
- **Format links** - HTML and PDF (Typst) versions available for all content
- **MathJax** - Mathematical expressions rendered via MathJax 3

## Common Workflows

### Adding a New Tutorial

1. Create `tutorials/nb_XX_YY_topic.qmd` following the numbering convention
2. Add YAML frontmatter with title, subtitle, and code-links:
   ```yaml
   ---
   title: "Notebook X.Y - Topic Name"
   subtitle: "Management Science"
   code-links:
     - text: Python
       href: nb_XX_YY_topic.py
       icon: hand-thumbs-up
   ---
   ```
3. Include Python code blocks with `{python}` syntax
4. Add to `_quarto.yml` sidebar navigation under appropriate section
5. Run `quarto render` to build (the post-render script will automatically generate the `.py` file)

### Adding a New Lecture

1. Create `lectures/lec_XX_topic.qmd`
2. Set `format: revealjs` in frontmatter with custom footer
3. Use `---` for slide breaks and `#` for slide titles
4. Add to `_quarto.yml` sidebar navigation
5. Run `quarto render` to generate presentation HTML

### Modifying Styles

- Edit `styles.scss` for custom CSS/SCSS
- Edit `_brand.yml` for colors, fonts, and typography
- Changes apply globally after running `quarto render`
