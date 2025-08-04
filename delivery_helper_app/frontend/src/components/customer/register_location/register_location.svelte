<script lang="ts">
  import ky from "ky";
  import RegisterLocationForm from "./register_location_form.svelte";
  import { gMaps_loader, type saved_location } from "../initialization";
  import PickLocationFromMap from "./pick_location_from_map.svelte";
  import { getCityFromCoords } from "./reverse_geocoding";

  type coordinates = {
    lat: number;
    lng: number;
  } | null;

  let { new_locations = $bindable() }: { new_locations: saved_location[] } =
    $props();
  async function register() {
    if (!coordinates) return;

    try {
      let city_level_address = await getCityFromCoords({
        lat: coordinates.lat,
        lng: coordinates.lng,
      });
      await ky
        .post("/api/add_modify_locations", {
          json: [
            {
              location_name,
              longitude: coordinates?.lng,
              latitude: coordinates?.lat,
              location_type,
              city_level_address,
            },
          ],
        })
        .json();
      new_locations.push({
        location_name,
        longitude: coordinates?.lng,
        latitude: coordinates?.lat,
        location_type,
        city_level_address,
      });
    } catch (e: any) {
      console.error(e);
      if (e instanceof Error) {
        console.error(e.message);
      }
    }
  }

  let location_name = $state("");
  let location_type = $state("");
  let coordinates: coordinates = $state(null);
</script>

<h1 class="text-3xl font-semibold color-base-content leading-relaxed">
  Add New Location
</h1>
<p class="color-gray text-sm mb-5">
  Register your delivery locations with unique names for easy ordering on
  Amazon, Flipkart, and other platforms
</p>
<div class="w-full flex lt-md:flex-col *:h-auto gap-6 mb-16">
  <div class="b-1 b-gray/20 rounded-box flex-1 p-6">
    <div class="flex gap-2 items-center mb-2">
      <div class="i-tabler:map-pin size-5"></div>
      <p class="text-lg font-semibold">Drop a Pin</p>
    </div>
    <p class="color-gray text-sm mb-6">
      Click anywhere on the map to select your delivery location
    </p>
    <div class="b-1 b-gray/20 rounded-box s">
      <PickLocationFromMap
        {gMaps_loader}
        apiKey={import.meta.env.VITE_GOOGLE_API_KEY}
        bind:coordinates
      />
    </div>
  </div>
  <RegisterLocationForm
    bind:new_locations
    bind:location_name
    bind:location_type
    on_submit={register}
  />
</div>
