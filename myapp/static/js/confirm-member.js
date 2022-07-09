const modalBtns = [...document.getElementsByClassName('modalbtn')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const sid = JSON.parse(document.getElementById('sid').textContent);

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
	const pk = modalBtn.getAttribute('data-pk')
	const photo = modalBtn.getAttribute('data-photo')
	const firstname = modalBtn.getAttribute('data-firstname')
	const lastname = modalBtn.getAttribute('data-lastname')
	const email = modalBtn.getAttribute('data-email')

	modalBody.innerHTML = 
	`
	<div class="card-body py-0 pt-2">

        <img src="${photo}" alt="" class="card-img-top rounded-3 mx-auto d-block" style="width: 80%; max-height: 250px;">
        <h3 class="m-0 px-3 text-center mt-3 text-success">${firstname}</h3>
		<h3 class="m-0 px-3 text-center mt-3 text-success">${lastname}</h3>
		<h3 class="m-0 px-3 text-center mt-3 text-success">${email}</h3>

	</div>

	`

	startBtn.setAttribute('href', `/delete-post/${pk}`)
}))