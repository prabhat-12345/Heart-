import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Neon Heart with Photo", layout="centered")
st.title("💖 Premium Neon Heart with Photo")

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
    const totalSteps = 240; 
    
    const colors = ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF"];

    // Aapki upload ki hui photo ko automatically detect karne ke liye
    const img = new Image();
    img.src = "profile.jpg"; 

    function drawTurtleStar(x, y, color) {
        ctx.save();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.shadowBlur = 15;
        ctx.shadowColor = color;
        for (let k = 0; k < 8; k++) {
            let angle = k * (Math.PI / 4);
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + Math.cos(angle) * 7, y + Math.sin(angle) * 7); 
            ctx.stroke();
        }
        ctx.restore();
    }

    // Photo ko dil ke shape mein kaat kar (clip) fit karne ke liye
    function drawHeartPhoto(opacity) {
        ctx.save();
        ctx.beginPath();
        
        for (let t = 0; t <= totalSteps; t++) {
            let angle = (t * (Math.PI * 2)) / totalSteps;
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
            let drawX = centerX + (x * 12.5);
            let drawY = centerY - (y * 12.5);
            if (t === 0) ctx.moveTo(drawX, drawY);
            else ctx.lineTo(drawX, drawY);
        }
        ctx.closePath();
        ctx.clip(); // Image sirf dil ke andar dikhegi

        ctx.globalAlpha = opacity;
        let imgSize = 350; 
        ctx.drawImage(img, centerX - imgSize/2, centerY - imgSize/2 - 20, imgSize, imgSize);
        ctx.restore();
    }

    function animate() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Lines banne ke sath-sath photo smoothly saaf hoti jayegi
        let currentOpacity = (i / totalSteps) * 0.7;
        if (img.complete) {
            drawHeartPhoto(currentOpacity);
        }

        // Rang-birangi lines ko canvas par maintain rakhna
        for (let step = 0; step < i; step++) {
            let angle = (step * (Math.PI * 2)) / totalSteps;
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
            let drawX = centerX + (x * 12.5);
            let drawY = centerY - (y * 12.5);
            
            let color = colors[step % colors.length];

            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = color;
            ctx.lineWidth = 1.2;
            ctx.globalAlpha = 0.4;
            ctx.stroke();
            ctx.restore();

            if (step >= i - 1) {
                drawTurtleStar(drawX, drawY, color);
            }
        }

        if (i <= totalSteps) {
            i++;
            setTimeout(animate, 25);
        } else {
            // Dil pura banne ke baad 4 second tak ruka rahega taaki photo saaf dikhe, fir dobara chalega
            setTimeout(() => {
                i = 0;
                animate();
            }, 4000);
        }
    }
    
    img.onload = function() { animate(); };
    img.onerror = function() { animate(); }; // Agar photo na mile toh bhi animation chalti rahegi
</script>
"""

components.html(html_code, height=650)
