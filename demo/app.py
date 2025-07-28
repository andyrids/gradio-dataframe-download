"""Demo app to test & demonstrate `DataFrameDownload` component.

Author: Andrew Ridyard.

License: GNU General Public License v3 or later.

Copyright (C): 2025.

Functions:
    generate_dataframe: Generate a `pandas.DataFrame` for display & download.
"""
import pathlib

import gradio as gr
import numpy as np
from pandas import DataFrame, date_range

from dataframe_download import DataFrameDownload


def generate_dataframe(nrows: int) -> tuple[DataFrame, DataFrame]:
    """Generate a `pandas.DataFrame` for display & download.
    
    Args:
        nrows (int): Number of rows to create for the generated `DataFrame`.
    
    Returns:
        tuple[DataFrame, DataFrame]: Two DataFrame objects, which are used as
            outputs to `gradio.DataFrame` and `DataFrameDownload`.
    """
    data = {
        "ID": np.arange(nrows),
        "Name": map(lambda x: f"NAME_{x}",  range(nrows)),
        "Value": np.random.randn(nrows),
        "Timestamp": date_range(start="2024-01-01", periods=nrows, freq="D"),
        "Category": np.random.choice(range(10), size=nrows),
    }
    dataframe = DataFrame(data)
    return dataframe, dataframe


with gr.Blocks() as demo:
    markdown = pathlib.Path(__file__).parent / "instructions.md"
    gr.Markdown(markdown.read_text())

    with gr.Row(equal_height=True):
        with gr.Column():
            row_slider = gr.Slider(
                minimum=10,
                maximum=1000,
                value=10,
                step=10,
                label="Row count",
                scale=1
            )
        with gr.Column():
            generate_btn = gr.Button("Generate DataFrame", scale=1)
            download_btn = DataFrameDownload(
                label="Download DataFrame",
                variant="huggingface",
                size="lg",
                scale=1,
            )

    with gr.Column():
        display = gr.Dataframe(label="DataFrame Preview")

    generate_btn.click(
        fn=generate_dataframe, inputs=row_slider, outputs=[display, download_btn]
    )

if __name__ == "__main__":
    demo.launch()
