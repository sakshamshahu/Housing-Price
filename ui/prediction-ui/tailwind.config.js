/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors : {
        'darkBlue' : '#090322',
        'buttonText' : '#5E7FF2'
      },
    },
  },
  plugins: [],
}