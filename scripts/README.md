# Visualization utilities

These figure-only utilities do not implement model architecture, training, inference, attribution calculation, or screening.

- `colors.py`: pastel colour helpers for manuscript-style plots.
- `render_pdf_previews.py`: converts the first page of each figure PDF in a folder into a PNG preview.

From the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/render_pdf_previews.py assets/figures/main
```

The command writes PNGs beside the source PDFs. The full research implementation is not included; publication status does not change its access conditions.
