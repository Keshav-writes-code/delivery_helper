/// <reference types="svelte" />
/// <reference types="vite/client" />
interface ImportMetaEnv {
  readonly VITE_GOOGLE_API_KEY: string;
}
interface ImportMeta {
  readonly env: ImportMetaEnv;
}
interface saved_location {
  location_name: string;
  longitude: number;
  latitude: number;
  location_type: string;
  city_level_address: string;
}
type PossibleSubmitStates =
  | "idle"
  | "disabled"
  | "waiting"
  | "success"
  | "error";
