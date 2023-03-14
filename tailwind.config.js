/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./website/templates/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
  important: true,
  mode: 'jit',
  extend: {
    spacing: {
      '192': '48rem',
    },
  }
}
