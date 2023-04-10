import {page, render} from "./lib.js"
import { logout} from "./api/users.js"
import { getUserData } from "./util.js";
import {homeView} from "./views/home.js"
import {loginView} from "./views/login.js"
import { registerView } from "./views/register.js";
import {catalogView} from "./views/catalog.js"
import {createView} from "./views/create.js"
import {editView} from "./views/edit.js"
import {profileView} from "./views/profile.js"
import { detailsView } from "./views/details.js";

const main = document.querySelector("main");

document.getElementById("logoutBtn").addEventListener("click", onLogout); 

page(decorateContext);
page ("/", homeView);
page ("/memes", catalogView);
page ("/memes/:id", detailsView)
page ("/login", loginView)
page ("/edit/:id", editView)
page ("/register", registerView)
page ("/create", createView)
page ("/profile", profileView)

updateNav();
page.start()

function decorateContext(ctx, next){
    ctx.render = renderMain;
    ctx.updateNav = updateNav;
    next();
}

function renderMain(templateResult){
    render(templateResult, main);
}

function updateNav(){
    const userData = getUserData();
    if (userData){
        document.querySelector(".user").style.display = "block";
        document.querySelector(".guest").style.display = "none";
        document.querySelector("#user-greeting").textContent = `Welcome, ${userData.username}!`;
    } else {
        document.querySelector(".user").style.display = "none";
        document.querySelector(".guest").style.display = "block";

        

    }
}

function onLogout(){
    logout();
    updateNav();
    page.redirect("/");
}