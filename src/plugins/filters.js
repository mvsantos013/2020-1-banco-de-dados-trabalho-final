import Vue from 'vue'
import moment from 'moment'

/** Formats to currency
 *  Example: Formats 1231203.1231 into 1.231.203,1231
 */
Vue.filter('currency', value => {
  if (value === null || value === undefined) return
  return value
    .toFixed(2)
    .replace(/\d(?=(\d{3})+\.)/g, '$&.')
    .replace(/.([^.]*)$/, ',$1')
})


/** Formats to date
 *  Example: Formats yyyy-mm-dd into dd/mm/yyyy (or any output format of choice)
 */
Vue.filter('date', (value, format = 'YYYY-MM-DD') => {
  if (!value) return null

  const valueIsNumeric = /^\d+$/.test(value)
  if (valueIsNumeric) return moment(value).format(format)

  return moment(value)
    .locale('pt-br')
    .format(format)
})


/** Formats to percent
 *  Example: Formats 0.4542 into 45,42%
 */
Vue.filter('percent', (value, precision = 1) =>
  (value * 100).toFixed(precision).replace('.', ',') + '%'
)