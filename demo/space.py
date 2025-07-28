
import gradio as gr
from app import demo as app
import os

_docs = {'DataFrameDownload': {'description': 'Download button component for client-side DataFrame download as CSV.\n\nA DataFrame is passed as `value` to this component, serialized to JSON,\nand sent to the frontend. The frontend JavaScript converts the JSON data\ninto a CSV string and triggers a download.', 'members': {'__init__': {'label': {'type': 'str', 'default': '"Download DataFrame"', 'description': None}, 'value': {'type': 'Optional[IntoFrame | Callable]', 'default': 'None', 'description': None}, 'variant': {'type': 'ButtonVariant', 'default': '"secondary"', 'description': None}, 'visible': {'type': 'bool', 'default': 'True', 'description': None}, 'size': {'type': 'Literal["sm", "md", "lg"]', 'default': '"lg"', 'description': None}, 'icon': {'type': 'Optional[str | Path]', 'default': 'None', 'description': None}, 'scale': {'type': 'Optional[int]', 'default': 'None', 'description': None}, 'min_width': {'type': 'Optional[int]', 'default': 'None', 'description': None}, 'interactive': {'type': 'bool', 'default': 'True', 'description': None}, 'elem_id': {'type': 'Optional[str]', 'default': 'None', 'description': None}, 'elem_classes': {'type': 'Optional[list[str] | str]', 'default': 'None', 'description': None}, 'render': {'type': 'bool', 'default': 'True', 'description': None}, 'return': {'type': 'None', 'description': None}}, 'postprocess': {'data': {'type': 'Optional[IntoFrame]', 'default': 'None', 'description': None}, 'value': {'type': 'Optional[IntoFrame]', 'default': 'None', 'description': None}}, 'preprocess': {'return': {'type': 'str | None', 'description': 'str | None: JSON string.'}, 'value': None}}, 'events': {'click': {'type': None, 'default': None, 'description': 'Triggered when the DataFrameDownload is clicked.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'DataFrameDownload': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `dataframe_download`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

A `gradio` component for stateless DataFrame download as a CSV.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install dataframe_download
```

## Usage

```python
\"\"\"Demo app to test & demonstrate `DataFrameDownload` component.

Author: Andrew Ridyard.

License: GNU General Public License v3 or later.

Copyright (C): 2025.

Functions:
    generate_dataframe: Generate a `pandas.DataFrame` for display & download.
\"\"\"
import pathlib

import gradio as gr
import numpy as np
from pandas import DataFrame, date_range

from dataframe_download import DataFrameDownload


def generate_dataframe(nrows: int) -> tuple[DataFrame, DataFrame]:
    \"\"\"Generate a `pandas.DataFrame` for display & download.
    
    Args:
        nrows (int): Number of rows to create for the generated `DataFrame`.
    
    Returns:
        tuple[DataFrame, DataFrame]: Two DataFrame objects, which are used as
            outputs to `gradio.DataFrame` and `DataFrameDownload`.
    \"\"\"
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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `DataFrameDownload`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["DataFrameDownload"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["DataFrameDownload"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, str | None: JSON string.


 ```python
def predict(
    value: str | None
) -> Optional[IntoFrame]:
    return value
```
""", elem_classes=["md-custom", "DataFrameDownload-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          DataFrameDownload: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
