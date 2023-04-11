import { html } from "../../node_modules/lit-html/lit-html.js";
import { getUserData } from "../util.js";
import { getEventById } from "../api/data.js";
import { deleteEvent } from "../api/data.js";
import { goEvent } from "../api/data.js";
import { getEventCount } from "../api/data.js";
import { getUserGoing } from "../api/data.js";

let detailsTemplate = (event, isOwner, onDelete, onGo, count, showGoButton, eventId) => html`
<section id="details">
<div id="details-wrapper">
  <img id="details-img" src="${event.imageUrl}" alt="example1" />
  <p id="details-title">${event.name}</p>
  <p id="details-category">
    Category: <span id="categories">${event.category}</span>
  </p>
  <p id="details-date">
    Date:<span id="date">${event.date}</span></p>
  <div id="info-wrapper">
    <div id="details-description">
      <span> ${event.description}</span>
    </div>

  </div>

  <h3>Going: <span id="go">${count}</span> times.</h3>

  <!--Edit and Delete are only for creator-->
  <div id="action-buttons">
  ${isOwner ? html`
  <a href="/edit/${event._id}" id="edit-btn">Edit</a>
  <a @click=${onDelete} href="javascript:void(0)" id="delete-btn">Delete</a>` : html``}
  
    <!--Bonus - Only for logged-in users ( not authors )-->
    ${showGoButton ? html`<a @click=${onGo} href="javascript:void(0)" id="go-btn">Going</a>` : html``}
  </div>
</div>
</section>
`;


export async function detailsPage(ctx) {
    let userData = getUserData();
    console.log(ctx.params.id)
    let [event, count, isGoing] = await Promise.all([
        getEventById(ctx.params.id),
        getEventCount(ctx.params.id),
        userData ? getUserGoing(ctx.params.id, userData.id) : 0
    ]);
    let eventId = ctx.params.id;

    let isOwner = userData && userData.id == event._ownerId;

    let showGoButton = isOwner == false && isGoing == false && userData != null;

    ctx.render(detailsTemplate(event, isOwner, onDelete, onGo, count, showGoButton, eventId));

    async function onDelete() {
        let confirmed = confirm("Are you sure you want to delete this event?");
        if (confirmed) {
            await deleteEvent(ctx.params.id);
        }
        ctx.page.redirect("/events/");
    }

    async function onGo() {
        await goEvent(ctx.params.id);
        ctx.page.redirect("/details/" + ctx.params.id);
    }


}