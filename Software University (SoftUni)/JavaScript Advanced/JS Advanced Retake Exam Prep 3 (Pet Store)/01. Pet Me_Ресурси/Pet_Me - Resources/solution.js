function solve() {
    //const fields=document.querySelectorAll("#container input"
    //const input{
    //    name: fields[0]...
    //}
    nameEl=document.querySelector("#container > input[type=text]:nth-child(1)")
    ageEl=document.querySelector("#container > input[type=text]:nth-child(2)")
    kindEl=document.querySelector("#container > input[type=text]:nth-child(3)")
    ownerEl=document.querySelector("#container > input[type=text]:nth-child(4)")

    addBtn=document.querySelector("#container > button")
    adoptionContainer=document.querySelector("#adoption > ul")
    adoptedContainer=document.querySelector("#adopted > ul")

    addBtn.addEventListener("click", (e)=>{
        e.preventDefault()
    
        petname=nameEl.value
        age=Number(ageEl.value)
        kind=kindEl.value
        owner=ownerEl.value

        if(isNaN(age)){ //if isNan() returns false then its a number
            console.log("not a numbeR")
            return 
        }
        if(petname=="" || kind=="" || owner==""){
            console.log("empty")
            return
        }
        nameEl.value=""
        ageEl.value=""
        kindEl.value=""
        ownerEl.value=""

        let li = document.createElement("li")
        let p = document.createElement("p")
        p.innerHTML=`
        <strong>${petname}</strong> is a <strong>${age}</strong> year old <strong>${kind}</strong>
        `
        let span = document.createElement("span")
        span.textContent=`Owner: ${owner}`
        let contactBtn=document.createElement("button")
        contactBtn.textContent="Contact with owner"

        li.appendChild(p)
        li.appendChild(span)
        li.appendChild(contactBtn)
        adoptionContainer.appendChild(li)

        contactBtn.addEventListener("click", (e)=>{
            e.preventDefault()
            contactBtn.textContent="Yes! I take it!"
            

            let div=document.createElement("div")
            let inputField=document.createElement("input")
            inputField.placeholder = "Enter your names"

            div.appendChild(contactBtn)
            div.appendChild(inputField)
            li.appendChild(div)
            
            contactBtn.addEventListener("click",(e)=>{
                e.preventDefault()
                
                let input=document.querySelector("#adoption > ul > li > div > input")
                span.textContent=`New Owner: ${input.value}`
                input.remove()
                e.target.parentNode.remove()
                li.appendChild(contactBtn)

                
                contactBtn.textContent="Checked"
                adoptedContainer.appendChild(li)

                contactBtn.addEventListener("click",fdelete())
                
                fdelete(){
                    e.preventDefault()
                    li.remove()
                })
            })
        })
    })
}

