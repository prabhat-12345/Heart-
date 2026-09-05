import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Multi-Photo Neon Heart", layout="centered")
st.title("✨ 4 Colors & 4 Photos Infinite Neon Heart")

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
    
    // 4 Alag-alag premium single-color themes (Pink, Cyan, Lime, Yellow)
    const colorThemes = ["#FF0055", "#00CCFF", "#99FF00", "#FFCC00"];
    const imageNames = ["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"];
    
    // 4 Images ka structure taiyar karna
    const images = [];
    for (let s = 0; s < 4; s++) {
        images[s] = new Image();
        images[s].src = imageNames[s];
    }
    
    let currentThemeIndex = 0;

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

    function drawHeartPhoto(opacity, imgObj) {
        // Agar photo puri tarah load ho chuki hai tabhi render karein, warna bina photo ke dil chalne de
        if (!imgObj || !imgObj.complete || imgObj.naturalWidth === 0) return;
        
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
        ctx.clip(); 

        ctx.globalAlpha = opacity;
        let imgSize = 350; 
        ctx.drawImage(imgObj, centerX - imgSize/2, centerY - imgSize/2 - 20, imgSize, imgSize);
        ctx.restore();
    }

    function animate() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        let activeThemeColor = colorThemes[currentThemeIndex];
        let activeImage = images[currentThemeIndex];
        
        // Photo opacity control
        let currentOpacity = (i / totalSteps) * 0.7;
        drawHeartPhoto(currentOpacity, activeImage);

        // Lines and stars drawing loop
        for (let step = 0; step < i; step++) {
            let angle = (step * (Math.PI * 2)) / totalSteps;
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
            let drawX = centerX + (x * 12.5);
            let drawY = centerY - (y * 12.5);
            
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = activeThemeColor;
            ctx.lineWidth = 1.2;
            ctx.globalAlpha = 0.4;
            ctx.stroke();
            ctx.restore();

            if (step >= i - 1) {
                drawTurtleStar(drawX, drawY, activeThemeColor);
            }
        }

        if (i <= totalSteps) {
            i++;
            setTimeout(animate, 20);
        } else {
            // Dil pura banne ke baad 3.5 second ruka rahega fir agla dil shuru hoga
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
                        currentThemeIndex = (currentThemeIndex + 1) % 4;
                        animate();
                    }
                }
                fade();
            }, 3500);
        }
    }
    
    // Direct trigger bina kisi delay ya blocking ke
    animate();
</script>
"""

components.html(html_code, height=650)
