<script lang="ts">
  type Props = {
    error: Error | undefined;
  };
  let { error }: Props = $props();
  let error_dialog_elem: HTMLDialogElement | undefined = $state();
  $effect(() => {
    if (error && error_dialog_elem) {
      error_dialog_elem.showModal();
    }
  });
</script>

<dialog id="my_modal_1" bind:this={error_dialog_elem} class="modal">
  <div class="modal-box">
    <div role="alert" class="alert alert-error">
      <div class="i-tabler:cancel size-6"></div>
      {error?.name}
    </div>
    <p class="py-4">
      <span>{@html error?.message}</span>
    </p>
    <div class="modal-action">
      <form method="dialog">
        <!-- if there is a button in form, it will close the modal -->
        <button class="btn">Close</button>
      </form>
    </div>
  </div>
</dialog>
