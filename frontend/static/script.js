// frontend/script.js

// Load Products
if (document.getElementById("product-list")) {
  fetch('http://127.0.0.1:8000/api/amazon/products/')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("product-list");
      data.forEach(p => {
        list.innerHTML += `
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h5>${p.name}</h5>
                <p>Price: ₹${p.price}</p>
                <button class="btn btn-sm btn-success" onclick="selectProduct(${p.id})">Buy</button>
              </div>
            </div>
          </div>`;
      });
    });
}

// Store selected product
function selectProduct(id) {
  localStorage.setItem("product_id", id);
  window.location.href = "checkout.html";
}

// Checkout Form Submission
if (document.getElementById("checkout-form")) {
  document.getElementById("checkout-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const name = document.getElementById("customer-name").value;
    const email = document.getElementById("customer-email").value;
    const product_id = document.getElementById("product-id").value;
    const quantity = document.getElementById("quantity").value;

    // Save Customer
    let res = await fetch('http://127.0.0.1:8000/api/amazon/customers/', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email })
    });
    let customer = await res.json();

    // Save Order
    res = await fetch('http://127.0.0.1:8000/api/amazon/orders/', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        customer: customer.id,
        product: product_id,
        quantity,
        total_price: quantity * 100  // Dummy price logic
      })
    });
    const order = await res.json();

    // VendorPay payment
    res = await fetch('http://127.0.0.1:8000/api/vendorpay/process/', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ order_id: order.id })
    });

    const txn = await res.json();
    localStorage.setItem("txn", JSON.stringify(txn));
    window.location.href = "success.html";
  });
}

// Show Transaction Summary
if (document.getElementById("transaction-summary")) {
  const txn = JSON.parse(localStorage.getItem("txn"));
  document.getElementById("transaction-summary").innerHTML = `
    <p><strong>Order ID:</strong> ${txn.order_id}</p>
    <p><strong>Total:</strong> ₹${txn.amount}</p>
    <p><strong>Platform Fee:</strong> ₹${txn.platform_fee}</p>
    <p><strong>VendorPay Fee:</strong> ₹${txn.vendorpay_fee}</p>
    <p><strong>Merchant Share:</strong> ₹${txn.merchant_share}</p>
  `;
}
