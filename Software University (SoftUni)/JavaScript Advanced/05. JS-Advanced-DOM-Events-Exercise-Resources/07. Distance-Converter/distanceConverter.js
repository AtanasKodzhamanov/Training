function attachEventsListeners() {
    let [inputField, outputField]=document.querySelectorAll('input[type="text"]')
    let inputUnits=document.querySelector('#inputUnits')
    let outUnits=document.querySelector('#outputUnits')

    let buttonEl=document.getElementById("convert")

    buttonEl.addEventListener("click",onClick)

    function onClick(event){
        let convert = Number(inputField.value)
        let result=0

        //conversion calc

    }


}