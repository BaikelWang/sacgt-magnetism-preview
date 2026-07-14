# SACGT Magnetism Preview

**Structure-aware crystal learning for interpretable magnetic reasoning in correlated solids**

> [!IMPORTANT]
> This is a limited **pre-publication preview** associated with the SACGT manuscript. It is not the final software or data release. Training code, model weights, task datasets, complete screening tables, and unpublished reproducibility materials are intentionally excluded.

<p align="center">
  <img src="assets/figures/main/figure1.png" width="92%" alt="Overview of the SACGT framework">
</p>

## Research overview

Magnetic and correlated solids present a demanding setting for crystal-property learning because their responses depend on local coordination, medium-range interaction pathways, and lattice-scale periodicity. The Structure-Aware Crystal Graph Transformer (SACGT) is a structure-first framework designed to represent these complementary scales from elemental identities and atomic geometry under periodic boundary conditions.

The accompanying study evaluates SACGT across thermodynamic, magnetic, and electronic targets. It also examines a constrained attribution strategy for identifying trend-level site contributions to crystal magnetization and applies the resulting workflow to the prioritization of two-dimensional magnetic semiconductors. The public material here is limited to selected visual outputs and figure-rendering utilities; it is not sufficient to reproduce the reported training or screening workflow.

## Public contents

```text
assets/figures/main/             Selected main-text figures in PDF and PNG formats
assets/figures/supplementary/    Selected supplementary figures in PDF and PNG formats
scripts/                         Figure-only colour and preview-rendering utilities
docs/                            Figure inventory, access policy, and release plan
examples/                        Placeholder for a future cleared public demonstration
```

The scripts in this repository operate only on already-generated figure files. They do not implement SACGT, train or evaluate a model, calculate attributions, or perform high-throughput screening.

## Figure index

| Item | File | Scope |
|---|---|---|
| Figure 1 | [`figure1.pdf`](assets/figures/main/figure1.pdf) | Framework overview and multiscale crystal representation |
| Figure 2 | [`figure2.pdf`](assets/figures/main/figure2.pdf) | Predictive evaluation, scaling behaviour, and ablations |
| Figure 3 | [`figure3.pdf`](assets/figures/main/figure3.pdf) | Magnetic attribution analysis in correlated Ti$_2$O$_3$ |
| Figure 4 | [`figure4.pdf`](assets/figures/main/figure4.pdf) | Two-dimensional materials screening and first-principles follow-up |
| Supplementary Figure 1 | [`supp_credibility_expanded_matrix.pdf`](assets/figures/supplementary/supp_credibility_expanded_matrix.pdf) | Expanded attribution diagnostics |
| Supplementary Figure 2 | [`supp_2d_saig_panel10.pdf`](assets/figures/supplementary/supp_2d_saig_panel10.pdf) | Attribution overview for representative screened candidates |

## Availability during peer review

This public preview is separate from the confidential reviewer package. Code, configurations, frozen data partitions, and supporting records needed to assess the central claims can be supplied to editors and referees through the journal's confidential submission channel upon request. Restricted materials will not be distributed through public GitHub issues.

After publication or formal release clearance, the authors plan to archive a versioned reproducibility package containing the manuscript-relevant training, inference, attribution, and screening code together with the required metadata and instructions. A Zenodo DOI has been reserved for that release: [`10.5281/zenodo.21340857`](https://doi.org/10.5281/zenodo.21340857). The DOI may remain inactive while the deposit is a restricted draft.

## Deliberately excluded

- SACGT architecture, training, inference, attribution, and screening source code;
- model checkpoints, weights, optimizer states, and private experiment logs;
- training, validation, test, and complete screening datasets;
- full Materials Project or C2DB records and unpublished candidate tables;
- manuscript source files, submission correspondence, and reviewer materials;
- API keys, credentials, local paths, and server-specific configuration.

## Authors

Shilei Ji, Yixuan Wang, Xiaoyang He, Jinlan Wang, Shengjie Zhang, and Li Gao.

Please direct requests for confidential peer-review material through the manuscript submission system so that reviewer anonymity and editorial confidentiality are preserved.

## Citation

This repository is a project preview, not the archival software release. Please cite the final article once bibliographic details are available. Citation metadata for the preview are provided in [`CITATION.cff`](CITATION.cff).

## License

The current contents are distributed under the restrictive pre-publication terms in [`LICENSE`](LICENSE). No open-source licence is implied for the withheld implementation. The licence and citation metadata may be updated when the final reproducibility release is cleared.

See [`docs/PREPUBLICATION_ACCESS.md`](docs/PREPUBLICATION_ACCESS.md) for the access boundary and [`docs/RELEASE_PLAN.md`](docs/RELEASE_PLAN.md) for the planned release stages.
