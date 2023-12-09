let button = document.querySelector('#button')
let name = document.querySelector('#name')
let author = document.querySelector('#author')
let version = document.querySelector('#version')
let database = document.querySelector('#database')
let os = document.querySelector('#os')
let python = document.querySelector('#python')

button.addEventListener('click', getApplicationInfo)

function getApplicationInfo() {
  const url = 'http://127.0.0.1:5000/hola/v1/version'

  fetch(url).then((response) => {
    return response.json()
  }).then((data) => {
    console.log(data)
    name.innerHTML = data.application.name
    author.innerHTML = data.application.author
    version.innerHTML = data.application.version
    database.innerHTML = data.application.versionDatabase
    os.innerHTML = data.application.versionOS
    python.innerHTML = data.application.versionPython
  }).catch((error) => {
    console.log(error)
  })
}
