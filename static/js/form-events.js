const inputFile = document.getElementById('input-file');
const form = document.querySelector('form');

inputFile.addEventListener('change', function () {
  if (inputFile.files.length > 0) {
    form.submit()
  }
});