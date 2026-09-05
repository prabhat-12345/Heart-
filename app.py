import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Neon Hearts with Mini Heart Boundary", layout="centered")
st.title("✨ 4 Styles Fast Neon Hearts with Mini Hearts")

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
    
    // 4 Alag-alag Premium Neon Colors
    const colorThemes = ["#FF0055", "#00CCFF", "#99FF00", "#FFCC00"];
    let currentThemeIndex = 0;

    const img = new Image();
    img.src = "profile.jpg"; 

    // CHHOTE DIL BANANE WALA NAYA FUNCTION (Boundary ke liye)
    function drawMiniHeart(x, y, size, color) {
        ctx.save();
        ctx.fillStyle = color;
        ctx.shadowBlur = 12;
        ctx.shadowColor = color;
        
        ctx.beginPath();
        // Chhote dil ka mathematical curve vector draw karne ke liye
        ctx.moveTo(x, y);
        ctx.bezierCurveTo(x - size/2, y - size/2, x - size, y + size/3, x, y + size);
        ctx.bezierCurveTo(x + size, y + size/3, x + size/2, y - size/2, x, y);
        
        ctx.closePath();
        ctx.fill();
        ctx.restore();
    }

    function getHeartCoordinates(angle, typeIndex) {
        let x = 0, y = 0;
        switch(typeIndex) {
            case 0:
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
                return { x: x * 12.5, y: y * 12.5 };
            case 1:
                let r1 = 15 * (1 - Math.sin(angle));
                x = r1 * Math.cos(angle);
                y = r1 * Math.sin(angle) + 5;
                return { x: x * 13, y: y * 13 };
            case 2:
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 14 * Math.cos(angle) - 4 * Math.cos(2 * angle) - Math.cos(3 * angle);
                return { x: x * 12.5, y: y * 12.5 };
            default:
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 12 * Math.cos(angle) - 6 * Math.cos(2 * angle) - 3 * Math.cos(3 * angle) - Math.cos(4 * angle);
                return { x: x * 13, y: y * 13 };
        }
    }

    function drawHeartPhoto(opacity, typeIndex) {
        if (!img || !img.complete || img.naturalWidth === 0) return;
        
        ctx.save();
        ctx.beginPath();
        for (let t = 0; t <= totalSteps; t++) {
            let angle = (t * (Math.PI * 2)) / totalSteps;
            let coords = getHeartCoordinates(angle, typeIndex);
            let drawX = centerX + coords.x;
            let drawY = centerY - coords.y;
            if (t === 0) ctx.moveTo(drawX, drawY);
            else ctx.lineTo(drawX, drawY);
        }
        ctx.closePath();
        ctx.clip(); 

        ctx.globalAlpha = opacity;
        let imgSize = 350; 
        ctx.drawImage(img, centerX - imgSize/2, centerY - imgSize/2 - 20, imgSize, imgSize);
        ctx.restore();
    }

    function animate() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        let activeThemeColor = colorThemes[currentThemeIndex];
        
        let currentOpacity = (i / totalSteps) * 0.7;
        drawHeartPhoto(currentOpacity, currentThemeIndex);

        for (let step = 0; step < i; step++) {
            let angle = (step * (Math.PI * 2)) / totalSteps;
            let coords = getHeartCoordinates(angle, currentThemeIndex);
            
            let drawX = centerX + coords.x;
            let drawY = centerY - coords.y;
            
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = activeThemeColor;
            ctx.lineWidth = 1.4;
            ctx.globalAlpha = 0.45;
            ctx.stroke();
            ctx.restore();

            // Har thodi-thodi doori par boundary par ek chhota sa dil banana
            // step % 3 isliye taaki dil ek dusre ke upar chadh kar khichdi na banayein
            if (step % 3 === 0 && step <= i) {
                // Dil ko thoda rotate/adjust karke upar-niche set karne ke liye drawY se minus 5 kiya h
                drawMiniHeart(drawX, drawY - 5, 6, activeThemeColor);
            }
        }

        if (i <= totalSteps) {
            i += 2; 
            setTimeout(animate, 8); 
        } else {
            setTimeout(() => {
                ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
                let fadeCount = 0;
                
                function fade() {
                    if (fadeCount < 8) {
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
            }, 2500);
        }
    }
    
    animate();
</script>
"""

components.html(html_code, height=650)
