export function getFromLocalStorage(item, defaultValue = null, parse = true) {
  if (!localStorage[item]) return defaultValue
  if (localStorage[item] === 'undefined') return defaultValue
  if (parse) return JSON.parse(localStorage[item])
  return localStorage[item]
}
