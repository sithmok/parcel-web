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
		<div class="text-center mx-auto" style="width: 300px; height: 200px; border-radius: 10px;">
			<img src="${thumbnail}" alt="" style="width: 100%; height: 100%; text-align: center; object-fit: cover; color: transparent; text-indent: 10000px;">
		</div>

        <h3 class="m-0 px-3 text-center mt-3 text-primary">${title}</h3>
	</div>
	`
	startBtn.setAttribute('href', `/delete-bookmark/${pk}`)
}))