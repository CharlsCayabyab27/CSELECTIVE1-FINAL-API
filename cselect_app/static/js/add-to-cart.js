
function addToCart(productName, productPrice) {
    var cartItemsContainer = document.querySelector('.cd-cart-items');

    var cartItem = document.createElement('li');
    cartItem.innerHTML = `
        <span class="cd-qty">1x</span> ${productName}
        <div class="cd-price">$${productPrice.toFixed(2)}</div>
        <a href="#0" class="cd-item-remove cd-img-replace" onclick="removeCartItem(this)">Remove</a>
    `;

    cartItemsContainer.appendChild(cartItem);

    updateCartTotal(productPrice);
}

function updateCartTotal(productPrice) {
    var cartTotalElement = document.getElementById('cart-total');

    var currentTotal = parseFloat(cartTotalElement.textContent.replace('$', ''));

    var newTotal = currentTotal + productPrice;

    cartTotalElement.textContent = `$${newTotal}`;
}

function removeCartItem(removeButton) {
    var cartItem = removeButton.parentNode;

    var itemPrice = parseFloat(cartItem.querySelector('.cd-price').textContent.replace('$', ''));

    cartItem.remove();

    updateCartTotal(-itemPrice);
}
