const { Calendar } = window.VanillaCalendarPro;

const submitButton = document.getElementById("submit-button");

let skillsIsEmpty = true;
let locationsIsEmpty = true;

// Handle skills selection

const skillsSelect = new SlimSelect({
    select: "#skills-select",
    settings: {
        placeholderText: "Select your skills",
    },
    events: {
        afterChange: function (info) {
            console.log(info);
            skillsIsEmpty = info.length === 0;
            submitButton.disabled = skillsIsEmpty || locationsIsEmpty;
        },
    },
});

// Handle locations selection
const locationsSelect = new SlimSelect({
    select: "#locations-select",
    settings: {
        placeholderText: "Select your locations",
    },
    events: {
        afterChange: function (info) {
            console.log(info);
            locationsIsEmpty = info.length === 0;
            submitButton.disabled = skillsIsEmpty || locationsIsEmpty;
        },
    },
});

// Bio not here because no JS needed

// Handle availability selection
const availabilityHiddenInput = document.getElementById("availability-hidden");
const options = {
    selectedDates: [],
    selectionDatesMode: "multiple",
    onClickDate(self) {
        availabilityHiddenInput.value = self.context.selectedDates.join();
    },
};
const calendar = new Calendar("#availability-calendar", options);
calendar.init();
