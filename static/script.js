document.addEventListener('DOMContentLoaded', () => {
    const promptInput = document.getElementById('promptInput');
    const stepsRange = document.getElementById('stepsRange');
    const stepsValue = document.getElementById('stepsValue');
    const generateBtn = document.getElementById('generateBtn');
    const loadingIcon = document.getElementById('loadingIcon');
    const btnText = generateBtn.querySelector('.btn-text');

    const domainWarning = document.getElementById('domainWarning');
    const suggestedPrompt = document.getElementById('suggestedPrompt');
    const useSuggestionBtn = document.getElementById('useSuggestionBtn');
    const closeNotif = document.querySelector('.close-notif');

    const placeholder = document.getElementById('placeholder');
    const imageContainer = document.getElementById('imageContainer');
    const resultImage = document.getElementById('resultImage');
    const downloadBtn = document.getElementById('downloadBtn');

    const exampleBtns = document.querySelectorAll('.example-btn');

    // Update steps display
    stepsRange.addEventListener('input', () => {
        stepsValue.textContent = stepsRange.value;
    });

    // Example prompts
    exampleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            promptInput.value = btn.textContent;
            domainWarning.classList.add('hidden');
        });
    });

    // Close notification
    closeNotif.addEventListener('click', () => {
        domainWarning.classList.add('hidden');
    });

    // Use suggestion
    useSuggestionBtn.addEventListener('click', () => {
        promptInput.value = suggestedPrompt.textContent;
        domainWarning.classList.add('hidden');
        generateImage();
    });

    // Generate action
    generateBtn.addEventListener('click', generateImage);

    async function generateImage() {
        const prompt = promptInput.value.trim();
        const steps = stepsRange.value;

        if (!prompt) {
            alert('Please enter a prompt!');
            return;
        }

        // Reset UI
        setLoading(true);
        domainWarning.classList.add('hidden');

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt, steps })
            });

            const data = await response.json();

            if (data.error) {
                if (data.out_of_domain) {
                    showDomainWarning(data.suggestion);
                } else {
                    alert(data.message || 'An error occurred');
                }
                setLoading(false);
                return;
            }

            // Success
            resultImage.src = data.image;
            downloadBtn.href = data.image;

            placeholder.classList.add('hidden');
            imageContainer.classList.remove('hidden');

            // Scroll to result on mobile
            if (window.innerWidth < 768) {
                imageContainer.scrollIntoView({ behavior: 'smooth' });
            }

        } catch (error) {
            console.error('Error:', error);
            alert('Connection failed. Is the server running?');
        } finally {
            setLoading(false);
        }
    }

    function setLoading(isLoading) {
        if (isLoading) {
            generateBtn.disabled = true;
            loadingIcon.classList.remove('hidden');
            btnText.textContent = 'Generating...';
            generateBtn.style.opacity = '0.7';
        } else {
            generateBtn.disabled = false;
            loadingIcon.classList.add('hidden');
            btnText.textContent = 'Generate Art';
            generateBtn.style.opacity = '1';
        }
    }

    function showDomainWarning(suggestion) {
        suggestedPrompt.textContent = suggestion;
        domainWarning.classList.remove('hidden');
    }
});
