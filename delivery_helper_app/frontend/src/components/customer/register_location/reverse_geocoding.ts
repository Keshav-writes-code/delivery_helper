import { gMaps_loader } from "../initialization";

export async function getCityFromCoords({
  lat,
  lng,
}: {
  lat: number;
  lng: number;
}): Promise<string> {
  const google = await gMaps_loader.importLibrary("geocoding");

  return new Promise((resolve, reject) => {
    const geocoder = new google.Geocoder();

    geocoder.geocode({ location: { lat, lng } }, (results, status) => {
      if (status === "OK" && results?.[0]) {
        const result = results[0];
        let city = "",
          state = "",
          country = "";

        result.address_components?.forEach((component) => {
          if (component.types.includes("locality")) city = component.long_name;
          if (component.types.includes("administrative_area_level_1"))
            state = component.long_name;
          if (component.types.includes("country"))
            country = component.long_name;
        });

        resolve([city, state, country].filter(Boolean).join(", "));
      } else {
        reject(new Error("Geocoding failed"));
      }
    });
  });
}
