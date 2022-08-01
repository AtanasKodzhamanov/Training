import {html} from "../../node_modules/lit-html/lit-html.js"

const guestLinks = html`
    <!--Only user-->
    <li><a href="#">Create Album</a></li>
    <li><a href="#">Logout</a></li>
`

const userLinks=html`
    <!--Only user-->
    <li><a href="#">Create Album</a></li>
    <li><a href="#">Logout</a></li>
`

const navigationTemplate = (isAuthenticated) => html`
    <nav>
        <img src="./images/headphones.png">
        <a href="#">Home</a>
        <ul>
            <!--All user-->
            <li><a href="#">Catalog</a></li>
            <li><a href="#">Search</a></li>
            ${isAuthenticated
                ? userlinks
                : guestLinks
            }
        </ul>
    </nav>
`;

export const navigationView=(ctx)=>{
    return navigationTemplate()
}