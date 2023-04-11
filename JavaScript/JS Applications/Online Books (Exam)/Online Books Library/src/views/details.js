import { html } from "../../node_modules/lit-html/lit-html.js";
import { deleteBook, getBookById, getLikesByBookId, likeBook, getMyLikesByBookId } from "../api/data.js";
import { getUserData } from "../util.js";

let detailsTemplate = (book, isOwner, onDelete, likes, showLikebutton, onLike, onEdit) => html`
<section id="details-page" class="details">
    <div class="book-information">
        <h3>${book.title}</h3>
        <p class="type">Type: ${book.type}</p>
        <p class="img"><img src="${book.imageUrl}"></p>
        <div class="actions">
            ${bookControlsTemplate(book, isOwner, onDelete, onEdit)}
            ${likesControlsTemplate(showLikebutton, onLike)}
            <div class="likes">
                <img class="hearts" src="../images/heart.png" />
                <span id="total-likes">Likes: ${likes}</span>
            </div>
        </div>
    </div>
`;

let bookControlsTemplate = (book, isOwner, onDelete, onEdit) => {
    if (isOwner) {
        return html`
        <a class="button" href="/edit/${book._id}">Edit</a>
        <a @click=${onDelete} class="button" href="javascript:void(0)">Delete</a>`;
    } else {
        return null;
    }
}

let likesControlsTemplate = (showLikebutton, onLike) => {
    if (showLikebutton) {
        return html`
        <a @click=${onLike} class="button" href="javascript:void(0)">Like</a>`;
    } else {
        return null;
    }
}

export async function detailsPage(ctx) {
    let userData = getUserData();
    let [book, likes, hasLike] = await Promise.all([
        getBookById(ctx.params.id),
        getLikesByBookId(ctx.params.id),
        userData ? getMyLikesByBookId(ctx.params.id, userData.id) : 0
    ]);

    let isOwner = userData && userData.id == book._ownerId;
    let showLikebutton = isOwner == false && hasLike == false && userData != null;
    ctx.render(detailsTemplate(book, isOwner, onDelete, likes, showLikebutton, onLike));

    async function onDelete() {
        await deleteBook(ctx.params.id);
        ctx.page.redirect("/");
    }

    async function onLike() {
        await likeBook(ctx.params.id);
        ctx.page.redirect("/details/" + ctx.params.id);
    }
}