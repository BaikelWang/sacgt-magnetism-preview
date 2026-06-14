"""Color utilities used for SACGT figure previews.

The palette is intentionally small and publication-oriented. It mirrors the
pastel visual language used in the manuscript figures without exposing any
model, data, or screening logic.
"""
from matplotlib.colors import LinearSegmentedColormap
import colorsys

PASTELS = {
    "pink": "#F9B6B0",
    "green": "#E1EDCB",
    "teal": "#B2DECF",
    "peach": "#FDD8C0",
    "lilac": "#C5CCE8",
}

def _hex2rgb01(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def _darker(rgb, factor=0.90):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    return colorsys.hls_to_rgb(h, max(0.0, min(1.0, l * factor)), s)

def single_hue_cmap(base_hex="#C5CCE8", with_dark_tail=True, name="sacgt_single_hue"):
    base = _hex2rgb01(base_hex)
    colors = [(1, 1, 1), base, _darker(base)] if with_dark_tail else [(1, 1, 1), base]
    return LinearSegmentedColormap.from_list(name, colors, N=256)

def two_slope_pastel(base_neg="#C5CCE8", base_pos="#F9B6B0", name="sacgt_diverging"):
    return LinearSegmentedColormap.from_list(name, [base_neg, "white", base_pos], N=256)
