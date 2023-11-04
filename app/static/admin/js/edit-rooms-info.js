document.addEventListener("DOMContentLoaded", function () {
  var btns = document.querySelectorAll(".editImgs");

  btns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var modalId = this.getAttribute("data-modal-id");
      var modal = document.querySelector(`[data-modal-id="${modalId}"]`);
      modal.style.display = "block";
    });
  });

  var closeBtns = document.querySelectorAll(".btn-close");

  closeBtns.forEach(function (closeBtn) {
    closeBtn.addEventListener("click", function () {
      var modal = closeBtn.closest(".modal");
      modal.style.display = "none";
    });
  });

  window.addEventListener("click", function (event) {
    if (event.target.classList.contains("modal")) {
      event.target.style.display = "none";
    }
  });
});

// add new room popup modal
// Get the modal
var modals = document.getElementById("modal2");

// Get the buttons that open the modal
var btns2 = document.getElementById("addNewRoomBtn");

// Get the <span> element that closes the modal
var spans = document.getElementsByClassName("btn-close")[0];

// When the user clicks on the button, open the modal
btns2.onclick = function () {
  modals.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
spans.onclick = function () {
  modals.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modals) {
    modals.style.display = "none";
  }
};

// Edit room details

let inEditMode = false;
function editRoomInfo(button, event) {
  // Prevent the form from submitting
  event.preventDefault();
  // Find the card associated with the clicked button
  var card = button.closest(".card-body");

  // Find the disabled input fields in that card
  var disabledInputFields = card.querySelectorAll(".roomDeet input:disabled, .roomDeet textarea:disabled");

  // Toggle the disabled attribute for the disabled input fields
    disabledInputFields.forEach(function (input) {
    input.disabled = inEditMode;
  });

 // Toggle the edit mode
 inEditMode = !inEditMode;

  // Show or hide the "Save changes" button based on the edit mode
  var saveButton = card.querySelector(".saveRooms");
  if (inEditMode) {
    saveButton.style.display = "block"; // Show the "Save changes" button
  } else {
    saveButton.style.display = "none"; // Hide the "Save changes" button
  }

}

