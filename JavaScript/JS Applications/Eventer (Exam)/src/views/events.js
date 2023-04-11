import { html } from "../../node_modules/lit-html/lit-html.js";

import { getEvents } from "../api/data.js";
import { eventTemplate } from "./event.js";

let eventsTemplate = (events) => html`

        <h2>Current Events</h2>
        <section id="dashboard">
          <!-- Display a div with information about every post (if any)-->
          ${events.length == 0
        ? html`<h4>No Events yet.</h4>`
        : html`${events.map(eventTemplate)}`}}  

        </section>
        
       

`;

export async function eventsPage(ctx) {
    let events = await getEvents();
    console.log(events)
    ctx.render(eventsTemplate(events));
}
