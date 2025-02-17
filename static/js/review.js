console.log("reviews.js loaded");
const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_review");
const reviewForm = document.getElementById("contractoratingForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    console.log('Edit button clicked for review ID:', reviewId);
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}



for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }