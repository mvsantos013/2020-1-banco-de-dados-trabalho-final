<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    min-width="290px"
  >
    <template v-slot:activator="{ on }">
      <v-text-field
        v-model="computedDateFormatted"
        :label="label"
        readonly
        v-on="on"
        :disabled="disabled"
      ></v-text-field>
    </template>
    <v-date-picker
      v-model="date"
      @input="onInput"
      no-title
      scrollable
    ></v-date-picker>
  </v-menu>
</template>

<script>
export default {
  props: {
    model: {
      default: null,
      type: String
    },
    label: {
      default: null,
      type: String
    },
    disabled: {
      default: false,
      type: Boolean
    }
  },
  data() {
    return {
      date: null,
      menu: false
    }
  },
  mounted() {
    this.date = this.model
  },
  watch: {
    model(value) {
      this.date = value
    }
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date)
    }
  },
  methods: {
    onInput() {
      this.$emit('update:model', this.date)
      this.menu = false
    },
    formatDate(date) {
      if (!date) return null

      return this.$options.filters.date(date, 'YYYY-MM-DD')
    }
  }
}
</script>
