import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Name Heart", layout="centered")
st.title("✨ Premium Neon Heart - Prabhat & Laxmi")

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
    const totalSteps = 280; // Aur zyada ghani smooth lines ke liye steps badha diye
    
    // Boundary par ghumne wala premium combination string
    const textPattern = ["P","R","A","B","H","A","T","❤️","L","A","X","M","I","❤️"];
    let patternIndex = 0;
    
    // Premium bright neon palettes
    const colorPalettes = [
        ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF"],
        ["#FF3366", "#FF6633", "#FFCC33", "#33FF66", "#3366FF", "#9933FF"],
        ["#00FFFF", "#00FF88", "#0088FF", "#00FF00", "#00FFDD", "#00AAFF"]
    ];
    let currentPaletteIndex = 0;

    // Premium Premium Chhota Dil banane wala fix function
    function drawSleekMiniHeart(x, y, size, color) {
        ctx.save();
        ctx.fillStyle = color;
        ctx.shadowBlur = 8;
        ctx.shadowColor = color;
        
        ctx.beginPath();
        ctx.moveTo(x, y + size/3);
        ctx.bezierCurveTo(x - size/2, y - size, x - size, y - size/3, x, y + size);
        ctx.bezierCurveTo(x + size, y - size/3, x + size/2, y - size, x, y + size/3);
        ctx.closePath();
        ctx.fill();
        ctx.restore();
    }

    // Chhota aur sharp Alphabet draw karne wala function
    function drawSleekLetter(x, y, letter, color) {
        ctx.save();
        ctx.fillStyle = color;
        // Font size 16 se chhota karke 13px bold kar diya taaki standard premium lage
        ctx.font = "bold 13px sans-serif"; 
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        
        ctx.shadowBlur = 8;
        ctx.shadowColor = color;
        
        ctx.fillText(letter, x, y);
        ctx.restore();
    }

    function animate() {
        if (i <= totalSteps) {
            let angle = (i * (Math.PI * 2)) / totalSteps;
            
            // Heart mathematical formula
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            let drawX = centerX + (x * 12.5); 
            let drawY = centerY - (y * 12.5);

            let currentPalette = colorPalettes[currentPaletteIndex];
            let randomColor = currentPalette[Math.floor(Math.random() * currentPalette.length)];

            // 1. Center se dense center-to-edge neon lines
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = randomColor;
            ctx.lineWidth = 1.0; // Lines ko thoda aur sleek kiya premium look ke liye
            ctx.globalAlpha = 0.5;
            ctx.stroke();
            ctx.restore();

            // 2. Alternate Pattern: Har 5 steps par ek element lagana
            if (i % 5 === 0) {
                let currentItem = textPattern[patternIndex % textPattern.length];
                
                if (currentItem === "❤️") {
                    // Agar pattern me dil h toh sleek mini heart draw hoga (size 5)
                    drawSleekMiniHeart(drawX, drawY - 2, 5, randomColor);
                } else {
                    // Agar alphabet h toh sharp alphabet draw hoga
                    drawSleekLetter(drawX, drawY, currentItem, randomColor);
                }
                patternIndex++;
            }

            i++;
            setTimeout(animate, 15); // Smooth premium rendering
        } else {
            // Dil pura hone par 2 second ka pause, fir naya palette loop
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
                        patternIndex = 0; // Har baar P se hi suru hoga loop
                        currentPaletteIndex = (currentPaletteIndex + 1) % colorPalettes.length;
                        animate();
                    }
                }
                fade();
            }, 2000);
        }
    }
    
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
