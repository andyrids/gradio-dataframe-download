# pyright: reportCallIssue=false
"""Custom `DataFrameDownload` component module.

Classes:
    DataFrameDownload: Download button component for client-side
        `DataFrame` download as CSV.
"""
from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Optional, TypeAlias

from gradio.components.base import Component
from gradio.events import Events
from gradio_client.documentation import document
from narwhals import from_native
from narwhals.dataframe import DataFrame
from narwhals.typing import IntoFrame

if TYPE_CHECKING:
    from gradio.components import Timer

ButtonVariant: TypeAlias = Literal[
    "primary", "secondary", "stop", "huggingface"
]

@document()
class DataFrameDownload(Component):
    """Download button component for client-side DataFrame download as CSV.

    A DataFrame is passed as `value` to this component, serialized to JSON,
    and sent to the frontend. The frontend JavaScript converts the JSON data
    into a CSV string and triggers a download.
    """
    # facilitate `click` event listeners
    EVENTS = [Events.click]

    def __init__(
        self,
        label: str = "Download DataFrame",
        value: Optional[IntoFrame | Callable] = None,
        *,
        variant: ButtonVariant = "secondary",
        visible: bool = True,
        size: Literal["sm", "md", "lg"] = "lg",
        icon: Optional[str | Path] = None,
        scale: Optional[int] = None,
        min_width: Optional[int] = None,
        interactive: bool = True,
        elem_id: Optional[str] = None,
        elem_classes: Optional[list[str] | str] = None,
        render: bool = True,
    ) -> None:
        """Initialise custom component.

        Args:
            label (str): Component label text.

            value (IntoFrame | Callable, optional): A DataFrame to be
                serialised for download or a callable. Defaults to None.

            variant (ButtonVariant): 'primary' for main call-to-action,
                'secondary' for a more subdued style, 'stop' for a stop
                button.

            visible (bool): If False, the component will be hidden.

            size (str): Size of the button. Can be "sm", "md", or "lg".

            icon (str | Path, optional): URL or path to the icon file to
                display within the button. If None, no icon will be displayed.

            scale (int, optional): Relative size compared to adjacent
                Components. If Components A & B are in a Row, where A has
                scale=2, and B has scale=1 - A will be twice as wide as B.

            min_width (int, optional): Minimum pixel width. Will wrap if
                insufficient screen space to satisfy this value.

            interactive (bool): If False, the component will be in a disabled state.

            elem_id (str, optional): An optional string that is assigned as
                the ID of this component in the HTML DOM. Can be used for
                targeting CSS styles.

            elem_classes (list[str] | str): An optional list of strings that
                are assigned as the classes of this component in the HTML DOM.
                Can be used for targeting CSS styles.

            render (bool): If False, the component will not be rendered in the
                `Blocks` context. Should be used if the intention is to assign
                event listeners now & render the component later.
        """
        super().__init__(
            value=value,
            label=label,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render
        )

        self.icon = self.serve_static_file(icon)
        self.variant = variant
        self.size = size
        # self.link = link
        #self.label = label
        

    def postprocess(self, data: Optional[IntoFrame] = None) -> str | None:
        """Convert the value returned by a `Gradio` function to JSON.

        Args:
            data (IntoFrame | None, optional): A Pandas DataFrame. Defaults to
                None.

        Returns:
            str | None: A DataFrame serialized as JSON in 'split' orientation,
                or None if `data` None.
        """
        nwdata = from_native(data, pass_through=True)
        if isinstance(nwdata, DataFrame):
            # non-serializable types converted to str - we export to CSV anyway
            return json.dumps(
                {
                    "columns": nwdata.columns,
                    "data": nwdata.to_numpy().tolist()
                },
                default=str
            )
        return

    def preprocess(self, data: Optional[str] = None) -> str | None:
        """Convert the frontend value to a python-native data structure.

        Whilst not required for our output-only download button, every
        component must implement a `preprocess` method.

        data (str, optional): JSON string. Defaults to None.

        Returns:
            str | None: JSON string.
        """
        return data

    def api_info(self) -> dict[str, Any]:
        """
        Provides information for the API documentation.
        """
        return {"type": "string", "description": "A JSON string representing the DataFrame."}

    def example_payload(self) -> Any:
        """Return an example JSON payload for the API."""
        return json.dumps({"column_one": [1,2,3], "column_two": [1,2,3]})

    def example_value(self) -> str:
        """Return an example JSON payload for the API."""
        """
        Returns an example value to display in the Gradio app's examples UI.
        """
        return json.dumps({"column_one": [1,2,3], "column_two": [1,2,3]})
