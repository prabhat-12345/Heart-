import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Heart Curve", layout="centered")
st.title("✨ Premium Glowing Heart Curve")

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
    // Steps badha diye taaki lines bohot ghani aur thick banein
    const totalSteps = 240; 
    
    // Premium neon aur bright colors
    const colors = ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF", "#FF3300", "#FF00AA"];

    // Boundary ke stars ko premium glowing look dene ke liye
    function drawTurtleStar(x, y, color) {
        ctx.save();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2.5; // Stars ki lines thodi thick ki
        
        // Neon Glow effect
        ctx.shadowBlur = 10;
        ctx.shadowColor = color;
        
        for (let k = 0; k < 8; k++) {
            let angle = k * (Math.PI / 4);
            ctx.beginPath();
            ctx.moveTo(x, y);
            // Star ka size thoda bada kiya (8px)
            ctx.lineTo(x + Math.cos(angle) * 8, y + Math.sin(angle) * 8); 
            ctx.stroke();
        }
        ctx.restore();
    }

    function animate() {
        if (i < totalSteps) {
            // Smooth dense drawing ke liye angle change kiya
            let angle = (i * (Math.PI * 2)) / totalSteps;
            
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            let drawX = centerX + (x * 12);
            let drawY = centerY - (y * 12);

            let randomColor = colors[Math.floor(Math.random() * colors.length)];

            // 1. Center se edge tak ki lines ko premium aur thick banana
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = randomColor;
            ctx.lineWidth = 1.5; // Line thodi thick ki taaki bhara hua dikhe
            ctx.globalAlpha = 0.85; // Halki si transparency soft look ke liye
            ctx.stroke();
            ctx.restore();

            // 2. Boundary par neon star draw karna
            drawTurtleStar(drawX, drawY, randomColor);

            i++;
            // Ghani lines hain isliye speed thodi fast ki taaki loading mein maza aaye
            setTimeout(animate, 30); 
        }
    }
    
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
