function launchTool(toolName) {
    console.log(`Launching ${toolName}...`);
    alert(`In a real deployment, this would open the ${toolName} interface.\nFor now, you can run the Python scripts in the terminal: utilities/${toolName}/${toolName}.py`);
}

// Add some interaction effects
document.querySelectorAll('.tool-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.borderColor = 'var(--accent-color)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.borderColor = 'rgba(255, 255, 255, 0.05)';
    });
});

// Mock API Call to check status
async function checkStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        console.log('System Status:', data.status);
    } catch (error) {
        console.log('Running in static mode.');
    }
}

checkStatus();
