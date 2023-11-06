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

function updateBookingStatus(clickedElement, newStatus) {
    const bookingId = clickedElement.getAttribute('data-booking-id');
    
    // Make an AJAX request to update the booking status in the database
    fetch(`/update-booking-status/${bookingId}`, {
        method: 'POST',
        body: JSON.stringify({ newStatus }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            // Update the statusSpan and other elements as needed
            const statusSpan = document.querySelector(`.statusSpan[data-booking-id="${bookingId}"]`);
            if (statusSpan) {
                statusSpan.textContent = newStatus;
                // Update styling as needed (e.g., add the checkmark icon)
                if (newStatus === 'Approved') {
                    statusSpan.classList.remove('default', 'cancelled');
                    statusSpan.classList.add('approved');
                } else if (newStatus === 'Cancelled') {
                    statusSpan.classList.remove('default', 'approved');
                    statusSpan.classList.add('cancelled');
                }
            }
        } else {
            console.error('Failed to update booking status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}