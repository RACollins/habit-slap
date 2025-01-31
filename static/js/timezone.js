// Handle timezone operations
document.addEventListener('DOMContentLoaded', function() {
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    
    // Send timezone to server
    fetch('/set_timezone', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `timezone=${timezone}`
    });
}); 