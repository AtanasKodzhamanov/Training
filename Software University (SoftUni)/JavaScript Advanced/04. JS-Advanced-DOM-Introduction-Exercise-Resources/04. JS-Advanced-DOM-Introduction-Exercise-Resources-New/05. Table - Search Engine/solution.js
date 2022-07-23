function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);
   let input = document.getElementById("searchField")
   let rows = document.querySelectorAll("tbody tr")



   function onClick() {
      for(let row of rows){
         console.log(input)
         row.classList.remove("select")
         if(input.value !=="" && row.innerHTML.includes(input.value)){
            console.log("found")
            row.className="select"
         }
         
      }
      input.value=""
   }
}