// script.js

// Example: Display a message when the form is submitted
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Files uploaded successfully! Processing...');
    // You can add more functionality here, such as AJAX requests or other actions.
});
