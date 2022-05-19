const modalBtns = [...document.getElementsByClassName('modalbtn')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const pid = JSON.parse(document.getElementById('pid').textContent);

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
	const pk = modalBtn.getAttribute('data-pk')
	const thumbnail = modalBtn.getAttribute('data-thumbnail')
	const title = modalBtn.getAttribute('data-title')

	modalBody.innerHTML = 
	`
	<div class="card-body py-0 pt-2">

        <img src="${thumbnail}" alt="" class="card-img-top rounded-3 mx-auto d-block" style="width: 80%; max-height: 250px;">
        <h3 class="m-0 px-3 text-center mt-3 text-primary">${title}</h3>

	</div>
	`

	startBtn.setAttribute('href', `/delete-post/${pk}`)
}))