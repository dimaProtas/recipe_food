let nameProduct = document.querySelector('#name_product')
let formProduct = document.querySelector('#formProduct')



const addName = () => {
    let csrftoken = formProduct.querySelector('[name=csrfmiddlewaretoken]').value
    let name = nameProduct.value

    fetch('http://127.0.0.1:8000/add_product/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'name': name
        })
    })
    .then(responce => {
        if (!responce.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return responce.json()
    })
    .then(data => {
        if (data.succes == 'OK') {
            nameProduct.value = ''  

            let containerProduct = document.querySelector('#containerProduct')
            let elP = document.createElement('p')
            elP.setAttribute('class', 'product')
            let textElP = document.createTextNode(`Приготовлено блюд 0 c продуктом "${name}"`)
            elP.appendChild(textElP)

            containerProduct.appendChild(elP)
        } else {
            let formProduct = document.querySelector('#formProduct')
            let body = document.querySelector('body')

            let elSpan = document.createElement('span')
            elSpan.style.color = 'red'
            let textSpan = document.createTextNode(data.error)
            elSpan.appendChild(textSpan)

            body.insertBefore(elSpan, formProduct)
        }
    })
    .catch(error => {
        console.log(`Error:`, error)
    })
}


let name_product = document.querySelector('#name_product')

const valideteInput = (event) => {
    
    if (name_product.value.length) {
        let spanEl = document.querySelector('span')
        if (spanEl) {
            spanEl.remove()
        }
    }
}


name_product.addEventListener('input', valideteInput)
