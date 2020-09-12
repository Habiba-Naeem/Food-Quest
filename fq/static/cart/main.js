function count(){
    var count = 0;
    document.querySelectorAll("#product-price").forEach( t =>{
        count = parseFloat(t.dataset.total) + count;
    })
    document.querySelector("#total").textContent = "Rs" + count.toFixed(2);
    document.querySelector("#totalhidden").value = count.toFixed(2);
    document.querySelector("#checkout_total").textContent = "Rs" + count.toFixed(2);
    document.querySelector("#totalhidden2").value = count.toFixed(2);
    
    return count.toFixed(2);    
}

document.addEventListener('click', event => {

    const element = event.target;
    if (element.id === "btn-purchase") {
        var checkoutform = document.getElementById('checkout-form');
        checkoutform.style.display = "block";
    }
})
document.addEventListener('DOMContentLoaded', () => {
    var rows =  document.querySelectorAll(".my-rows");
    var cancel = document.querySelectorAll(".cancel");
    var checkout = document.getElementById('checkout-form');
    console.log(checkout);
    checkout.style.display = "none";
    
    
    rows.forEach( row => {
        const prices = row.querySelector("#product-price");
        console.log(prices)
        const quantity = row.querySelector("#quantity");
        //var total = row.querySelector("#cart-item-total");
        console.log(row)
        prices.textContent = "Rs" +  (prices.dataset.price * parseInt(quantity.value)).toFixed(2);
        prices.setAttribute("data-total", `${(prices.dataset.price * parseInt(quantity.value)).toFixed(2)}`);
        
        quantity.addEventListener("change",()=>{
            console.log(prices)
            prices.textContent = "Rs " +  (prices.dataset.price * parseInt(quantity.value)).toFixed(2);
            prices.setAttribute("data-total", `${(prices.dataset.price * parseInt(quantity.value)).toFixed(2)}`);
            count();
            console.log(row)
            const request = new XMLHttpRequest();
            request.open('GET', `/cart/quantity/${row.id}/${quantity.value}`);

            request.onload = () => {
                const data = JSON.parse(request.responseText);
            };

            request.send();
            return false;
        })
    })
    count();

    cancel.forEach( can =>{
        can.addEventListener("click", ()=>{
            const parent = can.parentNode.parentNode;
            const id = parent.id;
            console.log(id);

            parent.remove();
            count();

            const request = new XMLHttpRequest();
            request.open('GET', `/cart/cancel/${id}`, true);

            request.send();
            return false;
            
        })
    })

    var purchase = document.querySelector(".btn-purchase");
    purchase.addEventListener("click", ()=>{
        checkout.style.display = "block"; 
    })
})