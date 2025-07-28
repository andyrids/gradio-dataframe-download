
# Client-Side DataFrame-to-CSV Download Component in Gradio

`gradio` already provides a suite of pre-built components for creating user interfaces, but it
does not provide a way to download data directly from the browser's memory, without any intermediate file-saving operations on the server. This issue is raised on [gradio GitHub](https://github.com/gradio-app/gradio/issues/10266).

This package contains a custom `DataFrameDownloadButton` component, which facilitates the in-memory download of a `DataFrame` as a CSV file.
