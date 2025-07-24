import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  base: "/static/",
  build: {
    outDir: "../../static/",
    emptyOutDir: true,
    manifest: "manifest.json",
    rollupOptions: {
      input: {
        temp: "./src/apps/temp.ts",
      },
    },
  },
});
