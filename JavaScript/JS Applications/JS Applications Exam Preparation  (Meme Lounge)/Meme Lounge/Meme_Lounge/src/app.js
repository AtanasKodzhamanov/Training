import {page, render} from "./lib.js"
import { catalogView } from "./views/catalog.js";
import {homeView} from "./views/home.js"

const main = document.querySelector("main");

page(decorateContext);
page ("/", homeView)
page ("/memes", catalogView)
page ("/mems/:id", () => console.log("details"))
page ("/login", () => console.log("login"))
page ("/register", () => console.log("reg"))
page ("/create", () => console.log("reg"))
page ("/profile", () => console.log("reg"))


page.start()

function decorateContext(ctx, next){
    ctx.render = renderMain;
    next();
}

function renderMain(templateResult){
    render(templateResult, main);
}