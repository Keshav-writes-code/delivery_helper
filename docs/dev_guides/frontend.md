## How to add new Svelte Component

While Developing this project, you might need to add Svelte components to use as an App in a Django template
this guide will focus on how to add a parent Svelte Component to be Used as the root app of a Given Django Template
if you just wanna make a child component to add to a svelte component, you dont need any extra work other than importing the child svelte component normally in the Parent Svelte Component

1. Create a `.svelte` file in `./delivery_helper_app/frontend/src/components/` directory
2. create a `.ts` file with the same name as the component in `./delivery_helper_app/frontend/src/apps/` that will be an intermediary to bundle it with Vite. Copy this snippit and paste and change `<component_name>` to your svelte component name

```ts
import { mount } from "svelte";
import App from "../components/<component_name>.svelte";
import "virtual:uno.css";
import "@unocss/reset/tailwind-compat.css";

const app = mount(App, {
  target: document.getElementById("app")!,
});

export default app;
```

3. add the entry for this component in the `vite.config.ts`. change the `<component_name>` and `<path_of_ts_file>` accordingly

```ts
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
        temp: "./src/apps/temp.ts",
        ...,
        <compnent_name>: '<path_of_ts_file>',
      },
    },
  },
});
```

4. then add a .html file in the `./delivery_helper_app/templates/delivery_helper_app/` directory (this is our django template that django can render in view.py)

- add `{% vite_hmr_client %}` in the `<head>` tag
- add `{% vite_asset '<path_of_ts_file>' %}` also in the head tag
  - example path `{% vite_asset 'src/apps/temp.ts' %}`

```html
{% load django_vite %}
<!doctype html>
<html lang="en">
  <head>
    {% vite_hmr_client %}
    {% vite_asset '<path_of_ts_file>' %}
    <!-- Example {% vite_asset 'src/apps/temp.ts' %} -->
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title></title>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
```
