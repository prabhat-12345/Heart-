import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart Curve Animation", layout="centered")
st.title("💖 True Python Heart Curve Replication")

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

    // Python ka star jo forward(6), backward(6), right(45) karke 8 lines banata hai
    def drawTurtleStar(x, y, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 1;
        
        for (let k = 0; k < 8; k++) {
            let angle = k * (Math.PI / 4); // 45 degrees
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + Math.cos(angle) * 6, y + Math.sin(angle) * 6);
            ctx.stroke();
        }
    }

    function animate() {
        if (i < totalSteps) {
            let angle = (i * (Math.PI * 2)) / 120;
            
            // Formula exact line 22-26 waala
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            // Scaling match karne ke liye * 12 kiya hai
            let drawX = centerX + (x * 12);
            let drawY = centerY - (y * 12);

            let randomColor = colors[Math.floor(Math.random() * colors.length)];

            // 1. Center se boundary tak line kheenchne ke liye (t.goto(x,y))
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = randomColor;
            ctx.lineWidth = 1;
            ctx.stroke();

            // 2. Boundary par star banane ke liye (for _ in range(8))
            drawTurtleStar(drawX, drawY, randomColor);

            i++;
            // Is number ko badha kar slow ya kam karke fast kar sakte ho
            setTimeout(animate, 60); 
        }
    }
    
    // Background black karne ke liye
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
