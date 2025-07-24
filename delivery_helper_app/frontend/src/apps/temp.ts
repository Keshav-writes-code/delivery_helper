import { mount } from "svelte";
import App from "../components/temp.svelte";
import "virtual:uno.css";
import "@unocss/reset/tailwind-compat.css";

const app = mount(App, {
  target: document.getElementById("app")!,
});

export default app;
