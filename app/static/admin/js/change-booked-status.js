function changeStatus(clickedElement, currentStatus)
{
     // Get references to the elements
     let statusSpan = clickedElement.closest('.btn-reveal-trigger').querySelector('.statusSpan');

    // Check the currentStatus parameter and update the span's style and text accordingly 
    if (currentStatus == 'Approved'){
        statusSpan.classList.remove('default', 'cancelled')
        // change the class to approved
        statusSpan.classList.add('approved')
        // change the textcontent
        statusSpan.textContent = 'Approved';
        // add the check mark icon
        var checkMarkIcon = document.createElement('span');
        checkMarkIcon.classList.add('ms-1', 'fa', 'fa-check')
        statusSpan.appendChild(checkMarkIcon);
    }
    else if (currentStatus == 'Cancelled') {
        statusSpan.classList.remove('default', 'approved')
        statusSpan.classList.add('cancelled')
        statusSpan.textContent = 'Cancelled'

        //  remove checkmark icon
        var checkmarkIcon = statusSpan.querySelector('.fa-check');
        if (checkmarkIcon) {
          statusSpan.removeChild(checkmarkIcon);
        }
    }

}

// Attach a click event handler to the "Delete" anchor tag 
document.querySelectorAll('.delete-item').forEach(deleteLink => {
    deleteLink.addEventListener('click', () => {
        //  find and remove the closest `<tr></tr>`
        var tr = deleteLink.closest('tr');
        if (tr) {
            tr.remove()
        }
    })
})

