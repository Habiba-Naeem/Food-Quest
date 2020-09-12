document.addEventListener('DOMContentLoaded', () => {
    alert("I am working!");
    /* document.addEventListener('click', event => {
         const element = event.target;
         if (element.className === 'menu') {
 
             getlist();
         }
     })*/
    //  const menu = document.getElementById('menu');
    document.getElementById('menu').onclick = function () {
        //const seller_name = document.getElementById('seller_name').innerHTML;
        console.log(document.getElementById('seller-name').innerHTML);
    }
    // getitems();

    /* function addlistmemeber(member) {
         list = document.getElementById('dish-list');
         itemdiv = document.createElement('div');
         item = document.createElement('p');
         item.innerHTML = member;
         item.className = "list-item";
         itemdiv.append(item);
         list.append(itemdiv);
     }*/

    /* function getitems() {
         //const start = 1;
         // const end = 10;
         //counter = end + 1;
         seller_name = document.getElementById('seller_name').innerHTML;
         // Get new posts and add posts
         fetch(`/getitems`)
             .then(response => response.json())
             .then(data => {
                 //data.items.forEach(addItem);
             })
     };
 
     function addItem(content) {
         item = document.createElement('div');
         item.className = "item";
 
 
     }
 */
})

function getlist() {
    //seller_name = document.getElementById('seller_name').innerHTML;
    //console.log(seller_name);
    // fetch(`${seller_name}/getlist`)
    fetch(`/getlist`)
        .then(response => {
            console.log('Response:', response)
            return response.json();
        })
        .then(data => {
            console.log(data.itemlist);
            // data = JSON.parse(data);
            // data.itemlist.forEach(addlistmemeber);
            //console.log(((data.itemlist)[0]).toString());
        })

}

function addlistmemeber(member) {
    console.log(member);
}
