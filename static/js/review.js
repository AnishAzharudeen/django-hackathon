console.log("reviews.js loaded");
const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_review");

const reviewForm = document.getElementById("contractor-rating-form");
const submitButton = document.getElementById("submit-button");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {


    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review-id");
        let reviewContent = document.getElementById(
            `review${reviewId}`
        ).innerText;
        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit-review/${reviewId}/`);
    });

}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review-id");
        deleteConfirm.href = `delete-review/${reviewId}`;
        deleteModal.show();
    });
}
