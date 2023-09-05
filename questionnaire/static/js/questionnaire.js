


class Division {
    constructor(id, name) {
        this.id     = id;
        this.name   = name;
    }
}

function setCompanies(division) {
    let xhr = new XMLHttpRequest();
    const currentURL = new URL(window.location.href);
    const companiesListURL = new URL(currentURL.origin + `/questionnaire/api/v1/companies_from/${division.id}`)
    console.log(companiesListURL.href)
    xhr.open('GET', companiesListURL.href);
    xhr.send();
    xhr.onload = function() {
        if (xhr.status != 200) { 
            alert(`Ошибка ${xhr.status}: ${xhr.statusText}`);
        } 
        else { 
            response_ = JSON.parse(xhr.response)
            const select_companies = document.getElementById('id_company');
            while (select_companies.lastChild)
                select_companies.removeChild(select_companies.lastChild)

            for (let i = 0; i < response_.length; ++i) {
                const company_info = response_[i];
                const newOption = document.createElement("option");
                newOption.value = company_info.id;
                newOption.division = company_info.division;
                newOption.innerText = company_info.name;
                select_companies.appendChild(newOption);
            }
        }
    };
}


document.getElementById('id_division').onchange = function(select) {
    const divisionOption = document.getElementById('id_division').querySelector(`option[value='${document.getElementById('id_division').value}']`)
    division = new Division(Number(divisionOption.value), divisionOption.innerText);
    setCompanies(division)
    console.log(`Division: ${division}`)
}