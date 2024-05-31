console.log('Drop Area defined');
let dropArea = document.getElementById('drop-area');

['dragenter', 'dragover', 'dragleave', 'drop'].
forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
} 

;['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false)
})

;['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false)
})

function highlight(e) {
  dropArea.classList.add('highlight');
  console.log("Highlight")
}

function unhighlight(e) {
  dropArea.classList.remove('highlight');
  console.log("Remove Highlight")
}

dropArea.addEventListener('drop', handleDrop, false)

function handleDrop(e) {
  let dt = e.dataTransfer
  let files = dt.files
  console.log("Files Dropped >> Go to handle files")

  handleFiles(files)
}

function handleFiles(files) {
  ([...files]).forEach(uploadFile)
}

function uploadFile(file) {
  console.log(file.name + " sent to upload file")
  let url = '/dragndrop'
  let formData = new FormData()

  formData.append('file', file)
  fetch(url, {
    method: 'POST',
    body: formData
  })
  .then(() => { console.log("Upload completed: File " + file.name) })
  .catch(() => { console.log("WARNING: File upload not complete. File: " + file.name)})
};
