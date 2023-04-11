import { render } from "../node_modules/lit-html/lit-html.js";
import { getUserData } from "./util.js";
import page from "../node_modules/page/page.mjs";
import { logout } from "./api/api.js";
import { loginPage } from "./views/login.js";
import { registerPage } from "./views/register.js";
import { homePage } from "./views/home.js";
import { eventsPage } from "./views/events.js";
import { createPage } from "./views/create.js";
import { detailsPage } from "./views/details.js";
import { editPage } from "./views/edit.js";


let root = document.getElementById("site-content");

function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, root);
    ctx.updateUserNav = updateUserNav;

    next()
}

export function updateUserNav() {
    let userData = getUserData();
    console.log(userData)
    if (userData) {
        document.querySelector(".user").style.display = "inline-block";
        document.querySelector(".guest").style.display = "none";
    } else {
        document.querySelector(".user").style.display = "none";
        document.querySelector(".guest").style.display = "inline-block";
    }

}

document.getElementById("logoutBtn").addEventListener("click", (e) => {
    logout();
    updateUserNav()
    page.redirect("/");
})

page(decorateContext);
page("/", homePage);
page("/login", loginPage);
page("/register", registerPage);
page("/events", eventsPage)
page("/create", createPage)
page("/details/:id", detailsPage)
page("/edit/:id", editPage)
updateUserNav()
page.start()