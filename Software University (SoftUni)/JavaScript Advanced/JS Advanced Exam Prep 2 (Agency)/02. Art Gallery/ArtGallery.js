class ArtGallery{
    constructor(creator){
        this.creator=creator
        this.possibleArticles = { "picture":200,"photo":50,"item":250 }
        this.listOfArticles = []
        this.guests = []
    }

    addArticle(articleModel, articleName, quantity ){
        articleModel=articleModel.toLowerCase()
        
        if(!this.possibleArticles[articleModel]){
            console.log("test")
            throw new Error("This article model is not included in this gallery!")
        }
        
        let isInTheArr=false

        for (let element of this.listOfArticles){
            if(element.articleName==articleName && element.articleModel==articleModel){
                element.quantity += Number(quantity)
                isInTheArr=true
            }
        }
        if(!isInTheArr){
            this.listOfArticles.push({articleModel,articleName,quantity})
        }
        console.log(`Successfully added article ${articleName} with a new quantity- ${quantity}.`)
        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`
    }

    inviteGuest(guestName, personality){
        for (let guest of this.guests){
            if(guest.guestName===guestName){
                throw new Error(`${guestName} has already been invited.`)
            }
        }
        let pointz=50
        if(personality=="Vip"){
            pointz=500
        }
        else if(personality=="Middle"){
            pointz=250
        }


        this.guests.push({guestName,points: pointz, purchaseArticle: 0})
        return `You have successfully invited ${guestName}!`
    }

    buyArticle(articleModel,articleName, guestName){
        
        let article
        let guest 

        let articlePresent=false
        for (let element of this.listOfArticles){
            if(element.articleName==articleName && element.articleModel==articleModel){
                articlePresent=true
                article=element 
            }
        }
        if(articlePresent==false){
            throw new Error("This article is not found.")
        }
        if(article.quantity<=0){
            return `The ${articleName} is not available.`
        }

        let guestInvite=false
        for (const element of this.guests){
            if(element.guestName==guestName){
                guestInvite=true
                guest=element
                
            }
        }
        if(guestInvite==false){
            return "This guest is not invited"
        }
        let guestPoints=guest.points
        if(this.possibleArticles[articleModel]<=guestPoints){
            guest.points=guestPoints-this.possibleArticles[articleModel]
            article.quantity=article.quantity-1
            guest.purchaseArticle=guest.purchaseArticle+1
            return `${guestName} successfully purchased the article worth ${this.possibleArticles[articleModel]} points.`
        }
        else{
            return "You need to more points to purchase the article."
        }
        

       
        

    }

    showGalleryInfo(criteria){
        let result =[]
        if(criteria==="article"){
            result.push("Articles information:")
            for(const element in this.listOfArticles){
                result.push(`${this.listOfArticles[element].articleModel} - ${this.listOfArticles[element].articleName} - ${this.listOfArticles[element].quantity}`)
            }
            
        }
        if(criteria==="guest"){
            result.push("Guests information:")
            for(let element in this.guests){
                result.push(`${this.guests[element].guestName} - ${this.guests[element].purchaseArticle}`)
            }
        }

        return result.join(`\n`)
    }
}


const artGallery = new ArtGallery('Curtis Mayfield'); 
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('picture', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
artGallery.buyArticle('picture', 'Mona Liza', 'John');
artGallery.buyArticle('item', 'Ancient vase', 'Peter');
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));


