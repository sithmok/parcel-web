const modalBtns = [...document.getElementsByClassName('modalbtn')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const pid = JSON.parse(document.getElementById('pid').textContent);

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
	const pk = modalBtn.getAttribute('data-pk')
	const photo = modalBtn.getAttribute('data-photo')
	const firstname = modalBtn.getAttribute('data-firstname')
	const lastname = modalBtn.getAttribute('data-lastname')
	const comment = modalBtn.getAttribute('data-comment')
	const stamp = modalBtn.getAttribute('data-stamp')

	modalBody.innerHTML = 
	`
	<div class="card-body py-0 overflow-auto pt-2">
        <div class="d-flex flex-start align-items-center">

		<img class="shadow-1-strong me-3"
		src="${photo}" alt="avatar" width="40"
		height="40" style="border-radius: 5px; object-fit: cover;"/>

        <div>
            <p class="m-0 text-primary"><a class="link-primary underline-hover" href="">${firstname} ${lastname}</a></p>
            <p class="m-0 text-grey small">${stamp}</p>
        </div>

        </div>
      
        <p class="mt-2 pb-2 mb-0">${comment}</p>
    </div>
	`
	
	startBtn.setAttribute('href', `/delete-comment/${pk}`)
}))