function updateTextInput(val) {
          document.getElementById('textmontant').value=val;

        }

function updateTextInput2(val) {
  document.getElementById('textduree').value=val;
}

 document
      .querySelector("#montant")
      .addEventListener("click", e => {
        fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({
              montant: Number(e.target.checked)
            })
          })
          .then(res => {
            if (!res.ok) {
              throw Error(res.status);
            }

            return res.json();
          })
          .then(({data: {val}}) => {
            console.log(val);
          })
          .catch(err => console.error(err))
        ;
      })
    ;




document
      .querySelector("#duree")
      .addEventListener("click", e => {
        fetch("/", {
            method: "POST",
            headers: {
              "Accept": "application/json",
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              duree: Number(e.target.checked)
            })
          })
          .then(res => {
            if (!res.ok) {
              throw Error(res.status);
            }

            return res.json();
          })
          .then(({data: {val}}) => {
            console.log(val);
          })
          .catch(err => console.error(err))
        ;
      })
    ;



document
      .querySelector("#taux-interet")
      .addEventListener("click", e => {
        fetch("/", {
            method: "POST",
            headers: {
              "Accept": "application/json",
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              taux_interet: Number(e.target.checked)
            })
          })
          .then(res => {
            if (!res.ok) {
              throw Error(res.status);
            }

            return res.json();
          })
          .then(({data: {val}}) => {
            console.log(val);
          })
          .catch(err => console.error(err))
        ;
      })
    ;


document
      .querySelector("#taux-assu")
      .addEventListener("click", e => {
        fetch("/", {
            method: "POST",
            headers: {
              "Accept": "application/json",
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              taux_assu: Number(e.target.checked)
            })
          })
          .then(res => {
            if (!res.ok) {
              throw Error(res.status);
            }

            return res.json();
          })
          .then(({data: {val}}) => {
            console.log(val);
          })
          .catch(err => console.error(err))
        ;
      })
    ;