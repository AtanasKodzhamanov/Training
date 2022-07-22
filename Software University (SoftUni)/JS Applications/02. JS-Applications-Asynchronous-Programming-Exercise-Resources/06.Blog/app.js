function attachEvents() {
    
    let urlPosts = "http://localhost:3030/jsonstore/blog/posts/"
    let urlComments = "http://localhost:3030/jsonstore/blog/comments"

    const loadBtn=document.getElementById("btnLoadPosts")
    loadBtn.addEventListener('click',toggle);

    const postsElement=document.getElementById("posts") 

    const viewBtn=document.getElementById("btnViewPost")
    viewBtn.addEventListener('click',getId);
    
    const posttextElement=document.getElementById("post-body")
    const commentstextElement=document.getElementById("post-comments")

    async function toggle(){
        const response = await fetch(urlPosts)
        const data = await response.json()
        //console.log(data)
        postsElement.replaceChildren()

        Object.values(data).forEach(a =>{
            //console.log(a.id)
            let optionElement=document.createElement("option")
            optionElement.textContent=a.title
            optionElement.value=a.id
            postsElement.appendChild(optionElement)
        })
    }

    async function getId(){
        posttextElement.replaceChildren()
        commentstextElement.replaceChildren()

        const selectedId = document.getElementById("posts").value
        console.log(selectedId)
        const urlPost= urlPosts + selectedId

        console.log(urlPost)
        const responsePost = await fetch(urlPost)
        const dataPost = await responsePost.json()
        console.log(dataPost)

        posttextElement.textContent=dataPost.body

        const responseComments = await fetch(urlComments)
        const dataComments = await responseComments.json()

        Object.values(dataComments).forEach(a =>{
            //console.log("FLAG1: "+a.postId)
            //console.log("FLAG2: "+dataPost.id)
            if(a.postId==dataPost.id){
               console.log(a.text) 
               let li=document.createElement("li")
               li.textContent=a.text
               commentstextElement.appendChild(li)
            }
            
        })

    }





    
    
}

attachEvents();