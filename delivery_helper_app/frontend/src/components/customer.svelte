<script lang="ts">
  import { onMount } from "svelte";

  let locationName = "";
  let locations: {
    name: string;
    address: string;
    coords: string;
    isDefault: boolean;
  }[] = [
    {
      name: "home_sweet_home",
      address: "123 Main Street, New Delhi, India",
      coords: "28.6139, 77.209",
      isDefault: true
    },
    {
      name: "office_hub",
      address: "456 Business Park, Noida, India",
      coords: "28.5355, 77.391",
      isDefault: false
    }
  ];

  let error = "";

  function validateName(name: string): boolean {
    const regex = /^[a-z0-9_]{3,}$/;
    return regex.test(name);
  }

  function saveLocation() {
    if (!validateName(locationName)) {
      error = "Invalid name. Use a-z, 0-9, _ (min 3 characters)";
      return;
    }

    if (locations.find((loc) => loc.name === locationName)) {
      error = "Location name already exists.";
      return;
    }

    error = "";
    locations.push({
      name: locationName,
      address: "Mock Address, India",
      coords: "00.0000, 00.0000",
      isDefault: false
    });

    locationName = "";
  }

  function setDefault(name: string) {
    locations = locations.map((loc) => ({
      ...loc,
      isDefault: loc.name === name
    }));
  }

  function deleteLocation(name: string) {
    locations = locations.filter((loc) => loc.name !== name);
  }
</script>

<!-- Header -->
<div class="header">
  <h1>Add New Location</h1>
  <p>
    Register your delivery location with unique names for easy ordering on
    Amazon, Flipkart, and other platforms
  </p>
</div>

<div class="container">
  <div class="map">
    <p style="text-align:center; color:#666;">🗺️ Map will appear here</p>
  </div>

  <div class="Register_location">
    <h2>Register Location</h2>
    <p>Give your location a unique name for easy identification.</p>
    <p id="Location">Location Name</p>
    <input
      type="text"
      bind:value={locationName}
      placeholder="e.g. home_sweet_home, office_hub, etc."
      class="location-input"
    />
    <p class="error" style="color: red; font-size: 12px;">{error}</p>
    <p>
      Only lowercase letters, numbers, and underscores allowed. Minimum 3
      characters.
    </p>
    <button class="save-location-button" on:click={saveLocation}>
      ⎙ Save Location
    </button>
  </div>
</div>

<div class="saved-location">
  <h2>Your Saved Locations</h2>
  <p class="subtext">Manage your registered delivery locations</p>

  {#each locations as loc (loc.name)}
    <div class="location-card {loc.isDefault ? 'default' : ''}">
      <div class="location-info">
        <div class="label">
          <span class="location-name">{loc.name}</span>
          {#if loc.isDefault}
            <span class="badge">Default</span>
          {/if}
        </div>
        <div class="address">{loc.address}</div>
        <div class="coords">{loc.coords}</div>
      </div>
      <div class="actions">
        {#if !loc.isDefault}
          <button class="set-default-btn" on:click={() => setDefault(loc.name)}>
            Set Default
          </button>
        {/if}
        <button class="delete-btn" on:click={() => deleteLocation(loc.name)}>🗑</button>
      </div>
    </div>
  {/each}
</div>

<style>
  /* You can keep your current CSS styles */
      * {
        padding: 0;
        margin: 0;
        font-family: poppins, sans-serif;
    }
    /* Header */
    .header {
        text-align: left;
        margin-left: 70px;
        margin-top: 5px;
    }

    .header h1 {
        font-size: 24px;
        color: #fff;
        font-weight: 700;
    }
    .header p {
        font-size: 12px;
        color: #cdd4de;
        font-weight: 400;
        padding-top: 1px;
    }

    /* Container */
    .container {
        display: flex;
        justify-content: space-evenly;
        align-items: stretch;
        height: 60vh;
        padding: 0 2%; /* Adjusts outer gap */
        gap: 2%; /* Adjusts space between divs */
        margin-top: 10px;
    }

    .map {
        width: 45%;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .Register_location {
        width: 45%;
        background-color: #13141f;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
    }
    .Register_location h2 {
        color: #fff;
        font-size: 20px;
        margin-bottom: 10px;
        font-weight: 600;
        font-size: 18px;
    }
    .Register_location p {
        color: #cdd4de;
        font-size: 12px;
        margin-bottom: 10px;
        margin-top: 10px;
    }
    #Location {
        color: #dfd0b8;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .location-input {
        width: 100%;
        height: 30px;
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #ccc;
        font-size: 14px;
        color: #fff;
    }
    .save-location-button {
    width: 100%;
    height: 40px;
    background-color: #393E46;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 10px;
    transition: background-color 0.3s ease;
}

.save-location-button:hover {
    background-color: #222831;
}




.saved-location {
  max-width: 90%;
  padding: 40px;
  background-color: #13141f;
  border-radius: 10px;
  margin: 40px auto;
}

h2 {
  font-size: 20px;
  margin-bottom: 4px;
}

.subtext {
  font-size: 14px;
  color: #aaa;
  margin-bottom: 20px;
}

.location-card {
  background-color: #1a1a2e;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.location-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.label {
  display: flex;
  align-items: center;
  gap: 8px;
}

.location-name {
  font-weight: bold;
  font-size: 16px;
}

.badge {
  background-color: #ffffff22;
  color: #fff;
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 4px;
}

.address,
.coords {
  font-size: 14px;
  color: #ccc;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: flex-end;
}

.set-default-btn {
  background-color: #444;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.set-default-btn:hover {
  background-color: #666;
}

.delete-btn {
  background: transparent;
  border: none;
  color: #ccc;
  font-size: 18px;
  cursor: pointer;
}

.delete-btn:hover {
  color: #ff6666;
}

</style>
