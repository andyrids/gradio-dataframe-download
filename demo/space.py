
import gradio as gr
from app import demo as app
import os

_docs = {'DataFrameDownload': {'description': 'Download button component for client-side DataFrame download as CSV.\n\nA DataFrame is passed as `value` to this component, serialized to JSON,\nand sent to the frontend. The frontend JavaScript converts the JSON data\ninto a CSV string and triggers a download.', 'members': {'__init__': {'label': {'type': 'str', 'default': '"Download DataFrame"', 'description': 'Component label text.'}, 'value': {'type': 'IntoFrame | Callable | None', 'default': 'None', 'description': 'A DataFrame to be serialised for download or a callable.'}, 'variant': {'type': 'Literal["primary", "secondary", "stop"]', 'default': '"secondary"', 'description': "Style variant; 'primary', 'secondary' or 'stop'."}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'Component visibility flag.'}, 'size': {'type': 'Literal["sm", "md", "lg"]', 'default': '"lg"', 'description': "Size of the button; 'sm', 'md' or 'lg'."}, 'icon': {'type': 'str | Path | None', 'default': 'None', 'description': 'URL or path to the icon file to display within the button.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'Relative size compared to adjacent Components.'}, 'min_width': {'type': 'int | None', 'default': 'None', 'description': 'Minimum pixel width (if sufficient screen space).'}, 'interactive': {'type': 'bool', 'default': 'True', 'description': 'Component interactivity flag.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'Optional string assigned as component ID in the HTML DOM.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'CSS classes assigned to component in HTML DOM.'}, 'render': {'type': 'bool', 'default': 'True', 'description': '`Blocks` context render flag.'}}, 'postprocess': {'value': {'type': 'IntoFrame | None', 'default': 'None', 'description': 'A DataFrame object.'}}, 'preprocess': {'return': {'type': 'None', 'description': 'None.'}, 'value': None}}, 'events': {'click': {'type': None, 'default': None, 'description': 'Triggered when the DataFrameDownload is clicked.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'DataFrameDownload': []}}}

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
# `gradio_dataframe_download`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_dataframe_download/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_dataframe_download"></a>  
</div>

A `gradio` component for stateless DataFrame download as CSV.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_dataframe_download
```

## Usage

```python
\"\"\"Custom component demo module.

Functions:
    generate_dataframe: Generate a `pandas.DataFrame` for display & download.
\"\"\"
import pathlib

import gradio as gr
import numpy as np
from pandas import DataFrame, date_range

from gradio_dataframe_download import DataFrameDownload


def generate_dataframe(nrows: int) -> tuple[DataFrame, DataFrame]:
    \"\"\"Generate a `pandas.DataFrame` for display & download.
    
    Args:
        nrows: Number of rows to generate for the DataFrame.
    
    Returns:
        A tuple of duplicate generated DataFrame objects.
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
                variant="primary",
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

- **As input:** Is passed, none.
- **As output:** Should return, a DataFrame object.

 ```python
def predict(
    value: None
) -> IntoFrame | None:
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
