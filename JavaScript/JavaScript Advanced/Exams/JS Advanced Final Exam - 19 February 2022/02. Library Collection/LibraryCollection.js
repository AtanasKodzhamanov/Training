class LibraryCollection {
    constructor(capacity) {
        this.capacity = capacity
        this.books = []
    }
    addBook(bookName, bookAuthor) {
        if (this.books.length == this.capacity) {
            throw new Error("Not enough space in the collection.")
        }
        this.books.push({ bookName, bookAuthor, payed: false })
        return `The ${bookName}, with an author ${bookAuthor}, collect.`
    }
    payBook(bookName) {
        let book = []
        let exists = false
        for (let i in this.books) {
            if (this.books[i].bookName === bookName) {
                book = this.books[i]
                exists = true
            }
        }
        if (exists == false) {
            throw new Error(`${bookName} is not in the collection.`)
        }
        if (book.payed == true) {
            throw new Error(`${bookName} has already been paid.`)
        }
        book.payed = true
        return `${bookName} has been successfully paid.`
    }
    removeBook(bookName) {
        let book = []
        let exists = false
        let index = -1
        for (let i in this.books) {
            if (this.books[i].bookName === bookName) {
                book = this.books[i]
                exists = true
                index = i
            }
        }
        if (exists == false) {
            throw new Error("The book, you're looking for, is not found.")
        }
        if (book.payed == false) {
            throw new Error(`${bookName} need to be paid before removing from the collection.`)
        }
        else {
            this.books.splice(index, 1)
            return `${bookName} remove from the collection.`
        }


    }
    // Fails a test somewhere
    // getStatistics(bookAuthor) {
    //     let returnArr = []
    //     let sortedBook = this.books.sort((a, b) => a.bookName.localeCompare(b.bookName));
    //     if (bookAuthor==undefined) {
    //         returnArr.push(`The book collection has ${this.capacity - this.books.length} empty spots left.`)

    //         for (let i in sortedBook) {
    //             let paid = "Not Paid"
    //             if (sortedBook[i].payed == true) {
    //                 paid = "Has Paid"
    //             }
    //             returnArr.push(`${sortedBook[i].bookName} == ${sortedBook[i].bookAuthor} - ${paid}.`)
    //         }

    //         return returnArr.join(`\n`).trim()
    //     }
    //     else {
    //         let returnArr = []
    //         let book = []
    //         let exists = false
    //         let index = -1
    //         let paid = "Not Paid"
    //         for (let i in sortedBook) {
    //             if (sortedBook[i].bookAuthor === bookAuthor) {
    //                 book = sortedBook[i]
    //                 exists = true
    //                 index = i
    //                 if (sortedBook[i].payed == true) {
    //                     paid = "Has Paid"
    //                 }
    //                 returnArr.push(`${book.bookName} == ${bookAuthor} - ${paid}.`)
    //             }


    //         } if (exists == false) {
    //                 return `${bookAuthor} is not in the collection.`
    //             }
    //         else{return returnArr.join(`\n`).trim()}
    //     }
    // }
    getStatistics(bookAuthor) {
        if (!bookAuthor) {
            let sortedBook = this.books.sort((a, b) => a.bookName.localeCompare(b.bookName));
            let result = [];
            result.push(`The book collection has ${this.capacity - this.books.length} empty spots left.`);
            sortedBook.map((b) => {
                let paid = b.payed ? 'Has Paid' : 'Not Paid';
                result.push(`${b.bookName} == ${b.bookAuthor} - ${paid}.`);
            });
            return result.join('\n').trim();
        } else {
            let findBook = this.books.find(b => b.bookAuthor == bookAuthor);

            if (findBook) {
                let result = [];
                let paid = findBook.payed ? 'Has Paid' : 'Not Paid';
                result.push(`${findBook.bookName} == ${findBook.bookAuthor} - ${paid}.`);
                return result.join('\n').trim();
            } else {
                throw new Error(`${bookAuthor} is not in the collection.`)
            }
        }
    }
}
let library = new LibraryCollection(10);

console.log(library.addBook("Don Quixote", "Miguel de Cervantes"))
console.log(library.payBook("Don Quixote"))
console.log(library.addBook("In Search of Lost Time", "Marcel Proust"))
console.log(library.addBook("Ulysses", "James Joyce"))
console.log(library.addBook("Ulysses2", "James Joyce"))
console.log(library.addBook("Alysses2", "James Joyce"))
console.log("HEre")
console.log(library.getStatistics())
console.log(library.getStatistics("James Joyce"))
console.log("HEre")