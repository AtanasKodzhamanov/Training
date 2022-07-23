function search() {
   let liElements = document.getElementsByTagName("li")
   let inputText = document.getElementById("searchText").value
   let count = 0

   for (let element of liElements) {

      element.style.fontWeight = ""
      element.style.textDecoration = ""

      if (element.textContent.includes(inputText)) {
         element.style.fontWeight = "bold"
         element.style.textDecoration = "underline"
         count++
      }

   }
   document.getElementById("result").textContent = `${count} matches found`
}
