import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Infinite Neon Name Heart", layout="centered")
st.title("✨ Infinite Glowing Heart with Laxmi Name")

html_code = """
<div style="background-color: black; display: flex; justify-content: center; align-items: center; height: 85vh; width: 100%;">
    <canvas id="heartCanvas"></canvas>
</div>
<script>
    const canvas = document.getElementById('heartCanvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = 600;
    canvas.height = 600;
    
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    
    let i = 0;
    const totalSteps = 240; // Ghana pattern
    
    // Boundary par ghumne wala naam
    const nameStr = "LAXMI";
    let letterIndex = 0;
    
    // Pure, premium neon color palettes
    const colorPalettes = [
        ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF"],
        ["#FF3366", "#FF6633", "#FFCC33", "#33FF66", "#3366FF", "#9933FF"],
        ["#00FFFF", "#00FF88", "#0088FF", "#00FF00", "#00FFDD", "#00AAFF"]
    ];
    let currentPaletteIndex = 0;

    // BOUNDARY PAR NEON ALPHABET DRAW KARNE WALA FUNCTION
    function drawNeonLetter(x, y, letter, color) {
        ctx.save();
        ctx.fillStyle = color;
        ctx.font = "bold 16px Arial"; // Font size aur style set kiya
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        
        // Neon Glow effect letters par lagane ke liye
        ctx.shadowBlur = 10;
        ctx.shadowColor = color;
        
        // Letter ko position par draw karna
        ctx.fillText(letter, x, y);
        ctx.restore();
    }

    function animate() {
        if (i <= totalSteps) {
            let angle = (i * (Math.PI * 2)) / totalSteps;
            
            // Mathematics formula
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            let drawX = centerX + (x * 12.5); 
            let drawY = centerY - (y * 12.5);

            let currentPalette = colorPalettes[currentPaletteIndex];
            let randomColor = currentPalette[Math.floor(Math.random() * currentPalette.length)];

            // 1. Center se thick neon ray nikalna
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = randomColor;
            ctx.lineWidth = 1.2;
            ctx.globalAlpha = 0.6;
            ctx.stroke();
            ctx.restore();

            // 2. Edge par Star/Dil ki jagah LAXMI naam ke alphabets lagana
            // Har 6 steps ke baad ek naya letter banta jayega taaki letters clear dikhein
            if (i % 6 === 0) {
                let currentLetter = nameStr[letterIndex % nameStr.length];
                drawNeonLetter(drawX, drawY, currentLetter, randomColor);
                letterIndex++;
            }

            i++;
            setTimeout(animate, 20); 
        } else {
            // Jab ek dil pura ban jaye, toh smoothly clear karke naya dil aur firse naam shuru karein
            setTimeout(() => {
                ctx.fillStyle = "rgba(0, 0, 0, 0.15)";
                let fadeCount = 0;
                
                function fade() {
                    if (fadeCount < 10) {
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        fadeCount++;
                        requestAnimationFrame(fade);
                    } else {
                        ctx.fillStyle = "black";
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        i = 0;
                        letterIndex = 0; // Naam ko firse 'L' se shuru karne ke liye
                        currentPaletteIndex = (currentPaletteIndex + 1) % colorPalettes.length;
                        animate();
                    }
                }
                fade();
            }, 1800); // Dil banne ke baad thodi der ruka rahega
        }
    }
    
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
