<script lang="ts">
  import PickLocationFromMap from "./pick_location_from_map.svelte";
  let coordinates = $state(null);
</script>

<main class="w-full h-full p-7">
  <h1 class="text-3xl font-semibold color-base-content leading-relaxed">
    Add New Location
  </h1>
  <p class="color-gray text-sm mb-5">
    Register your delivery locations with unique names for easy ordering on
    Amazon, Flipkart, and other platforms
  </p>
  <div class="w-full flex *:h-auto gap-6">
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
          apiKey={import.meta.env.VITE_GOOGLE_API_KEY}
          bind:coordinates
        />
      </div>
    </div>
    <div class="b-1 b-gray/20 rounded-box size-100 flex-1"></div>
  </div>
</main>
