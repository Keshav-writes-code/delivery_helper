<script lang="ts">
  import SubmitButton from "../../common/submit_button.svelte";
  type Props = {
    new_locations: saved_location[];
    location_name: string;
    location_type: string;
    submit_state: PossibleSubmitStates;
    on_submit: Function;
  };

  let {
    new_locations = $bindable(),
    location_name = $bindable(),
    location_type = $bindable(),
    on_submit,
    submit_state,
  }: Props = $props();
</script>

<div class="b-1 b-gray/20 rounded-box flex-1 p-6">
  <div class="flex gap-2 items-center mb-2">
    <div class="i-tabler:device-floppy size-5"></div>
    <p class="text-lg font-semibold">Register Location</p>
  </div>
  <p class="color-gray text-sm mb-4">
    Give your location a unique name for easy identification
  </p>
  <fieldset class="fieldset">
    <legend class="fieldset-legend">Location Unique Name</legend>
    <input
      type="text"
      class="input w-full"
      placeholder="e.g., home_sweet_home, office_hub"
      bind:value={location_name}
    />
    <p class="label text-wrap mb-5">
      Only lowercase letters, numbers, and underscores allowed. Minimum 3
      characters.
    </p>
  </fieldset>
  <fieldset class="fieldset">
    <legend class="fieldset-legend">Common Location types</legend>
    <form class="filter">
      <input
        class="btn btn-square"
        type="reset"
        bind:group={location_type}
        name="delivery_locations_type"
        value="×"
        required
      />
      {#each ["home", "office", "college"] as type}
        <input
          class="btn capitalize"
          type="radio"
          name="delivery_locations_type"
          aria-label={type}
          value={type}
          bind:group={location_type}
          required
        />
      {/each}
    </form>
    <p class="label text-wrap mb-5">Choose one of the Location types</p>
  </fieldset>
  <SubmitButton
    class="btn btn-block btn-soft flex-1 "
    label_text_html="Register"
    onclick={on_submit}
    state={submit_state}
  />
</div>
