/**
 * This script sets up the delete modal functionality for product deletions.
 * When the DOM content is fully loaded, it attaches event listeners
 * to all delete links, which will display a modal to delete product.
 */
document.addEventListener("DOMContentLoaded", function () {
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteLinks = document.querySelectorAll(".delete-link"); 
    const deleteForm = document.getElementById("deleteForm");

    // Ensure all elements exist before proceeding
    if (deleteModalElement && deleteForm && deleteLinks) {
        const deleteModal = new bootstrap.Modal(deleteModalElement);
        deleteLinks.forEach(link => {
            link.addEventListener("click", function (e) {
                e.preventDefault();  
                let productId = link.getAttribute("data-product-id");  
                deleteForm.action = `/products/delete/${productId}/`;  
                deleteModal.show();  
            });
        });
    }
});
