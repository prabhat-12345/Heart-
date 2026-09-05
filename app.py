import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart Curve Animation", layout="centered")
st.title("💖 Python Heart Curve Exact Match")

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
    const totalSteps = 120;
    const colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"];

    // Python ka star framework jo forward aur backward lines banata hai
    function drawTurtleStar(x, y, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 1.5;
        
        for (let k = 0; k < 8; k++) {
            let angle = k * (Math.PI / 4); // 45 degrees match
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + Math.cos(angle) * 6, y + Math.sin(angle) * 6);
            ctx.stroke();
        }
    }

    function animate() {
        if (i < totalSteps) {
            let angle = (i * (Math.PI * 2)) / 120;
            
            // Exact formula python line 22-26 waala
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            // Size set karne ke liye * 12
            let drawX = centerX + (x * 12);
            let drawY = centerY - (y * 12);

            let randomColor = colors[Math.floor(Math.random() * colors.length)];

            // 1. Center (0,0) se lekar edge tak line banana (t.goto(x, y))
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = randomColor;
            ctx.lineWidth = 1;
            ctx.stroke();

            // 2. Boundary ke upar 8-line waala star banana
            drawTurtleStar(drawX, drawY, randomColor);

            i++;
            setTimeout(animate, 60); 
        }
    }
    
    // Pure page ko black set karna suru mein
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
