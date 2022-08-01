import page from "../node_modules/page/page.mjs"
import {homeView} from "./views/homeView.js"
import {renderNavigation} from `./middlewares/renderMiddleware.js`

page(renderNavigation)

page("/",homeView)

page.start()