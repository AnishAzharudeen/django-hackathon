console.log("contractorSearch.js loaded");

const skillsSelect = new SlimSelect({
    select: "#skills-select",
    settings: {
        placeholderText: "Select your skills",
    },
    events: {
        afterChange: function (info) {
            // Handle required fields
            //skillsIsEmpty = info.length === 0;
            //submitButton.disabled = skillsIsEmpty || locationsIsEmpty;
        },
    },
});

const locationsSelect = new SlimSelect({
    select: "#locations-select",
    settings: {
        placeholderText: "Select your locations",
    },
    events: {
        afterChange: function (info) {
            // Handle required fields
            //locationsIsEmpty = info.length === 0;
            //submitButton.disabled = skillsIsEmpty || locationsIsEmpty;
        },
    },
});

const { Calendar } = window.VanillaCalendarPro;

let selectedDates = [];

if (window.availability_json) {
    selectedDates = window.availability_json;
}

// Handle availability selection
const availabilityHiddenInput = document.getElementById("availability-hidden");
const options = {
    selectedDates: selectedDates,
    selectionDatesMode: "multiple", // to make read-only, set to "false"
    onClickDate(self) {
        // Ensure hidden input stays in sync with selected dates
        availabilityHiddenInput.value = self.context.selectedDates.join();
    },
};
const calendar = new Calendar("#availability-calendar", options);
calendar.init();
