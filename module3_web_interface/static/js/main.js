// Main JavaScript for prediction form

document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Hide previous results
    document.getElementById('result').classList.add('d-none');
    document.getElementById('error').classList.add('d-none');
    
    // Show loading spinner
    const predictBtn = document.getElementById('predictBtn');
    const spinner = document.getElementById('spinner');
    predictBtn.disabled = true;
    spinner.classList.remove('d-none');
    
    // Get form data
    const jobDescription = document.getElementById('jobDescription').value;
    const requirements = document.getElementById('requirements').value;
    const benefits = document.getElementById('benefits').value;
    
    try {
        // Make API request
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                job_description: jobDescription,
                requirements: requirements,
                benefits: benefits
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Prediction failed');
        }
        
        // Display result
        displayResult(data);
        
    } catch (error) {
        // Display error
        displayError(error.message);
    } finally {
        // Hide loading spinner
        predictBtn.disabled = false;
        spinner.classList.add('d-none');
    }
});

function displayResult(data) {
    const resultDiv = document.getElementById('result');
    const resultAlert = document.getElementById('resultAlert');
    const resultTitle = document.getElementById('resultTitle');
    const resultText = document.getElementById('resultText');
    const resultDetails = document.getElementById('resultDetails');
    
    // Set alert class based on prediction
    resultAlert.className = 'alert';
    if (data.label === 'Fake') {
        resultAlert.classList.add('alert-danger');
        resultTitle.textContent = '⚠️ This job posting appears to be FAKE';
    } else {
        resultAlert.classList.add('alert-success');
        resultTitle.textContent = '✅ This job posting appears to be REAL';
    }
    
    resultText.textContent = `Confidence: ${data.confidence}%`;
    
    // Add detailed probabilities
    resultDetails.innerHTML = `
        <div class="mt-3">
            <h6>Probability Breakdown:</h6>
            <div class="progress mb-2" style="height: 25px;">
                <div class="progress-bar bg-success" role="progressbar" 
                     style="width: ${data.probabilities.real}%">
                    Real: ${data.probabilities.real}%
                </div>
            </div>
            <div class="progress" style="height: 25px;">
                <div class="progress-bar bg-danger" role="progressbar" 
                     style="width: ${data.probabilities.fake}%">
                    Fake: ${data.probabilities.fake}%
                </div>
            </div>
        </div>
    `;
    
    resultDiv.classList.remove('d-none');
    
    // Scroll to result
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function displayError(message) {
    const errorDiv = document.getElementById('error');
    const errorText = document.getElementById('errorText');
    
    errorText.textContent = message;
    errorDiv.classList.remove('d-none');
    
    // Scroll to error
    errorDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
