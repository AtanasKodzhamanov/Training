window.addEventListener('load', solve);

function solve() {
    //get input elements
    const productTypeEl=document.getElementById("type-product")
    const descriptionEl=document.getElementById("description")
    const clientNameEl=document.getElementById("client-name")
    const phoneEl=document.getElementById("client-phone")

    //get other forms
    const receivedOrdersEl=document.getElementById("received-orders")
    const completedOrdersEl=document.getElementById("completed-orders")

    //get buttons
    submitBtn=document.querySelector("#right > form > button")
    clearBtn=document.querySelector("#completed-orders > button")

    clearBtn.addEventListener("click",(e)=>{
        e.preventDefault();
        let containers= document.querySelectorAll("#completed-orders > div")
        for(let i in containers){
            containers[i].remove()
        }
    })

    submitBtn.addEventListener("click",(e)=>{
        e.preventDefault();
        
        if(clientNameEl.value==="" || descriptionEl.value==="" || phoneEl.value===""){
            return
        }

        let containerEl=document.createElement("div")
        containerEl.classList.add("container")
        let h2El=document.createElement("h2")
        let h3El=document.createElement("h3")
        let h4El=document.createElement("h4")

        let startBtn=document.createElement("button")
        let finishBtn=document.createElement("button")
        startBtn.classList.add("start-btn")
        finishBtn.classList.add("finish-btn")

        h2El.innerText="Product type for repair: "+productTypeEl.value
        h3El.innerText="Client information: "+clientNameEl.value+", "+phoneEl.value
        h4El.innerText="Description of the problem: "+descriptionEl.value
        startBtn.innerText="Start repair"
        finishBtn.innerText="Finish repair"
        finishBtn.disabled = true

        clientNameEl.value=""
        descriptionEl.value=""
        phoneEl.value=""


        containerEl.appendChild(h2El)
        containerEl.appendChild(h3El)
        containerEl.appendChild(h4El)
        containerEl.appendChild(startBtn)
        containerEl.appendChild(finishBtn)
        receivedOrdersEl.appendChild(containerEl)

        startBtn.addEventListener("click",(e)=>{
            finishBtn.disabled = false
            startBtn.disabled = true
        })

        finishBtn.addEventListener("click",(e)=>{
            completedOrdersEl.appendChild(e.target.parentNode)
            finishBtn.remove()
            startBtn.remove()
        })

    })

}