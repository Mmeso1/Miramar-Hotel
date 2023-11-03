function makeEditable(anchor) {
    // Get the parent row of the clicked anchor tag
    const parentRow = anchor.closest('tr');

    // find all elements with a class of `myContent`
    const editElements = parentRow.querySelectorAll('.myContent');

    // loop through and set the `contenteditable` property to true
    editElements.forEach(el => {
        el.contentEditable = true;
    })
}

// These 👇👆 2 code do the same thing to use the one above just cus the function in the `onClick(this)` in each edit anchor tag

// Get all the "Edit" anchor tags by their class
// const editItems = document.querySelectorAll('.edit-item');

// Add a click event listener to each "Edit" anchor tag
// editItems.forEach(editItem => {
//     editItem.addEventListener('click', function () {
//         // Find the closest "tr" element to the clicked anchor tag
//         const parentRow = this.closest('tr');

//         // Toggle the "contenteditable" property of all "td" elements in the row
//         parentRow.querySelectorAll('td').forEach(td => {
//             td.contentEditable = true;
//         });
//     });
// });


// Get all the "Save" anchor tags by their class
const saveItems = document.querySelectorAll('.save-item');

// Add a click event listener to each "Save" anchor tag
saveItems.forEach(saveItem => {
    saveItem.addEventListener('click', function () {
        // Find the closest "tr" element to the clicked anchor tag
        const parentRow = this.closest('tr');

        // Set the "contenteditable" property of all "td" elements in the row to false
        parentRow.querySelectorAll('td').forEach(td => {
            td.contentEditable = 'false';
        });
    });
});


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