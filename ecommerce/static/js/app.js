const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const addToCart = (event) => {
    event.preventDefault();
    const product_id = event.target.dataset.productId;
    const url = "/cart/api/";

    $.ajax({
        type: "POST",
        url: url,
        data: {
            "csrfmiddlewaretoken": getCookie("csrftoken"),
            "product_id": product_id,
        },
        success: function(response) {
            $("#cart-item-number").text(response.number_of_items_in_cart);
            alert(response["message"]);
            event.target.disabled = true;
        }
    });
}

const deleteCartItem = (event) => {
    const item_id = event.target.dataset.itemId;

    $.ajax({
        type: "DELETE",
        url: "/cart/api/",
        data: {
            "csrfmiddlewaretoken": getCookie("csrftoken"),
            "item_id": item_id,
        },
        headers:{"X-CSRFToken": getCookie("csrftoken")},
        success: function(response) {
            const element = event.target.parentElement.parentElement.parentElement.parentElement;
            element.parentElement.removeChild(element);
        },
    });
}


const incrementCartItem = (event) => {
    const target = event.currentTarget;
    const item_id = target.dataset.itemId;
    $.ajax({
        type: "PUT",
        url: "/cart/api/",
        data: {
            "csrfmiddlewaretoken": getCookie("csrftoken"),
            "item_id": item_id,
        },
        headers:{"X-CSRFToken": getCookie("csrftoken")},
        success: function(response) {
            const totalPriceTarget = document.getElementById("total-price-span")
            totalPriceTarget.innerText = response.total_price;

            const element = target.parentElement.parentElement;

            const quantityTarget = element.querySelector('.quantity-target');
            quantityTarget.value = response.quantity;

            const TotalProductPriceTarget= element.querySelector('.product-total-price');
            TotalProductPriceTarget.innerText = response.current_product_total_price
        },
    });
}


const addCartButtons = document.querySelectorAll(".btn-cart");
addCartButtons.forEach(button => button.addEventListener("click", addToCart));

const deleteCartItemButtons = document.querySelectorAll(".btn-cart-item-delete");
deleteCartItemButtons.forEach(button => button.addEventListener("click", deleteCartItem));

const incrementCartItemButtons = document.querySelectorAll(".btn-cart-item-increment");
incrementCartItemButtons.forEach(button => button.addEventListener("click", incrementCartItem));


$.ajax({
    type: "GET",
    url: "/cart/api/",
    success: function(response) {
        $("#cart-item-number").text(response.length);
    },
    error: function(response) {
        console.log("no auth")
    }
});
