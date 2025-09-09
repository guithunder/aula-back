<template>
  <div class="campo">
    <label>{{ label }}</label>
    <input
      :placeholder="placeholder"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </div>
</template>

<script>
export default {
  name: 'MeuComponente',
  props: {
    label: String,
    placeholder: String,
    modelValue: String
  }
}
</script>

<style scoped>
.campo {
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

</style>
