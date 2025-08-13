// Toggle mobile menu
function toggleMenu() {
    const navLinks = document.getElementById("navLinks");
    navLinks.classList.toggle("active");
}

// Typing Effect
const typingText = document.getElementById("typing-text");
const words = ["Data Analyst", "Web Developer", "AWS Learner", "Problem Solver"];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeEffect() {
    const currentWord = words[wordIndex];
    if (isDeleting) {
        typingText.textContent = currentWord.substring(0, charIndex--);
        if (charIndex < 0) {
            isDeleting = false;
            wordIndex = (wordIndex + 1) % words.length;
        }
    } else {
        typingText.textContent = currentWord.substring(0, charIndex++);
        if (charIndex > currentWord.length) {
            isDeleting = true;
        }
    }
    setTimeout(typeEffect, isDeleting ? 100 : 150);
}
typeEffect();

// Script Viewer
function showScript(filePath) {
    fetch(filePath)
        .then(response => {
            if (!response.ok) throw new Error("File not found");
            return response.text();
        })
        .then(data => {
            document.getElementById('scriptCode').textContent = data;
            document.getElementById('scriptModal').style.display = 'flex';
        })
        .catch(err => {
            document.getElementById('scriptCode').textContent = "Error loading script: " + err;
            document.getElementById('scriptModal').style.display = 'flex';
        });
}

function closeModal() {
    document.getElementById('scriptModal').style.display = 'none';
}
