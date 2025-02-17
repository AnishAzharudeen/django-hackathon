console.log("hello from contractorDetail.js");

const { Calendar } = window.VanillaCalendarPro;

let selectedDates = [];

if (window.availability_json) {
    selectedDates = window.availability_json;
}

const options = {
    selectedDates: selectedDates,
    selectionDatesMode: false,
};

const calendar = new Calendar("#availability-calendar", options);
calendar.init();
