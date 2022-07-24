function attachEventsListeners() {

    let ratios={
        days:1,
        hours:24,
        minutes:1440,
        seconds:86400
    }

    document.getElementById("daysBtn").addEventListener("click",onConvert)
    document.getElementById("hoursBtn").addEventListener("click",onConvert)
    document.getElementById("minutesBtn").addEventListener("click",onConvert)
    document.getElementById("secondsBtn").addEventListener("click",onConvert)

    function onConvert(event){
        let input= event.target.parentElement.querySelector('input[type="text"]')
        let time = convert (Number(input.value), input.id)

        //add calcs
        
    }
}