import { html } from '../../node_modules/lit-html/lit-html.js';
import { createEvent } from '../api/data.js';

let createTemplate = (onSubmit) => html`
<section id="create">
          <div class="form">
            <h2>Add Event</h2>
            <form @submit=${onSubmit} class="create-form">
              <input
                type="text"
                name="name"
                id="name"
                placeholder="Event"
              />
              <input
                type="text"
                name="imageUrl"
                id="event-image"
                placeholder="Event Image URL"
              />
              <input
                type="text"
                name="category"
                id="event-category"
                placeholder="Category"
              />


              <textarea
                id="event-description"
                name="description"
                placeholder="Description"
                rows="5"
                cols="50"
              ></textarea>
              
              <input
              type="text"
              name="date"
              id="date"
              placeholder="When?"
            />

              <button type="submit">Add</button>
            </form>
          </div>
        </section>

`;


export function createPage(ctx) {
    ctx.render(createTemplate(onSubmit))

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let name = formData.get("name").trim();
        let description = formData.get("description").trim();
        let date = formData.get("date").trim();
        let imageUrl = formData.get("imageUrl").trim();
        let category = formData.get("category").trim();


        if (name == "" || description == "" || imageUrl == "" || date == "" || category == "") {
            return alert("All fields are required!");
        }

        await createEvent({
            name,
            description,
            imageUrl,
            category,
            date

        })

        ctx.page.redirect("/")
    }
}