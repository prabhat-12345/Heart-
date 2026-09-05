import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="4 Different Neon Hearts", layout="centered")
st.title("✨ 4 Styles & 4 Colors Infinite Neon Hearts")

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
    
    // 4 Alag-alag Premium Neon Colors (Pink, Cyan, Lime, Yellow)
    const colorThemes = ["#FF0055", "#00CCFF", "#99FF00", "#FFCC00"];
    let currentThemeIndex = 0;

    // 8-Line Wala Glowing Neon Star
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

    // 4 Alag-Alag Dil ke Mathematical Formulas aur Shapes
    def getHeartCoordinates(angle, typeIndex) {
        let x = 0, y = 0;
        
        if (typeIndex === 0) {
            // Type 1: Aapka Original Parametric Heart
            x = 16 * Math.pow(Math.sin(angle), 3);
            y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
            return { x: x * 12.5, y: y * 12.5 };
            
        } else if (typeIndex === 1) {
            // Type 2: Standard Cardioid Heart (Thoda Round aur Mota)
            let r = 15 * (1 - Math.sin(angle));
            x = r * Math.cos(angle);
            y = r * Math.sin(angle) + 5; // Halka offset upar karne ke liye
            return { x: x * 13, y: y * 13 };
            
        } else if (typeIndex === 2) {
            // Type 3: Bipolar Smooth Heart Shape
            x = 16 * Math.pow(Math.sin(angle), 3);
            y = 14 * Math.cos(angle) - 4 * Math.cos(2 * angle) - Math.cos(3 * angle);
            return { x: x * 12.5, y: y * 12.5 };
            
        } else {
            // Type 4: Dynamic Dense Petal Heart Shape
            let scale = 14 / (Math.PI);
            x = 16 * Math.pow(Math.sin(angle), 3);
            y = 12 * Math.cos(angle) - 6 * Math.cos(2 * angle) - 3 * Math.cos(3 * angle) - Math.cos(4 * angle);
            return { x: x * 13, y: y * 13 };
        }
    }

    function animate() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        let activeThemeColor = colorThemes[currentThemeIndex];

        // Purani saari bani hui lines ko screen par maintain rakhna
        for (let step = 0; step < i; step++) {
            let angle = (step * (Math.PI * 2)) / totalSteps;
            
            // Current index ke hisaab se shape lena
            let coords = getHeartCoordinates(angle, currentThemeIndex);
            
            let drawX = centerX + coords.x;
            let drawY = centerY - coords.y;
            
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = activeThemeColor;
            ctx.lineWidth = 1.4;
            ctx.globalAlpha = 0.45; // Soft premium glow effect ke liye
            ctx.stroke();
            ctx.restore();

            // Sirf bilkul aakhri chal rahe point par star dikhana
            if (step >= i - 1) {
                drawTurtleStar(drawX, drawY, activeThemeColor);
            }
        }

        if (i <= totalSteps) {
            i++;
            setTimeout(animate, 20); // Smooth drawing speed
        } else {
            // Ek design pura hone par 3 second tak rukega, phir smoothly agla design shuru hoga
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
                        // Agla colour aur agla dil ka style (0, 1, 2, 3 loop)
                        currentThemeIndex = (currentThemeIndex + 1) % 4;
                        animate();
                    }
                }
                fade();
            }, 3000);
        }
    }
    
    // Animation shuru karein
    animate();
</script>
"""

components.html(html_code, height=650)
