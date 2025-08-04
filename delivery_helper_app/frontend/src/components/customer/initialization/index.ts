import ky from "ky";

export interface saved_location {
  location_name: string;
  longitude: number;
  latitude: number;
  location_type: string;
  city_level_address: string;
}
export async function get_saved_location(): Promise<saved_location[]> {
  let fetched_locations: {
    id: number;
    owner_id: number;
    location_name: string;
    longitude: string;
    latitude: string;
    location_type: string;
    city_level_address: string;
  }[] = await ky.get("/api/get_customer_locations").json();

  let processed_locations: saved_location[] = fetched_locations.map((obj) => ({
    location_name: obj.location_name,
    location_type: obj.location_type,
    city_level_address: obj.city_level_address,
    longitude: parseFloat(obj.longitude),
    latitude: parseFloat(obj.latitude),
  }));

  return processed_locations;
}
import { Loader } from "@googlemaps/js-api-loader";
export let gMaps_loader = new Loader({
  apiKey: import.meta.env.VITE_GOOGLE_API_KEY,
  version: "weekly",
  libraries: ["places", "geocoding"],
});
