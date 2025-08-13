<script lang="ts">
  type Props = {
    all_locations: saved_location[];
    deleted_locations: saved_location[];
    modified_locations: saved_location[];
  };
  let {
    all_locations,
    deleted_locations = $bindable(),
    modified_locations = $bindable(),
  }: Props = $props();
  // TODO: Start Working on the Editing and Removing of location functionlity
</script>

<div class="b-1 b-gray/20 rounded-box flex-1 p-6">
  <div class="flex gap-2 items-center mb-2">
    <p class="text-lg font-semibold">Your Saved Locations</p>
  </div>
  <p class="color-gray text-sm mb-6">
    Manage your registered delivery locations
  </p>
  <ul class="list bg-base-100 rounded-box shadow-md">
    {#each all_locations.reverse() as location}
      <li class="list-row">
        <div class=" aspect-ratio-square grid place-items-center">
          {#if location.location_type == "home"}
            <div class="i-tabler:home-filled color-#e3ffba size-7"></div>
          {:else if location.location_type == "office"}
            <div class="i-tabler:briefcase-filled color-#adaeff size-7"></div>
          {:else if location.location_type == "college"}
            <div class="i-tabler:book-filled color-#add5ff size-7"></div>
          {:else}
            <div class="i-tabler:map-pin size-6"></div>
          {/if}
        </div>
        <div>
          <div>{location.location_name}</div>
          <div class="text-xs uppercase font-semibold opacity-60">
            {location.city_level_address}
          </div>
        </div>
        <button class="btn btn-square btn-ghost">
          <div class="i-tabler:pencil size-5"></div>
        </button>
      </li>
    {/each}
  </ul>
</div>
