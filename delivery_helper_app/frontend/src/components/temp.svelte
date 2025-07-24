<script lang="ts">
  let n = $state(0);
</script>

<main>
  {n}
  <button
    onclick={() => {
      n++;
    }}
  >
    Increment
  </button>
</main>

<style>
  .hello {
    width: 10px;
  }
</style>
