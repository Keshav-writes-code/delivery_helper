<script lang="ts">
  import PickLocationFromMap from "./pick_location_from_map.svelte";
  let coordinates = $state(null);
  let placeHolderLocation = [
    {
      location_uname: "keshav_house_1231",
      city_level_address: "ambala, haryana, india",
      location_type: "home",
    },
    {
      location_uname: "keshav_office_2",
      city_level_address: "panjokhra, ambala, haryana, india",
      location_type: "office",
    },
    {
      location_uname: "keshav_college_1231",
      city_level_address: "ambala, haryana, india",
      location_type: "college",
    },
    {
      location_uname: "keshav_hair_2",
      city_level_address: "panjokhra, ambala, haryana, india",
      location_type: "parlour",
    },
  ];
</script>

<main class="w-full h-full p-7">
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
          apiKey={import.meta.env.VITE_GOOGLE_API_KEY}
          bind:coordinates
        />
      </div>
    </div>
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
        />
        <p class="label text-wrap mb-5">
          Only lowercase letters, numbers, and underscores allowed. Minimum 3
          characters.
        </p>
      </fieldset>
      <fieldset class="fieldset">
        <legend class="fieldset-legend">Common Location types</legend>
        <form class="filter">
          <input class="btn btn-square" type="reset" value="×" />
          <input
            class="btn"
            id="home"
            type="radio"
            name="delivery_locations"
            aria-label="Home"
          />
          <input
            class="btn"
            type="radio"
            name="delivery_locations"
            aria-label="Office"
          />
          <input
            class="btn"
            type="radio"
            name="delivery_locations"
            aria-label="College"
          />
        </form>
        <p class="label text-wrap mb-5">Choose one of the Location types</p>
      </fieldset>
      <button class="btn btn-block btn-soft">Register</button>
    </div>
  </div>
  <div class="b-1 b-gray/20 rounded-box flex-1 p-6">
    <div class="flex gap-2 items-center mb-2">
      <p class="text-lg font-semibold">Your Saved Locations</p>
    </div>
    <p class="color-gray text-sm mb-6">
      Manage your registered delivery locations
    </p>
    <ul class="list bg-base-100 rounded-box shadow-md">
      {#each placeHolderLocation as location}
        <li class="list-row">
          <div class="bg-base-300 aspect-ratio-square grid place-items-center">
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
            <div>{location.location_uname}</div>
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
</main>
