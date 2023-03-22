function solve() {
    fnameEl=document.getElementById("fname")
    lnameEl=document.getElementById("lname")
    emailEl=document.getElementById("email")
    birthEl=document.getElementById("birth")
    positionEl=document.getElementById("position")
    salaryEl=document.getElementById("salary")

    tableEl=document.getElementById("tbody")
    sumEl=document.getElementById("sum")

    addBtn=document.getElementById("add-worker")

    addBtn.addEventListener("click",(e)=>{
        e.preventDefault()
        fname=fnameEl.value
        lname=lnameEl.value
        email=emailEl.value
        birth=birthEl.value
        position=positionEl.value
        salary=salaryEl.value

        //if(fname=="" || lname=="" || email=="" || birth=="" || position=="" || salary==""){
        //    return 
       //}

   
       let tr=document.createElement("tr")
       let td1=document.createElement("td")
       let td2=document.createElement("td")
       let td3=document.createElement("td")
       let td4=document.createElement("td")
       let td5=document.createElement("td")
       let td6=document.createElement("td")
       let td7=document.createElement("td")
       let buttonFire=document.createElement("button")
       let buttonEdit=document.createElement("button")
       buttonFire.classList.add("fired")
       buttonEdit.classList.add("edit")

       buttonFire.textContent="Fired"
       buttonEdit.textContent="Edit"

       td1.textContent=fname
       td2.textContent=lname
       td3.textContent=email
       td4.textContent=birth
       td5.textContent=position
       td6.textContent=salary

       td7.appendChild(buttonFire)
       td7.appendChild(buttonEdit)
       tr.appendChild(td1)
       tr.appendChild(td2)
       tr.appendChild(td3)
       tr.appendChild(td4)
       tr.appendChild(td5)
       tr.appendChild(td6)
       tr.appendChild(td7)
       tableEl.appendChild(tr)

       sumEl.textContent=(Number(sumEl.textContent)+Number(salary)).toFixed(2)
       
            buttonEdit.addEventListener("click", (e)=>{
                
                fnameEl.value=td1.textContent
                lnameEl.value=td2.textContent
                emailEl.value=td3.textContent
                birthEl.value=td4.textContent
                positionEl.value=td5.textContent
                salaryEl.value=td6.textContent
                console.log(sumEl.textContent)
                sumEl.textContent=(Number(sumEl.textContent)-Number(td6.textContent)).toFixed(2)
                console.log(sumEl.textContent)
                e.target.parentNode.parentNode.remove()
            })

            buttonFire.addEventListener("click", (e)=>{
                console.log(sumEl.textContent)
                sumEl.textContent=(Number(sumEl.textContent)-Number(td6.textContent)).toFixed(2)
                console.log(sumEl.textContent)
                e.target.parentNode.parentNode.remove()
            })
            fnameEl.value=""
            lnameEl.value=""
            emailEl.value=""
            birthEl.value=""
            positionEl.value=""
            salaryEl.value=""
     
        })

}
solve();
