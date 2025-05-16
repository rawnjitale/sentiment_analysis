document.addEventListener('DOMContentLoaded', function() {
    // You can add interactive functionality here
    console.log("Sentiment analysis app loaded");
    
    // Example: Clear form when clicking on textarea
    const textarea = document.getElementById('text');
    if (textarea) {
        textarea.addEventListener('click', function() {
            if (this.value === '') return;
            this.select();
        });
    }
});