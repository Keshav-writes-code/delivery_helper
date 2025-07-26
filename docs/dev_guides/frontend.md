# How to add new Svelte Page

**Focus** : if you need to add a Svelte component as full page in Django

**Not Focus** : if you just wanna make a child component to add to a svelte component, this guide is not for that. although you can just import the child svelte component in the Parent Svelte Component as you would normally do

## Steps

### Step 1

Create a `.svelte` file in `./delivery_helper_app/frontend/src/components/` directory. The file can be left empty for now

### Step 2

create a `.ts` file with the same name as the component in `./delivery_helper_app/frontend/src/apps/`

paste this snippit into the `.ts` file

`./delivery_helper_app/frontend/src/apps/<component_name>` &darr;

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

- Then, change `<component_name>` to the svelte component's name, that you just created

### Step 3

add the entry for this component in the `vite.config.ts`.

`./frontend/vite.config.ts` &darr;

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
        <compnent_name>: '<path_of_ts_file>',
      },
    },
  },
});
```

- then do these changes :
  - `<component_name>` change to &rarr; the Svelte component Name.
  - `<path_of_ts_file>` change to &rarr; path of the `.ts` file relative to `./frontend`
    - example path : `./src/apps/temp.ts`.

### Step 4

create a `.html` file in the `./delivery_helper_app/templates/delivery_helper_app/`directory (this is our django template that django can render in`view.py`). the name could be the Webpage name Example : `temp.html`

now, Paste this Snippit

`templates/delivery_helper_app/temp.html` &darr;

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

- in `{% vite_asset '<path_of_ts_file>' %}`, change the `path_of_ts_file` to the path of the `.ts` file we create earlier
  - example path `'src/apps/temp.ts'`

### Step 5

Open the `views.py` and add a function to render this html in the browser

`./delivery_helper_app/views.py` &darr;

```python
from django.shortcuts import render

def <name_of_the_page>(request):
    return render(request, "<location of the html file>")
    # Exapmle :
    # return render(request, "delivery_helper_app/temp.html")
```

- change the `<location of the html file>` to the the path of the html file relative to the `templates` folder. Example : `delivery_helper_app/temp.html`
- change the `<name_of_the_page>` to whatever you wanna name the page. Example `"temp"`

### Step 6

create a `urls.py` in the django app

`./delivery_helper_app/urls.py` &darr;

```python
from django.urls import path
from . import views

urlpatterns = [path("<url_of_page>/", views.<name_of_the_page>, name="<name_of_the_page>")]

```

- change `<url_of_page>` to the url the page we want.
- change `<name_of_the_page>` to the Page Name
