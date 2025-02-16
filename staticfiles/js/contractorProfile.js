const { Calendar } = window.VanillaCalendarPro;

let selectedDates = [];

if (window.availability_json) {
    selectedDates = window.availability_json;
}

const availabilityInput = document.getElementById("id_availability");

const options = {
    selectedDates: selectedDates,
    selectionDatesMode: "multiple",
    onClickDate(self) {
        availabilityInput.value = self.context.selectedDates.join();
    },
};

const calendar = new Calendar("#availability-calendar", options);
calendar.init();
