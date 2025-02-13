console.log("hello from contractorProfile.js");

const { Calendar } = window.VanillaCalendarPro;

let selectedDates = [];

const options = {
    selectedDates: selectedDates,
    selectionDatesMode: "multiple",
    onClickDate(self) {
        console.log(self.context.selectedDates);
    },
};

const calendar = new Calendar("#availability-calendar", options);
calendar.init();
