import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="4 Fast Neon Hearts with Photo", layout="centered")
st.title("✨ 4 Styles Fast Neon Hearts with Your Photo")

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

    // GitHub par upload ki gayi aapki single photo ko automatically load karna
    const img = new Image();
    img.src = "profile.jpg"; 

    // Glowing Neon Star (Turtle style)
    function drawTurtleStar(x, y, color) {
        ctx.save();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2.5;
        ctx.shadowBlur = 15;
        ctx.shadowColor = color;
        for (let k = 0; k < 8; k++) {
            let angle = k * (Math.PI / 4);
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + Math.cos(angle) * 8, y + Math.sin(angle) * 8); 
            ctx.stroke();
        }
        ctx.restore();
    }

    // 4 Alag-Alag Dil ke Mathematical Shapes ke Coordinates
    function getHeartCoordinates(angle, typeIndex) {
        let x = 0, y = 0;
        switch(typeIndex) {
            case 0: // Style 1: Original Parametric
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
                return { x: x * 12.5, y: y * 12.5 };
            case 1: // Style 2: Cardioid Heart (Thoda Round)
                let r1 = 15 * (1 - Math.sin(angle));
                x = r1 * Math.cos(angle);
                y = r1 * Math.sin(angle) + 5;
                return { x: x * 13, y: y * 13 };
            case 2: // Style 3: Bipolar Smooth
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 14 * Math.cos(angle) - 4 * Math.cos(2 * angle) - Math.cos(3 * angle);
                return { x: x * 12.5, y: y * 12.5 };
            default: // Style 4: Dense Petal Shape
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 12 * Math.cos(angle) - 6 * Math.cos(2 * angle) - 3 * Math.cos(3 * angle) - Math.cos(4 * angle);
                return { x: x * 13, y: y * 13 };
        }
    }

    // Dil ke shape ke andar photo ko kaat kar (clip) fit karne ke liye
    function drawHeartPhoto(opacity, typeIndex) {
        if (!img || !img.complete || img.naturalWidth === 0) return;
        
        ctx.save();
        ctx.beginPath();
        
        // Current dil ke shape ke hisaab se photo ko crop area dena
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
        
        // Lines banne ke sath-sath photo smoothly reveal hogi
        let currentOpacity = (i / totalSteps) * 0.7;
        drawHeartPhoto(currentOpacity, currentThemeIndex);

        // Saari rang-birangi center-to-edge lines ko draw karna
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

            if (step >= i - 2) {
                drawTurtleStar(drawX, drawY, activeThemeColor);
            }
        }

        if (i <= totalSteps) {
            i += 2; // Lightning FAST Speed
            setTimeout(animate, 8); 
        } else {
            // Dil aur photo banne ke baad thodi der screen par rukega
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
                        // Agla colour aur agla dil ka shape (0 se 3 tak loop)
                        currentThemeIndex = (currentThemeIndex + 1) % 4;
                        animate();
                    }
                }
                fade();
            }, 2500);
        }
    }
    
    // Direct trigger
    animate();
</script>
"""

components.html(html_code, height=650)
