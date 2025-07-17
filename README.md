# 💰 Vendor Payment System

A multi-database eCommerce backend system that simulates real-time payments between customers, the VendorPay platform, and merchants. Built using **Django**, **Django REST Framework**, and **MySQL**.

---

## 🔧 Project Features

- 👥 **Customer Orders** from an eCommerce platform (Amazon DB)
- 🧮 **VendorPay Interface** calculates platform & gateway fees
- 💼 **Merchant Wallet** updates after transactions
- 🔄 Real-time fee deduction using **MySQL Triggers**
- 🔗 Integrated with REST API for seamless communication
- 🧪 Modular databases: `amazone_db`, `vendorpay_db`, `merchant_db`

---

## ⚙️ Technologies Used

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **MySQL**
- **HTML, CSS, JavaScript (Frontend)**
- **AJAX / Angular (optional frontend support)**

---

## 🗃️ Database Schema

- **Amazone DB**
  - `Customer`
  - `Order`
  - `Product`

- **VendorPay DB**
  - `Transaction`
  - MySQL Trigger for fee split:
    - 5% Amazone Fee
    - 5% VendorPay Fee
    - 90% to Merchant Wallet

- **Merchant DB**
  - `Merchant`
  - `Wallet`

---

## 🚀 How It Works

1. Customer places an order
2. A transaction is created in `vendorpay_db`
3. A MySQL **Trigger** fires:
   - Deducts 5% Amazone Fee
   - Deducts 5% VendorPay Fee
   - Adds 90% to the merchant's wallet
4. APIs return final status to customer & merchant

---



