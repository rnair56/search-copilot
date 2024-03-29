document.getElementById('message-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const userInputField = document.getElementById('userInput');
    const userMessage = userInputField.value;
    if (userMessage.trim()) {
        appendMessage(userMessage, 'user');
        front_to_back_connection(userMessage);
    }
    userInputField.value = ''; // Clear input field after sending
});

function appendMessage(message, sender) {
    const messageContainer = document.getElementById('message-container');
    const messageDiv = document.createElement('div');

    // Convert newlines to <br> and bold markdown to <strong> tags for HTML
    const formattedMessage = message
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Convert markdown bold to <strong>
        .replace(/\n/g, '<br>'); // Convert newlines to <br>

    messageDiv.innerHTML = formattedMessage; // Use innerHTML to interpret the <br> and <strong>
    messageDiv.className = sender === 'user' ? 'user-message' : 'bot-message';
    messageContainer.appendChild(messageDiv);
    messageContainer.scrollTop = messageContainer.scrollHeight; // Scroll to the latest message
}


function front_to_back_connection(message) {
    fetch("/chat", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({message: message})
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, 'bot');
    })
    .catch((error) => {
        console.error('Error:', error);
        appendMessage('Error getting response from server.', 'bot');
    });
}
