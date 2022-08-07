window.addEventListener('load', solution);

function solution() {
  //Get input elements
  const nameEl = document.querySelector('#fname')
  const emailEl = document.getElementById("email")
  const phoneEl = document.getElementById("phone")
  const addressEl = document.getElementById("address")
  const codeEl = document.getElementById("code")

  //Get form additional elements
  let infoPreview=document.getElementById("infoPreview")
  let blockEl=document.getElementById("block")

  //Get button elements
  const buttonSbmt = document.getElementById("submitBTN")
  const buttonEdit = document.getElementById("editBTN")
  const buttonCont = document.getElementById("continueBTN")

  //Attach event listener and add function logic
  buttonSbmt.addEventListener("click",(e)=>{
    e.preventDefault()
    

    //Can only submit form if email and name are not empty
     if(!nameEl.value || !emailEl.value){
      return
    }

    //Get input values from the forms
    let fname=nameEl.value
    let email=emailEl.value
    let phone=phoneEl.value
    let address=addressEl.value
    let code=codeEl.value

    //Remove input values from the fields

    nameEl.value=""
    emailEl.value=""
    phoneEl.value=""
    addressEl.value=""
    codeEl.value=""

    //Turn off/on buttons
    buttonSbmt.disabled=true
    buttonEdit.disabled=false
    buttonCont.disabled=false

    //Create list elements
    createLi(`Full Name: ${fname}`)
    createLi(`Email: ${email}`)
    createLi(`Phone Number: ${phone}`)
    createLi(`Address: ${address}`)
    createLi(`Postal Code: ${code}`)
    
    buttonEdit.addEventListener("click", (ev)=>{
      buttonEdit.disabled=true
      buttonCont.disabled=true
      nameEl.value=fname
      emailEl.value=email
      phoneEl.value=phone
      addressEl.value=address
      codeEl.value=code
      buttonSbmt.disabled=false
      infoPreview.innerHTML=""
    })
    buttonCont.addEventListener("click",(e)=>{
      blockEl.innerHTML=""
      let lastMessage=document.createElement("h3")
      lastMessage.innerText="Thank you for your reservation!"
      blockEl.appendChild(lastMessage)
    })

    })
  function createLi(line){
  let li=document.createElement("li")
  li.textContent=line 
  infoPreview.appendChild(li)
}
}

