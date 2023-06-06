<template>
  <div class="login">
    <div class="title">
      <h1>Shopping Cart</h1>
    </div>

    <div class="form">
      <button class="form-submit" @click="showAddItemsModal">Add Item</button>

      <table>
        <thead>
          <tr>
            <th>Product</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Total</th>
            <th></th> <!-- Empty header for the remove button column -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in cartItems" :key="item.id">
            <td>{{ item.product }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.total }}</td>
            <td>
              <button class="form-remove" @click="removeItem(index)">Remove</button>
            </td>
          </tr>
        </tbody>
      </table>

      <button class="form-buy" @click="buyItems">Buy</button>

      <!-- Add Items Modal -->
      <div v-if="showModal" class="form-modal">
        <h2 class="form-label">Select an item:</h2>
        <ul>
          <li v-for="item in availableItems" :key="item.id">
            {{ item.product }}
            <button class="form-add" @click="addItem(item)">Add</button>
          </li>
        </ul>
        <button class="form-cancel" @click="hideAddItemsModal">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      availableItems: [
        { id: 1, product: 'Item 1', price: 10 },
        { id: 2, product: 'Item 2', price: 20 },
        { id: 3, product: 'Item 3', price: 30 },
      ],
      cartItems: [],
    };
  },
  methods: {
    showAddItemsModal() {
      this.showModal = true;
    },
    hideAddItemsModal() {
      this.showModal = false;
    },
    addItem(item) {
      this.cartItems.push({
        ...item,
        quantity: 1,
        total: item.price,
      });
    },
    removeItem(index) {
      this.cartItems.splice(index, 1);
    },
    buyItems() {
      // Logic to handle the purchase
      // e.g., send the cartItems to the server
      console.log('Items bought:', this.cartItems);
    },
  },
};
</script>

<style scoped>
.login {
  padding: 2rem;
}

.title {
  text-align: center;
  color: #333;
}

.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  max-width: 600px;
  background: #f5f5f5;
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.1);
}

.form-submit {
  background: #1ab188;
  border: none;
  color: #fff;
  margin-top: 1rem;
  padding: 1rem;
  cursor: pointer;
  transition: background 0.2s;
  width: 100%;
  font-size: 16px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
}

th,
td {
  padding: 0.5rem;
  border: 1px solid #ddd;
}

.form-remove {
  background: #d9534f;
  border: none;
  color: #fff;
  padding: 0.5rem;
  cursor: pointer;
  transition: background 0.2s;
}

.form-buy {
  background: #1ab188;
  border: none;
  color: #fff;
  margin-top: 1rem;
  padding: 1rem;
  cursor: pointer;
  transition: background 0.2s;
  width: 100%;
  font-size: 16px;
}

.form-modal {
  background: #fff;
  border-radius: 5px;
  padding: 20px;
  margin-top: 1rem;
}

.form-label {
  margin-top: 1rem;
  color: #333;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-add {
  background: #1ab188;
  border: none;
  color: #fff;
  padding: 0.5rem;
  cursor: pointer;
  transition: background 0.2s;
}

.form-cancel {
  background: #d9534f;
  border: none;
  color: #fff;
  margin-top: 1rem;
  padding: 1rem;
  cursor: pointer;
  transition: background 0.2s;
  width: 100%;
  font-size: 16px;
}
</style>
