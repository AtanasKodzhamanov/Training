function toggle() {
    let buttonElement=document.getElementsByClassName("button")[0]
    let boxElement=document.getElementById("extra")

    if(buttonElement.textContent==="More"){
        buttonElement.textContent="Less"
        boxElement.style.display="block"
        
    }
    else{
        buttonElement.textContent="More"
        boxElement.style.display="none"
    }
}