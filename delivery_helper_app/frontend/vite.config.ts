import { defineConfig, loadEnv } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import Unocss from "unocss/vite";

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    plugins: [svelte(), Unocss()],
    base: "/static/",
    envDir: "../../",
    build: {
      outDir: "../../static/",
      emptyOutDir: true,
      manifest: "manifest.json",
      rollupOptions: {
        input: {
          customer: "./src/apps/customer.ts",
        },
      },
    },
  };
});
