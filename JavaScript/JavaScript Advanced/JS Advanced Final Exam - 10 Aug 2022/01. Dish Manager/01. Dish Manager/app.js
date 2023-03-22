window.addEventListener("load", solve);

function solve() {
  fnameEl=document.getElementById("first-name")
  lnameEl=document.getElementById("last-name")
  ageEl=document.getElementById("age")
  genderEl=document.getElementById("genderSelect")
  descEl=document.getElementById("task")

  progressEl=document.getElementById("in-progress")
  finishedEl=document.getElementById("finished")

  dishesCountEl=document.getElementById("progress-count")

  submitBtn=document.getElementById("form-btn")
  clearBtn=document.getElementById("clear-btn")

  submitBtn.addEventListener("click",(e)=>{
    e.preventDefault()
    if(fnameEl.value=="" || lnameEl.value=="" ||ageEl.value=="" || descEl.value=="" ){
      return
    }

    let li=document.createElement("li")
    li.classList.add("each-line")
    let articleEl=document.createElement("article")

    let h4=document.createElement("h4")
    let pGender=document.createElement("p")
    let pDesc=document.createElement("p")

    h4.textContent=fnameEl.value+" "+lnameEl.value
    pGender.textContent=genderEl.value+", "+ageEl.value
    pDesc.textContent="Dish description: "+descEl.value

    let editBtn=document.createElement("button")
    let completeBtn=document.createElement("button")
    editBtn.classList.add("edit-btn")
    editBtn.textContent="Edit"
    completeBtn.classList.add("complete-btn")
    completeBtn.textContent="Mark as complete"

    articleEl.appendChild(h4)
    articleEl.appendChild(pGender)
    articleEl.appendChild(pDesc)
    li.appendChild(articleEl)
    li.appendChild(editBtn)
    li.appendChild(completeBtn)
    progressEl.appendChild(li)

    fnameEl.value=""
    lnameEl.value=""
    ageEl.value=""
    descEl.value=""

    dishesCountEl.textContent=Number(Number(dishesCountEl.textContent)+1)

    editBtn.addEventListener("click",(e)=>{
      e.preventDefault()
      fnameEl.value=h4.textContent.split(" ")[0]
      lnameEl.value=h4.textContent.split(" ")[1]
      ageEl.value=pGender.textContent.split(", ")[1]
      genderEl.value=pGender.textContent.split(", ")[0]
      descEl.value=pDesc.textContent.substring(18)

      e.target.parentNode.remove()
      dishesCountEl.textContent=Number(Number(dishesCountEl.textContent)-1)
    })
    completeBtn.addEventListener("click",(e)=>{
      e.preventDefault()
      finishedEl.appendChild(li)

      editBtn.remove()
      completeBtn.remove()
      dishesCountEl.textContent=Number(Number(dishesCountEl.textContent)-1)

    })
    clearBtn.addEventListener("click",(e)=>{
      e.preventDefault()
      finishedEl.innerHTML=""
      
      
    })
  })
}