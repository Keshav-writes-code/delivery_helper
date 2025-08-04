<script lang="ts">
  import { get_saved_location } from "./initialization";
  import type { saved_location } from "./initialization";
  import RegisterLocation from "./register_location/register_location.svelte";
  import SavedLocations from "./saved_locations.svelte";

  let initial_saved_locations: saved_location[] = $state([]);
  (async () => {
    initial_saved_locations = await get_saved_location();
  })();
  let new_locations: saved_location[] = $state([]);
  let modified_locations: saved_location[] = $state([]);
  let deleted_locations: saved_location[] = $state([]);
  let all_locations = $derived.by(() => {
    let locations = [...initial_saved_locations, ...new_locations];

    locations = locations.map((loc) => {
      const modified = modified_locations.find(
        (mod) => mod.location_name === loc.location_name,
      );
      return modified ? modified : loc;
    });

    locations = locations.filter(
      (loc) =>
        !deleted_locations.some(
          (deleted) => deleted.location_name === loc.location_name,
        ),
    );

    return locations;
  });
</script>

<main class="w-full h-full p-7">
  <RegisterLocation bind:new_locations />
  <SavedLocations
    {all_locations}
    bind:deleted_locations
    bind:modified_locations
  />
</main>
