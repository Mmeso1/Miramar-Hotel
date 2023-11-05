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
    closeBtn.addEventListener("click", function (event) {
      event.preventDefault();
      var modal = closeBtn.closest(".modal");
      modal.style.display = "none";
    });
  });

  window.addEventListener("click", function (event) {
    if (event.target.classList.contains("modal")) {
      event.target.style.display = "none";
    }
  });

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


  const editButtons = document.querySelectorAll(".editRooms");
  editButtons.forEach((editButton) => {
    editButton.addEventListener("click", function () {
      const roomId = editButton.getAttribute("data-id");
      const viewMode = document.querySelector(`[data-id="${roomId}-viewMode"]`); 
      const editMode = document.querySelector(`[data-id="${roomId}-editMode"]`); 

      viewMode.style.display = "none";
      editMode.style.display = "block";

      const cancelButton = document.querySelector(`[data-id="${roomId}-cancelButton"]`);
      cancelButton.addEventListener("click", function () {
        editMode.style.display = "none";
        viewMode.style.display = "block";
      });
    });
  });

});
