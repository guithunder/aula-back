<template>
  <div id="app">
    
    <h1>Cadastro de Clientes</h1>

    <form @submit.prevent="cadastrarCliente">
      <MeuComponente label="Nome completo" placeholder="Digite seu nome" v-model="cliente.nome" />
      <MeuComponente label="E-mail" placeholder="Digite seu e-mail" v-model="cliente.email" />
      <MeuComponente label="Telefone" placeholder="Digite seu telefone" v-model="cliente.telefone" />
      <MeuComponente label="Endereço" placeholder="Digite seu endereço" v-model="cliente.endereco" />
      <MeuComponente label="CPF" placeholder="Digite seu CPF" v-model="cliente.cpf" />

      <button type="submit">Cadastrar</button>
    </form>

    <div v-if="cadastrado">
      <h2>Cliente cadastrado:</h2>
      <ul>
        <li><strong>Nome:</strong> {{ cliente.nome }}</li>
        <li><strong>E-mail:</strong> {{ cliente.email }}</li>
        <li><strong>Telefone:</strong> {{ cliente.telefone }}</li>
        <li><strong>Endereço:</strong> {{ cliente.endereco }}</li>
        <li><strong>CPF:</strong> {{ cliente.cpf }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import MeuComponente from './components/MeuComponente.vue'

export default {
  name: 'App',
  components: {
    MeuComponente
  },
  data() {
    return {
      cliente: {
        nome: '',
        email: '',
        telefone: '',
        endereco: '',
        cpf: ''
      },
      cadastrado: false
    }
  },
  methods: {
    cadastrarCliente() {
      this.cadastrado = true
    }
  }
}
</script>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  margin: 20px;
}

form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
}

button {
  margin-top: 10px;
  padding: 8px;
  background-color: #42b883;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #2c9c6b;
}


</style>
