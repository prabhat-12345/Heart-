import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart Curve Animation", layout="centered")
st.title("💖 Glowing Heart Curve with Stars")

html_code = """
<div style="background-color: black; display: flex; justify-content: center; align-items: center; height: 85vh; width: 100%;">
    <canvas id="heartCanvas"></canvas>
</div>
<script>
    const canvas = document.getElementById('heartCanvas');
    const ctx = canvas.getContext('2d');
    
    // Canvas size responsive rakhne ke liye
    canvas.width = 500;
    canvas.height = 500;
    
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    
    let i = 0;
    const colors = ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF", "#FF6600", "#FF00AA"];

    function drawStar(cx, cy, spikes, outerRadius, innerRadius, color) {
        let rot = Math.PI / 2 * 3;
        let x = cx;
        let y = cy;
        let step = Math.PI / spikes;
        ctx.beginPath();
        ctx.moveTo(cx, cy - outerRadius);
        for (let j = 0; j < spikes; j++) {
            x = cx + Math.cos(rot) * outerRadius;
            y = cy + Math.sin(rot) * outerRadius;
            ctx.lineTo(x, y);
            rot += step;
            x = cx + Math.cos(rot) * innerRadius;
            y = cy + Math.sin(rot) * innerRadius;
            ctx.lineTo(x, y);
            rot += step;
        }
        ctx.lineTo(cx, cy - outerRadius);
        ctx.closePath();
        ctx.fillStyle = color;
        ctx.fill();
    }

    function animate() {
        // Isko infinite kar diya taaki stars bante rahein aur dil bharta jaye
        let angle = (i * (Math.PI * 2)) / 120;
        
        let x = 16 * Math.pow(Math.sin(angle), 3);
        let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
        
        // Halka sa random offset lagaya taaki boundary ke aas-paas stars fail kar mota dil banayein
        let randomSpread = (Math.random() - 0.5) * 15; 
        let drawX = centerX + (x * 12) + randomSpread;
        let drawY = centerY - (y * 12) + (Math.random() - 0.5) * 15;

        let randomColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Stars ka size thoda bada aur thick kiya hai (outer radius 12)
        let starSize = 8 + Math.random() * 6;
        drawStar(drawX, drawY, 4, starSize, starSize/2.5, randomColor);
        
        i += 0.5; // Smooth movement ke liye
        
        setTimeout(animate, 15); // Fast and glowing effect ke liye speed badha di
    }
    
    // Canvas background ko suruat mein black set karne ke liye
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
