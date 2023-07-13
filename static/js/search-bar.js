const input = document.querySelector('input');
const select = document.querySelector('select');
const buttonSearch = document.getElementById('btn-search');
const cols = document.querySelectorAll('.col');

function disableInput() {
    if (select.value === 'all') {
        input.disabled = true;
    } else {
        input.disabled = false;
    }
}

function normalizeString(str) {
    return String(str.normalize('NFD').replace(/[\u0300-\u036f]/g, '')).toLowerCase();
}

function searchBy() {
    if (select.value == 'all') {
        for (let i = 0; i < cols.length; i++) {
            cols[i].style.display = '';
        }
    } else {
        const inputValue = normalizeString(input.value);
        const names = document.querySelectorAll(`.${select.value}-name`);

        for (let i = 0; i < cols.length; i++) {
            const name = normalizeString(names[i].textContent);

            if (name.includes(inputValue)) {
                cols[i].style.display = '';
            } else {
                cols[i].style.display = 'none';
            }
        }
    }
}

disableInput();
select.addEventListener('change', disableInput);
buttonSearch.addEventListener('click', searchBy);
