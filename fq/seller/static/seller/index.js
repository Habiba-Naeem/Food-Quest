document.addEventListener('DOMContentLoaded', () => {

})
window.onload = function () {
    getlist();
}
function getlist() {
    fetch(`getlist`)
        .then(response => {
            console.log('Response:', response)
            return response.json();
        })
        .then(data => {
            console.log(data.itemlist);
            data.itemlist.forEach(addlistmemeber);
        })
};

function addlistmemeber(member) {
    console.log("member:")
    console.log(member);
    const list = document.getElementById('dish-list');
    itemdiv = document.createElement('div');
    itemdiv.dataset.dish_id = member["dish_id"];
    itemdiv.dataset.dish_name = member["dish_name"];
    itemdiv.className = "shadow-lg p-3 mb-3 bg-white rounded m-4";
    itemp = document.createElement('p');
    item = document.createElement('b');
    br = document.createElement('br');
    button = document.createElement("button");
    button.className = "rounded overall cartbtn border-0 float-right p-1 details_button";
    button.innerHTML = "View";
    item.innerHTML = member["dish_name"];
    item.className = "dish-list-item";
    item.href = "#";
    itemdiv.append(button);
    itemdiv.append(item);
    itemdiv.append(itemp);
    list.append(itemdiv);
};

document.addEventListener('click', event => {
    console.log("buton clik")
    const element = event.target;
    console.log(element)
    if (element.className === "rounded overall cartbtn border-0 float-right p-1 details_button") {
        //itemdiv = element.parentElement;
        var itemdiv = element.parentElement;
        console.log(itemdiv)
        var dish_name = itemdiv.dataset.dish_name;
        var dish_id = itemdiv.dataset.dish_id;
        console.log(dish_name);
        console.log(dish_id);
        getItem(dish_name, dish_id);
    }
});
function getItem(dish_name, dish_id) {
    fetch(`get${dish_id}`)
        .then(response => {
            console.log('Response:', response)
            return response.json();
        })
        .then(data => {
            console.log("here")
            console.log(data.item["name"])
            addItem(data.item, dish_id);
        })
};

function addItem(content, dish_id) {
    console.log(content["name"]);
    console.log(content["summary"]);
    console.log(content["nationality"]);
    console.log(content["no_of_serving"]);
    console.log(content["picture"]);
    console.log(content["glutten_free"]);
    console.log(content["customizable"]);
    console.log(content["price"]);

    const namediv = document.createElement('div');
    namediv.className = "namediv";
    const name = document.createElement('p');
    name.className = "dish-name";
    name.innerHTML = content["name"];
    namediv.append(name);

    const summarydiv = document.createElement('div');
    summarydiv.className = "summarydiv";
    const summary = document.createElement('p');
    summary.className = "dish-summary";
    summary.innerHTML = content["summary"];
    summarydiv.append(summary);

    const nationalitydiv = document.createElement('div');
    nationalitydiv.className = "nationalitydiv";
    const nationality = document.createElement('p');
    nationality.className = "dish-nationality";
    nationality.innerHTML = content["nationality"];
    nationalitydiv.append(nationality);

    const no_of_servingdiv = document.createElement('div');
    no_of_servingdiv.className = "no_of_servingdiv";
    const no_of_serving = document.createElement('p');
    no_of_serving.className = "dish-no_of_serving";
    no_of_serving.innerHTML = content["no_of_serving"];
    no_of_servingdiv.append(no_of_serving);

    const glutten_freediv = document.createElement('div');
    glutten_freediv.className = "glutten_freediv";
    const glutten_free = document.createElement('p');
    glutten_free.className = "glutten_free-name";
    glutten_free.innerHTML = content["glutten_free"];
    glutten_freediv.append(glutten_free);

    const customizablediv = document.createElement('div');
    customizablediv.className = "customizablediv";
    const customizable = document.createElement('p');
    customizable.className = "customizable-name";
    customizable.innerHTML = content["customizable"];
    customizablediv.append(customizable);

    const pricediv = document.createElement('div');
    pricediv.className = "pricediv";
    const price = document.createElement('p');
    price.className = "dish-price-name";
    price.innerHTML = content["price"];
    pricediv.append(price);
    console.log("appendingdone");

    console.log("In append function");

    const dishdiv = document.createElement('div');
    console.log(dishdiv)

    dishdiv.append(namediv);
    dishdiv.append(summarydiv);
    dishdiv.append(nationalitydiv);
    dishdiv.append(no_of_servingdiv);
    dishdiv.append(glutten_freediv);
    dishdiv.append(customizablediv);
    dishdiv.append(pricediv)
    console.log("appended to main div");
    display_items(content["name"], dish_id);
    //console.log(document.getElementById('testing').innerHTML);
}


function display_items(dish_name, dish_id) {
    // Open new request to get render page.
    console.log("ok");

    const request = new XMLHttpRequest();
    // request.open('GET', '/seller/' + seller + '/' + dish_name);
    request.open(`GET`, `/seller/${dish_id}`, true);
    //request.open('GET', `/price/${item_name}/${size}`, true)
    request.onload = () => { window.location.replace(`${dish_id}`) };
    request.send();
    console.log("ok2")
}