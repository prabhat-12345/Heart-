import streamlit as st
import streamlit.components.v1 as components

# Web page ka title aur layout set karein
st.set_page_config(page_title="Heart Curve Animation", layout="centered")
st.title("💖 Python Heart Curve with Colorful Stars")

# HTML + CSS + JS Code jo animation chalayega
html_code = """
<div style="background-color: black; display: flex; justify-content: center; align-items: center; height: 80vh; width: 100%;">
    <canvas id="heartCanvas"></canvas>
</div>
<script>
    const canvas = document.getElementById('heartCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 500;
    canvas.height = 500;
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    let i = 0;
    const totalSteps = 120;
    const colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"];

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
        if (i < totalSteps) {
            let angle = (i * (Math.PI * 2)) / 120;
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
            let drawX = centerX + (x * 10);
            let drawY = centerY - (y * 10);
            let randomColor = colors[Math.floor(Math.random() * colors.length)];
            drawStar(drawX, drawY, 4, 7, 3, randomColor);
            i++;
            setTimeout(animate, 50);
        }
    }
    animate();
</script>
"""

# HTML component ko Streamlit app mein render karein
components.html(html_code, height=600)
