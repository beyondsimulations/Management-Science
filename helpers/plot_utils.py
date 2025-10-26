"""
Plotting utilities for Management Science course.
Provides consistent styling across all plots.
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from cycler import cycler

# Brand colors from _brand.yml - exported for direct use
BRAND_COLORS = {
    "darker": "#363D45",  # Main text
    "lighter": "#FFFDFC",  # Background
    "oneDark": "#F6B265",  # Primary accent (yellow/orange)
    "twoDark": "#537E8F",  # Success/light accent (blue/teal)
    "threeDark": "#DB6B6B",  # Secondary/info (red/pink)
    "oneLight": "#FCCF9C",  # Danger/links (light orange)
    "twoLight": "#A7C7C6",  # Primary accent (light teal)
    "threeLight": "#EBADAD",  # Success/light accent (light pink)
    "codeline": "#FFEEE2",  # Code background
}

# Color sequence used in plots (same as cycler order)
PLOT_COLORS = [
    BRAND_COLORS["threeDark"],  # Red/pink
    BRAND_COLORS["twoDark"],  # Blue/teal
    BRAND_COLORS["oneDark"],  # Yellow/orange
    BRAND_COLORS["threeLight"],  # Light pink
    BRAND_COLORS["twoLight"],  # Light teal
    BRAND_COLORS["oneLight"],  # Light orange
]


def setup_clean_style() -> None:
    """
    Setup a clean, minimal matplotlib style using brand colors.
    No background, good axes, very light grid.

    IMPORTANT: Does NOT reset figure.figsize to preserve Quarto's settings.
    """
    # DO NOT reset rcParams - this would override Quarto's figure size settings!
    # Instead, only update the specific styling parameters we need

    # Clean style settings
    plt.rcParams.update(
        {
            # Figure and axes backgrounds - transparent
            "figure.facecolor": "none",
            "axes.facecolor": "none",
            # Grid - very light
            "grid.alpha": 0.15,
            "grid.linestyle": "--",
            "grid.linewidth": 0.5,
            "grid.color": BRAND_COLORS["darker"],
            # Axes - using brand darker color
            "axes.linewidth": 1.5,
            "axes.edgecolor": BRAND_COLORS["darker"],
            "axes.labelcolor": BRAND_COLORS["darker"],
            "axes.spines.top": False,
            "axes.spines.right": False,
            # Ticks
            "xtick.color": BRAND_COLORS["darker"],
            "ytick.color": BRAND_COLORS["darker"],
            # Lines - using primary brand color
            "lines.linewidth": 2.5,
            "axes.prop_cycle": cycler(color=PLOT_COLORS),
            # Text
            "text.color": BRAND_COLORS["darker"],
            "font.size": 11,
        }
    )


def create_plot(
    figsize: tuple[float, float] | None = None,
    transparent: bool = True,
    equal_aspect: bool = False,
    cartesian: bool = False,
) -> tuple[Figure, Axes]:
    """
    Create a figure with consistent styling and optional Cartesian coordinate system.

    Args:
        figsize: Figure size as (width, height) or None for Quarto defaults
        transparent: Whether to use transparent background (default True)
        cartesian: If True, place spines at zero to create Cartesian axes (default False)

    Returns:
        fig, ax: Figure and axes objects
    """

    # Apply clean brand style
    setup_clean_style()

    fig, ax = plt.subplots()  # pyright: ignore[reportUnknownMemberType]
    ax.grid(True, alpha=0.2)  # pyright: ignore[reportUnknownMemberType]

    # Set transparent background
    if transparent:
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

    return fig, ax
