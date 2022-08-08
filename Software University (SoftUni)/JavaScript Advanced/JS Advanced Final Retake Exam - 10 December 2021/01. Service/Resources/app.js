window.addEventListener('load', solve);

function solve() {
    //Description, client name, and client phone are non-empty strings. If any of them are empty, the program should not do anything. 

    //get input elements
    const productTypeEl=document.getElementById("type-product")
    const descriptionEl=document.getElementById("description")
    const clientNameEl=document.getElementById("client-name")
    const phoneEl=document.getElementById("client-phone")

    //get other forms

    //get buttons
    submitBtn=document.querySelector("#right > form > button")
    
    submitBtn.addEventListener("click",(e)=>{
        console.log(submitBtn)
    })

}