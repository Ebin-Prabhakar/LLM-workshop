const chatbox = document.getElementById("chatbox");
const inputField = document.getElementById("message");

// Send message on 'Enter' key press
inputField.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

function addMessage(text, type) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", type);

    let profileIcon = '';
    if (type === 'bot') {
        profileIcon = `<i class="ph-fill ph-robot message-icon" style="font-size: 24px;"></i>`;
    }

    // Replace newlines with <br> for proper rendering of workout plans
    const formattedText = text.replace(/\n/g, '<br/>');

    msgDiv.innerHTML = `
        ${profileIcon}
        <div class="message-content">
            <p>${formattedText}</p>
        </div>
    `;

    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function addLoadingIndicator() {
    const loadingDiv = document.createElement("div");
    loadingDiv.classList.add("message", "bot", "loading-message");
    loadingDiv.id = "loading-indicator";

    loadingDiv.innerHTML = `
        <i class="ph-fill ph-robot message-icon" style="font-size: 24px;"></i>
        <div class="message-content">
            <div style="display: flex; gap: 4px;">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>
        </div>
    `;

    chatbox.appendChild(loadingDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function removeLoadingIndicator() {
    const loadingDiv = document.getElementById("loading-indicator");
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

async function sendMessage() {
    const text = inputField.value.trim();
    if (!text) return;

    // 1. Add user message
    addMessage(text, "user");
    inputField.value = "";
    
    // 2. Add loading indicator
    addLoadingIndicator();

    try {
        // 3. Send request to backend
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        });

        // 4. Remove loader and display bot response
        removeLoadingIndicator();
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        
        // Delay bot response slightly for natural feel if it was too fast
        setTimeout(() => {
            addMessage(data.reply, "bot");
        }, 100);

    } catch (error) {
        removeLoadingIndicator();
        addMessage("⚠️ Sorry, I'm having trouble connecting to the server.", "bot");
        console.error("Error thinking:", error);
    }
}