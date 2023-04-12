function subtract() {
    let resultElement=document.getElementById("result")
    let oneElement=document.getElementById("firstNumber")
    let twoElement=document.getElementById("secondNumber")
    console.log(oneElement.value)
    resultElement.textContent=Number(oneElement.value)-Number(twoElement.value)
}