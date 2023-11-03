(function () {
    "use strict";


    const profileTabToggler = document.getElementById("profileTabToggler");
    const bookingsTabToggler = document.getElementById("bookingsTabToggler");
    const bookingsTab = document.getElementById("bookingsTab");
    const profileTab = document.getElementById("profileTab");

    profileTabToggler.addEventListener("click", (e) => {
        profileTab.style.width = "100%";
        profileTab.style.display = "block";
        profileTabToggler.style.borderBottom = "2px solid yellow";

        bookingsTabToggler.style.borderBottom = "none";
        bookingsTab.style.display = "none";
    });

    bookingsTabToggler.addEventListener("click", (e) => {
        bookingsTab.style.display = "block";
        bookingsTabToggler.style.borderBottom = "2px solid yellow";

        profileTabToggler.style.borderBottom = "none";
        profileTab.style.display = "none";
    })

})();

document.addEventListener("DOMContentLoaded", function() {
    // Get elements
    const viewMode = document.getElementById("view-mode");
    const editMode = document.getElementById("edit-mode");
    const editButton = document.getElementById("edit-button");
    const usernameInput = document.getElementById("username-input");
    const emailInput = document.getElementById("email-input");
    const saveButton = document.getElementById("save-button");
    const cancelButton = document.getElementById("cancel-button");

    // Function to switch to editing mode
    function switchToEditMode() {
        viewMode.style.display = "none";
        editMode.style.display = "block";
    }

    // Function to switch to viewing mode
    function switchToViewMode() {
        viewMode.style.display = "block";
        editMode.style.display = "none";
    }

    // Event listener for the "Edit" button
    editButton.addEventListener("click", function(event) {
        event.preventDefault();
        switchToEditMode();
    });

    // Event listener for the "Cancel" button
    cancelButton.addEventListener("click", function(event) {
        event.preventDefault();
        switchToViewMode();
    });

    // Event listener for the "Save" button (you can add a function to handle form submission here)
    saveButton.addEventListener("click", function(event) {
        event.preventDefault();
        // Get updated values from input fields (usernameInput and emailInput)
        const updatedUsername = usernameInput.value;
        const updatedEmail = emailInput.value;
        // Perform an action with the updated values, such as making an AJAX request to update the user's information on the server
        // After the action is complete, switch back to viewing mode using switchToViewMode()
        switchToViewMode();
    });
});


document.getElementById("upload-button").addEventListener("click", function() {
    document.getElementById("image-upload-input").click();
});

document.getElementById("image-upload-input").addEventListener("change", function() {
    // Trigger the form submission when a file is selected
    document.getElementById("image-upload-form").submit();
});

document.addEventListener("DOMContentLoaded", function() {
    const saveButton = document.getElementById("save-button");
    const form = document.querySelector("form");

    saveButton.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default form submission
        form.submit(); // Manually trigger the form submission
    });
});