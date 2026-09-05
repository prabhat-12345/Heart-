import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Infinite Neon Heart", layout="centered")
st.title("✨ Infinite Glowing Neon Heart")

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
    const totalSteps = 240; // Ghana (thick) banane ke liye high density steps
    
    // Pure, premium neon color palettes
    const colorPalettes = [
        ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF"],
        ["#FF3366", "#FF6633", "#FFCC33", "#33FF66", "#3366FF", "#9933FF"],
        ["#00FFFF", "#00FF88", "#0088FF", "#00FF00", "#00FFDD", "#00AAFF"]
    ];
    let currentPaletteIndex = 0;

    // EKDOM SEEDHA CHHOTA DIL BANANE WALA FUNCTION (Star ki jagah boundary ke liye)
    function drawMiniHeart(x, y, size, color) {
        ctx.save();
        ctx.fillStyle = color;
        ctx.shadowBlur = 12;
        ctx.shadowColor = color;
        
        ctx.beginPath();
        // Pointy tail perfectly neeche aayegi aur bumps upar rahenge
        ctx.moveTo(x, y + size/3);
        ctx.bezierCurveTo(x - size/2, y - size, x - size, y - size/3, x, y + size);
        ctx.bezierCurveTo(x + size, y - size/3, x + size/2, y - size, x, y + size/3);
        
        ctx.closePath();
        ctx.fill();
        ctx.restore();
    }

    function animate() {
        if (i <= totalSteps) {
            let angle = (i * (Math.PI * 2)) / totalSteps;
            
            // Mathematics formula
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            let drawX = centerX + (x * 12.5); // Size match kiya
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
            ctx.globalAlpha = 0.7; // Standard smoothness
            ctx.stroke();
            ctx.restore();

            // 2. Edge par purane Star ki jagah seedha chhota Dil banana
            // i % 3 isliye taaki dil ek dusre ke upar chadh kar khichdi na banayein
            if (i % 3 === 0) {
                drawMiniHeart(drawX, drawY - 4, 7, randomColor);
            }

            i++;
            setTimeout(animate, 20); // Smooth velocity rendering
        } else {
            // Jab ek dil pura ban jaye, toh smoothly clear karke naya dil shuru karein
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
                        currentPaletteIndex = (currentPaletteIndex + 1) % colorPalettes.length;
                        animate();
                    }
                }
                fade();
            }, 1500); // 1.5 second tak screen par rukega
        }
    }
    
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
