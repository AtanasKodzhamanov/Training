function solve() {
    fnameEl = document.getElementById("fname");
    lnameEl = document.getElementById("lname");
    emailEl = document.getElementById("email");
    birthEl = document.getElementById("birth");
    positionEl = document.getElementById("position");
    salaryEl = document.getElementById("salary");

    tableEl = document.getElementById("tbody");
    sumEl = document.getElementById("sum");

    addBtn = document.getElementById("add-worker");

    addBtn.addEventListener("click", (e) => {
        e.preventDefault();
        fname = fnameEl.value;
        lname = lnameEl.value;
        email = emailEl.value;
        birth = birthEl.value;
        position = positionEl.value;
        salary = salaryEl.value;

        if (
            fname == "" ||
            lname == "" ||
            email == "" ||
            birth == "" ||
            position == "" ||
            salary == ""
        ) {
            return;
        }

        fnameEl.value = "";
        lnameEl.value = "";
        emailEl.value = "";
        birthEl.value = "";
        positionEl.value = "";
        salaryEl.value = "";

        let tr = document.createElement("tr");
        let td1 = document.createElement("td");
        let td2 = document.createElement("td");
        let td3 = document.createElement("td");
        let td4 = document.createElement("td");
        let td5 = document.createElement("td");
        let td6 = document.createElement("td");
        let td7 = document.createElement("td");
        let buttonFire = document.createElement("button");
        let buttonEdit = document.createElement("button");
        buttonFire.classList.add("fired");
        buttonEdit.classList.add("edit");

        buttonFire.textContent = "Fired";
        buttonEdit.textContent = "Edit";

        td1.textContent = fname;
        td2.textContent = lname;
        td3.textContent = email;
        td4.textContent = birth;
        td5.textContent = position;
        td6.textContent = salary;

        td7.appendChild(buttonFire);
        td7.appendChild(buttonEdit);
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tr.appendChild(td4);
        tr.appendChild(td5);
        tr.appendChild(td6);
        tr.appendChild(td7);
        tableEl.appendChild(tr);

        
        sumEl.textContent = (Number(sumEl.textContent) + Number(salary)).toFixed(2);


                buttonEdit.addEventListener("click", (e) => {
                e.preventDefault();
                //console.log(e.target.parentNode.parentNode.childNodes) //fix code below
                let children=e.target.parentNode.parentNode.childNodes
                let i=0
                for (const element of children) {
                    console.log(element.textContent);
                    if(i==0){
                        fnameEl.value = element.textContent;
                    }
                    if(i==1){
                        lnameEl.value = element.textContent;
                    }
                    if(i==2){
                        emailEl.value = element.textContent;
                    }
                    if(i==3){
                        birthEl.value = element.textContent;
                    }
                    if(i==4){
                        positionEl.value = element.textContent;
                    }
                    if(i==5){
                        salaryEl.value = element.textContent;
                    }
                    if(i==6){break}
                  }
  
                sumEl.textContent = (Number(sumEl.textContent) - Number(salaryEl.textContent)).toFixed(2);
                e.target.parentNode.parentNode.remove();
            });

            buttonFire.addEventListener("click", (ev) => {
                ev.preventDefault();
                console.log(sumEl.textContent);
                sumEl.textContent = (Number(sumEl.textContent) - Number(salary)).toFixed(2);
                console.log(sumEl.textContent);
                e.target.parentNode.parentNode.remove();
            });
    });

  
}
solve();
