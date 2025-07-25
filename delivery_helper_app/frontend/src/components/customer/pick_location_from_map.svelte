<script lang="ts">
  import { Loader } from "@googlemaps/js-api-loader";

  // Define interfaces for our component
  interface MapProps {
    apiKey: string;
    height?: string;
    width?: string;
    coordinates: { lat: number; lng: number } | null;
  }

  // Define props with the $props rune
  let {
    apiKey = "GOOGLE_API_KEY", // Will use the global API key from Vite config
    height = "500px",
    width = "100%",
    coordinates = $bindable<{ lat: number; lng: number } | null>(null),
  }: MapProps = $props();

  // Flag to prevent infinite loop
  let isUpdatingFromMap = $state(false);

  // Use let with $state for mutable reactive state
  let mapState = $state<{
    mapInstance: google.maps.Map | null;
    currentMarker: google.maps.Marker | null;
    infoWindowInstance: google.maps.InfoWindow | null;
    loaderInstance: Loader | null;
  }>({
    mapInstance: null,
    currentMarker: null,
    infoWindowInstance: null,
    loaderInstance: null,
  });
  // Dark theme styles for Google Maps
  const darkMapStyles = [
    { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
    { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
    { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
    {
      featureType: "administrative.locality",
      elementType: "labels.text.fill",
      stylers: [{ color: "#d59563" }],
    },
    {
      featureType: "poi",
      elementType: "labels.text.fill",
      stylers: [{ color: "#d59563" }],
    },
    {
      featureType: "poi.park",
      elementType: "geometry",
      stylers: [{ color: "#263c3f" }],
    },
    {
      featureType: "poi.park",
      elementType: "labels.text.fill",
      stylers: [{ color: "#6b9a76" }],
    },
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [{ color: "#38414e" }],
    },
    {
      featureType: "road",
      elementType: "geometry.stroke",
      stylers: [{ color: "#212a37" }],
    },
    {
      featureType: "road",
      elementType: "labels.text.fill",
      stylers: [{ color: "#9ca5b3" }],
    },
    {
      featureType: "road.highway",
      elementType: "geometry",
      stylers: [{ color: "#746855" }],
    },
    {
      featureType: "road.highway",
      elementType: "geometry.stroke",
      stylers: [{ color: "#1f2835" }],
    },
    {
      featureType: "road.highway",
      elementType: "labels.text.fill",
      stylers: [{ color: "#f3d19c" }],
    },
    {
      featureType: "transit",
      elementType: "geometry",
      stylers: [{ color: "#2f3948" }],
    },
    {
      featureType: "transit.station",
      elementType: "labels.text.fill",
      stylers: [{ color: "#d59563" }],
    },
    {
      featureType: "water",
      elementType: "geometry",
      stylers: [{ color: "#17263c" }],
    },
    {
      featureType: "water",
      elementType: "labels.text.fill",
      stylers: [{ color: "#515c6d" }],
    },
    {
      featureType: "water",
      elementType: "labels.text.stroke",
      stylers: [{ color: "#17263c" }],
    },
  ];
  // Initialize the map when component is mounted
  $effect(() => {
    initMap();

    // Cleanup function
    return () => {
      if (mapState.mapInstance) {
        google.maps.event.clearInstanceListeners(mapState.mapInstance);
      }
      if (mapState.currentMarker) {
        mapState.currentMarker.setMap(null);
      }
    };
  });

  // Watch for external coordinates changes and update marker
  $effect(() => {
    // Skip if the update is coming from the map itself
    if (isUpdatingFromMap) return;

    if (coordinates && mapState.mapInstance) {
      // Only update if we have coordinates and a map
      updateMarkerFromCoordinates();
    }
  });

  async function initMap(): Promise<void> {
    // Initialize the Google Maps loader
    mapState.loaderInstance = new Loader({
      apiKey,
      version: "weekly",
      libraries: ["places"],
    });

    try {
      // Load the Google Maps API
      const google = await mapState.loaderInstance.load();

      // Default center coordinates
      const center: google.maps.LatLngLiteral = { lat: 40.7128, lng: -74.006 };

      const mapElement = document.getElementById("map-container");
      if (!mapElement) {
        console.error("Map container element not found");
        return;
      }

      // Initialize the map
      mapState.mapInstance = new google.maps.Map(mapElement, {
        center,
        zoom: 12,
        mapTypeControl: true,
        streetViewControl: true,
        fullscreenControl: true,
        styles: darkMapStyles,
      });

      // Create info window
      mapState.infoWindowInstance = new google.maps.InfoWindow();

      // Set up map click listener for dropping pins
      mapState.mapInstance.addListener(
        "click",
        (event: google.maps.MapMouseEvent) => {
          if (event.latLng) {
            setMarker(event.latLng);
          }
        },
      );

      // Try to get user's location
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position: GeolocationPosition) => {
            const userLocation: google.maps.LatLngLiteral = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            if (mapState.mapInstance) {
              mapState.mapInstance.setCenter(userLocation);
            }
          },
          (error: GeolocationPositionError) => {
            console.log("Geolocation failed or was denied:", error.message);
          },
        );
      }
    } catch (error) {
      console.error("Error loading Google Maps:", error);
    }
  }

  function setMarker(
    location: google.maps.LatLng | google.maps.LatLngLiteral,
  ): void {
    if (!mapState.mapInstance) return;

    // Remove existing marker if any
    if (mapState.currentMarker) {
      mapState.currentMarker.setMap(null);
    }

    // Using the Advanced Marker is recommended now, but for compatibility we'll use Marker
    const marker = new google.maps.Marker({
      position: location,
      map: mapState.mapInstance,
      title: "Selected Location",
      animation: google.maps.Animation.DROP,
      draggable: true,
    } as google.maps.MarkerOptions);

    // Store the marker
    mapState.currentMarker = marker;

    // Get the latitude and longitude from the location
    const latLng =
      location instanceof google.maps.LatLng
        ? location
        : new google.maps.LatLng(location);

    // Set flag to prevent infinite loop
    isUpdatingFromMap = true;

    // Update the bindable coordinates value
    coordinates = {
      lat: latLng.lat(),
      lng: latLng.lng(),
    };

    // Reset flag after update
    setTimeout(() => {
      isUpdatingFromMap = false;
    }, 0);

    // Create content for info window
    const contentString = `
      <div style="padding: 10px; max-width: 200px;">
        <h3 style="margin-bottom: 8px;">Selected Location</h3>
        <p><strong>Latitude:</strong> ${latLng.lat().toFixed(6)}</p>
        <p><strong>Longitude:</strong> ${latLng.lng().toFixed(6)}</p>
      </div>
    `;

    // Show info window
    if (mapState.infoWindowInstance) {
      mapState.infoWindowInstance.setContent(contentString);
      mapState.infoWindowInstance.open(mapState.mapInstance, marker);
    }

    // Update coordinates when marker is dragged
    marker.addListener("dragend", () => {
      const newPosition = marker.getPosition();
      if (newPosition) {
        // Set flag to prevent infinite loop
        isUpdatingFromMap = true;

        // Update the bindable coordinates
        coordinates = {
          lat: newPosition.lat(),
          lng: newPosition.lng(),
        };

        // Reset flag after update
        setTimeout(() => {
          isUpdatingFromMap = false;
        }, 0);

        // Update info window
        if (mapState.infoWindowInstance) {
          const updatedContent = `
            <div style="padding: 10px; max-width: 200px;">
              <h3 style="margin-bottom: 8px;">Selected Location</h3>
              <p><strong>Latitude:</strong> ${newPosition.lat().toFixed(6)}</p>
              <p><strong>Longitude:</strong> ${newPosition.lng().toFixed(6)}</p>
            </div>
          `;
          mapState.infoWindowInstance.setContent(updatedContent);
          mapState.infoWindowInstance.open(mapState.mapInstance, marker);
        }
      }
    });
  }

  // Function to update marker when coordinates are updated externally
  function updateMarkerFromCoordinates(): void {
    if (!coordinates || !mapState.mapInstance) return;

    // Create a LatLng object from the coordinates
    const location = new google.maps.LatLng(coordinates.lat, coordinates.lng);

    // Only update the marker's position if it already exists
    if (mapState.currentMarker) {
      mapState.currentMarker.setPosition(location);

      // Update info window if open
      if (mapState.infoWindowInstance) {
        const contentString = `
          <div style="padding: 10px; max-width: 200px;">
            <h3 style="margin-bottom: 8px;">Selected Location</h3>
            <p><strong>Latitude:</strong> ${coordinates.lat.toFixed(6)}</p>
            <p><strong>Longitude:</strong> ${coordinates.lng.toFixed(6)}</p>
          </div>
        `;
        mapState.infoWindowInstance.setContent(contentString);
        mapState.infoWindowInstance.open(
          mapState.mapInstance,
          mapState.currentMarker,
        );
      }
    } else {
      // Create a new marker if none exists
      setMarker(location);
    }

    // Center the map on this location
    mapState.mapInstance.setCenter(location);
  }

  // Public method to clear the marker
  export function clearMarker(): void {
    if (mapState.currentMarker) {
      mapState.currentMarker.setMap(null);
      mapState.currentMarker = null;
    }

    // Set flag to prevent infinite loop
    isUpdatingFromMap = true;

    // Clear the coordinates
    coordinates = null;

    // Reset flag after update
    setTimeout(() => {
      isUpdatingFromMap = false;
    }, 0);

    // Close any open info window
    if (mapState.infoWindowInstance) {
      mapState.infoWindowInstance.close();
    }
  }
</script>

<div class=" w-full rounded-box overflow-hidden relative">
  <div id="map-container" style="height: {height}; width: {width};"></div>
</div>
