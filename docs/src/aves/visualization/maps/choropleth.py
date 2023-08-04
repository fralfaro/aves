import matplotlib.colors as colors
import numpy as np
import pandas as pd
import seaborn as sns
from mapclassify import FisherJenks, Quantiles
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.ticker import StrMethodFormatter

from aves.visualization.colors import (
    MidpointNormalize,
    add_ranged_color_legend,
    bivariate_matrix_from_palette,
)


def choropleth_map(
    ax,
    geodf,
    column,
    k=10,
    palette=None,
    default_divergent="RdBu_r",
    default_negative="Blues_r",
    default_positive="Reds",
    palette_type="light",
    legend="colorbar",
    edgecolor="white",
    palette_center=None,
    binning="uniform",
    bins=None,
    alpha=1.0,
    linewidth=1,
    zorder=1,
    cbar_args={},
    **kwargs,
):
    geodf = geodf[pd.notnull(geodf[column])].copy()
    min_value, max_value = geodf[column].min(), geodf[column].max()

    if binning in ("fisher_jenks", "quantiles"):
        if binning == "fisher_jenks":
            binning_method = FisherJenks(geodf[column], k=k)
        else:
            binning_method = Quantiles(geodf[column], k=k)
        bins = np.insert(binning_method.bins, 0, geodf[column].min())
        geodf = geodf.assign(__bin__=binning_method.yb)
    elif binning == "uniform":
        bins = np.linspace(
            min_value, max_value + (max_value - min_value) * 0.001, num=k + 1
        )
        geodf = geodf.assign(
            __bin__=lambda x: pd.cut(
                x[column], bins=bins, include_lowest=True, labels=False
            ).astype(np.int)
        )
    elif binning == "custom":
        if bins is None:
            raise ValueError("bins are needed for custom binning")
        bins = np.array(bins)
        geodf = geodf.assign(
            __bin__=lambda x: pd.cut(
                x[column], bins=bins, include_lowest=True, labels=False
            ).astype(np.int)
        )
    else:
        raise ValueError(
            "only fisher_jenks, quantiles and uniform binning are supported"
        )

    cmap_name = None
    norm = None
    midpoint = 0.0
    using_divergent = False
    built_palette = None

    if palette_center is not None:
        midpoint = palette_center

    if palette is None:
        if min_value < 0 and max_value > 0:
            # divergent
            cmap_name = default_divergent
            norm = MidpointNormalize(vmin=min_value, vmax=max_value, midpoint=midpoint)
            using_divergent = True
        elif min_value < 0:
            # sequential
            cmap_name = default_negative
        else:
            # sequential
            cmap_name = default_positive
    else:
        if not isinstance(palette, colors.Colormap):
            if colors.is_color_like(palette):
                if palette_type == "light":
                    built_palette = sns.light_palette(palette, n_colors=k)
                else:
                    built_palette = sns.dark_palette(palette, n_colors=k)
            else:
                built_palette = sns.color_palette(palette, n_colors=k)

    if norm is None:
        if palette_center is None:
            # norm = colors.Normalize(vmin=min_value, vmax=max_value)
            norm = colors.BoundaryNorm(bins, k)
        else:
            norm = MidpointNormalize(vmin=min_value, vmax=max_value, midpoint=midpoint)
            using_divergent = True

    if built_palette is None:
        if not using_divergent:
            built_palette = sns.color_palette(cmap_name, n_colors=k)
        else:
            middle_idx = np.where((bins[:-1] * bins[1:]) <= 0)[0][0]
            left = middle_idx
            right = k - middle_idx - 1
            if left == right:
                built_palette = sns.color_palette(cmap_name, n_colors=k)
            else:
                delta = np.abs(left - right)
                expanded_k = k + delta
                start_idx = max(middle_idx - left, right - middle_idx)
                built_palette = sns.color_palette(cmap_name, n_colors=expanded_k)[
                    start_idx : start_idx + k
                ]

    for idx, group in geodf.groupby("__bin__"):
        group.plot(
            ax=ax,
            facecolor=built_palette[idx],
            linewidth=linewidth,
            edgecolor=edgecolor,
            alpha=alpha,
            zorder=zorder,
            aspect=None,
        )

    if legend is not None:
        cbar_ax = add_ranged_color_legend(ax, bins, built_palette, **cbar_args)
    else:
        cbar_ax = None

    return ax, cbar_ax


def bivariate_choropleth_map(
    ax,
    geodf,
    col1,
    col2,
    palette="PiYG",
    k=3,
    binning="uniform",
    xlabel=None,
    ylabel=None,
    cbar_ax=None,
    cbar_args={},
    **kwargs,
):
    full_palette = sns.color_palette(palette, n_colors=2 * k - 1)
    bivariate_palette = bivariate_matrix_from_palette(palette, n_colors=k)

    if binning == "uniform":
        col1_binned, col1_bins = pd.cut(geodf[col1], bins=k, labels=False, retbins=True)
        col1_binned = col1_binned.rename(f"{col1}_bin_")
        col2_binned, col2_bins = pd.cut(geodf[col2], bins=k, labels=False, retbins=True)
        col2_binned = col2_binned.rename(f"{col2}_bin_")
    elif binning == "quantiles":
        col1_binned, col1_bins = pd.qcut(geodf[col1], q=k, labels=False, retbins=True)
        col1_binned = col1_binned.rename(f"{col1}_bin_")
        col2_binned, col2_bins = pd.qcut(geodf[col2], q=k, labels=False, retbins=True)
        col2_binned = col2_binned.rename(f"{col2}_bin_")
    elif binning == "fisher_jenks":
        col1_binning = FisherJenks(geodf[col1], k=k)
        col2_binning = FisherJenks(geodf[col2], k=k)
        col1_binned = pd.Series(col1_binning.yb, name=f"{col1}_bin_", index=geodf.index)
        col2_binned = pd.Series(col2_binning.yb, name=f"{col2}_bin_", index=geodf.index)
        col1_bins = np.insert(col1_binning.bins, 0, geodf[col1].min())
        col2_bins = np.insert(col2_binning.bins, 0, geodf[col2].min())
    else:
        raise Exception("binning not supported")

    binned_geodf = geodf[["geometry"]].join(col1_binned).join(col2_binned)

    for i in range(k):
        for j in range(k):
            binned_geodf[
                (binned_geodf[f"{col1}_bin_"] == i)
                & (binned_geodf[f"{col2}_bin_"] == j)
            ].plot(color=bivariate_palette[(j, i)], ax=ax, edgecolor="none")

    # legend
    if cbar_ax is None:
        cbar_ax = inset_axes(
            ax,
            width=cbar_args.get("width", "10%"),
            height=cbar_args.get("height", "10%"),
            loc=cbar_args.get("location", "lower center"),
            bbox_to_anchor=cbar_args.get("bbox_to_anchor", [0.0, 0.0, 1.0, 1.0]),
            bbox_transform=cbar_args.get("bbox_transform", ax.transAxes),
        )

    # cbar_ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.2f}"))
    # cbar_ax.yaxis.set_major_formatter(StrMethodFormatter("{x:,.2f}"))

    cbar_ax.set_xlabel(
        xlabel if xlabel else col1, fontsize=cbar_args.get("font_size", "x-small")
    )
    cbar_ax.set_ylabel(
        ylabel if ylabel else col2, fontsize=cbar_args.get("font_size", "x-small")
    )

    cbar_ax.set_xticks(
        np.arange(k + 1) - 0.5,
        labels=list(map(lambda x: f"{x:.2f}", col1_bins)),
        fontsize="xx-small",
    )
    cbar_ax.set_yticks(
        np.arange(k + 1) - 0.5,
        labels=list(map(lambda x: f"{x:.2f}", col2_bins)),
        fontsize="xx-small",
    )

    cbar_ax.imshow(bivariate_palette, origin="lower")

    return bivariate_palette, cbar_ax
