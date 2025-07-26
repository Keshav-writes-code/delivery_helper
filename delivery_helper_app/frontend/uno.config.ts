import { defineConfig } from "unocss";
import { transformerVariantGroup } from "unocss";
import { presetIcons } from "unocss";
import { presetMini } from "unocss";
import { presetDaisy } from "@ameinhardt/unocss-preset-daisy";
import theme from "daisyui/functions/variables.js";
import { presetWebFonts } from "unocss";
import { createLocalFontProcessor } from "@unocss/preset-web-fonts/local";
export default defineConfig({
  rules: [
    ["capitalize", { "text-transform": "capitalize" }],
    ["isolate", { isolation: "isolate" }],
  ],
  presets: [
    presetMini(),
    presetIcons(),
    presetDaisy(),
    presetWebFonts({
      provider: "bunny",
      fonts: {
        sans: "Atkinson Hyperlegible",
        sans2: "Alata",
        mono: "Fira Code",
      },
      processors: createLocalFontProcessor({
        cacheDir: "node_modules/.cache/unocss/fonts",
        fontAssetsDir: "../../static/public/assets/fonts",
        fontServeBaseUrl: "/static/public/assets/fonts",
      }),
    }),
  ],
  transformers: [transformerVariantGroup()],
  separators: [":"],
  theme: {
    ...theme,
    // colors: colors as Record<string, string>
  },
});
