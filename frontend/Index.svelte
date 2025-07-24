<script lang="ts">
	import { Block, BlockLabel  } from "@gradio/atoms";
	import Button from "@gradio/button";
	import { Download as DownloadIcon } from "@gradio/icons";
	import type { Gradio } from "@gradio/utils";
  import { tick } from "svelte";

	// props passed from the `gradio` Python backend
	export let gradio: Gradio<{click: never;}>;
	export let label: string = "Download CSV";
	// `value` will receive the JSON string from `DataFrameDownloadButton.postprocess`
	export let value: string | null = null;
	export let visible: boolean = true;
	export let elem_id: string = "";
	export let elem_classes: string[] = [];


	
</script>

<Block {visible} {elem_id} {elem_classes}>
	
	<Button
		on:click={() => downloadCSVData(value)}
		value={label}
		gradio={gradio}
		interactive={!!value}
		variant="primary"
	/>

	<button
		on:click={() => downloadCSVData(value)}
		class="lg primary"
	>
		{label}
	</button>
</Block>

<style>

</style>