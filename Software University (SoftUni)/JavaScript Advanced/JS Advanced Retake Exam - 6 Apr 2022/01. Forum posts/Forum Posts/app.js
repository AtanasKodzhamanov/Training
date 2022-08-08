window.addEventListener("load", solve);

function solve() {
    
    //get elements
    let titleElement=document.getElementById("post-title")
    let categoryElement=document.getElementById("post-category")
    let contentElement=document.getElementById("post-content")
    let ulElement=document.getElementById("review-list")
    let uploadedEl=document.getElementById("published-list")

    //get buttons
    let publishBtn=document.getElementById("publish-btn")
    let clearBtn=document.getElementById("clear-btn")

    //clear
    clearBtn.addEventListener("click",(e)=>{
      uploadedEl.innerHTML=""
    })

    //attach eventListener
    publishBtn.addEventListener("click",(e)=>{
      e.preventDefault()
      if(titleElement.value==="" || categoryElement.value==="" || contentElement.value===""){
        return
      }


      let li=document.createElement("li")
      li.classList.add("rpost")

      let article=document.createElement("article")

      let hElement=document.createElement("h4")
      let p1Element=document.createElement("p")
      let p2Element=document.createElement("p")
      
      let buttonEdit=document.createElement("button")
      buttonEdit.classList.add("action-btn", "edit")
      buttonEdit.textContent="Edit"

      let buttonApprove=document.createElement("button")
      buttonApprove.classList.add("action-btn","approve") 
      //Exercise suggest there should be more to the class, but it gives an error
      buttonApprove.textContent="Approve"

      hElement.textContent=titleElement.value 
      p1Element.textContent="Category: "+ categoryElement.value
      p2Element.textContent="Content: "+ contentElement.value

      titleElement.value=""
      categoryElement.value=""
      contentElement.value=""
      
      article.appendChild(hElement)
      article.appendChild(p1Element)
      article.appendChild(p2Element)
      li.appendChild(article)
      li.appendChild(buttonApprove)
      li.appendChild(buttonEdit)
  
      ulElement.appendChild(li)

      buttonEdit.addEventListener("click",(e)=>{
        titleElement.value= hElement.textContent
        //hack due to time pressure
        categoryElement.value=p1Element.textContent.substring(10)
        contentElement.value=p2Element.textContent.substring(9)

        e.target.parentNode.remove()
      })
      buttonApprove.addEventListener("click",(e)=>{
        uploadedEl.appendChild(e.target.parentNode)
        //the operation above is not copying, it is moving
        li.querySelector(".edit").remove()
        li.querySelector(".approve").remove()
      })

    })


}
