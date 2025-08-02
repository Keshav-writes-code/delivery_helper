import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import Unocss from "unocss/vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte(), Unocss()],
  base: "/static/",
  build: {
    outDir: "../../static/",
    emptyOutDir: true,
    manifest: "manifest.json",
    rollupOptions: {
      input: {
        delivery_agent: "./src/apps/delivery_agent.ts",
      },
    },
  },
});
