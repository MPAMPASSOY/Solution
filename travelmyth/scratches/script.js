document.addEventListener('DOMContentLoaded', function () {
    const destinationFilter = document.getElementById('destination');
    const languageFilter = document.getElementById('language');
    const categoryFilter = document.getElementById('category');
    const weatherFilter = document.getElementById('weather');
    const travelPackages = document.querySelectorAll('.card');

    function filterPackages() {
        travelPackages.forEach(package => {
            const matchesDestination = destinationFilter.value === 'all' || package.dataset.destination === destinationFilter.value;
            const matchesLanguage = languageFilter.value === 'all' || package.dataset.language === languageFilter.value;
            const matchesCategory = categoryFilter.value === 'all' || package.dataset.category === categoryFilter.value;
            const matchesWeather = weatherFilter.value === 'all' || package.dataset.weather === weatherFilter.value;
            if (matchesDestination && matchesLanguage && matchesCategory && matchesWeather) {
                package.style.display = '';
            } else {
                package.style.display = 'none';
            }
        });
    }

    destinationFilter.addEventListener('change', filterPackages);
    languageFilter.addEventListener('change', filterPackages);
    categoryFilter.addEventListener('change', filterPackages);
    weatherFilter.addEventListener('change', filterPackages);
});
// Initialize the chat API (assuming you have a setup function provided by the API)
initializeChatAPI({
    elementId: 'chat-widget',
    onMessageReceived: handleChatMessage
});

// Function to handle messages received from the chat
function handleChatMessage(message) {
    // Check if the message is a command to turn off filters
    if (message.text === "Turn off filters") {
        disableFilters();
    }
}

// Function to disable all filters
function disableFilters() {
    document.querySelectorAll('select').forEach(select => {
        select.value = 'all';  // Resetting filter to 'All'
        select.dispatchEvent(new Event('change'));  // Trigger the change event
    });
}
initializeChatAPI({
    elementId: 'chat-widget',
    onMessageReceived: handleChatMessage
});

function handleChatMessage(message) {
    // Example: Message to update the region based on chatbot interaction
    if (message.intent === "selectRegion") {
        document.getElementById('region').value = message.entities.region;
        updateCountries(message.entities.region);
    }
}

function updateCountries(region) {
    const countrySelect = document.getElementById('country');
    countrySelect.style.display = region === 'all' ? 'none' : 'block';

    // This is a simplified version; you'd likely fetch these from a server based on the region
    const countries = {
        Europe: ['France', 'Germany', 'Spain'],
        Asia: ['China', 'Japan', 'India']
    };

    countrySelect.innerHTML = countries[region] ? countries[region].map(country => `<option value="${country}">${country}</option>`).join('') : '';
}