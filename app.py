import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="10 Ultra Fast Neon Hearts", layout="centered")
st.title("✨ 10 Styles & 10 Colors Ultra Fast Neon Hearts")

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
    const totalSteps = 240; // Ghana pattern
    
    // 10 Premium Distinct Neon Colors
    const colorThemes = [
        "#FF0055", "#00CCFF", "#99FF00", "#FFCC00", "#FF00FF", 
        "#00FF88", "#FF5500", "#FF00AA", "#00FFFF", "#CC00FF"
    ];
    let currentThemeIndex = 0;

    // Glowing Neon Star
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

    // 10 Alag-Alag Dil ke Mathematical Formulas aur Shapes
    function getHeartCoordinates(angle, typeIndex) {
        let x = 0, y = 0;
        
        switch(typeIndex) {
            case 0: // Original Parametric
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);
                return { x: x * 12.5, y: y * 12.5 };
            case 1: // Cardioid Heart (Thoda Round)
                let r1 = 15 * (1 - Math.sin(angle));
                x = r1 * Math.cos(angle);
                y = r1 * Math.sin(angle) + 5;
                return { x: x * 13, y: y * 13 };
            case 2: // Bipolar Smooth
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 14 * Math.cos(angle) - 4 * Math.cos(2 * angle) - Math.cos(3 * angle);
                return { x: x * 12.5, y: y * 12.5 };
            case 3: // Dense Petal Heart
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 12 * Math.cos(angle) - 6 * Math.cos(2 * angle) - 3 * Math.cos(3 * angle) - Math.cos(4 * angle);
                return { x: x * 13, y: y * 13 };
            case 4: // Wide Bottom Heart
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 13 * Math.cos(angle) - 5 * Math.cos(2*angle) - 2 * Math.cos(3*angle);
                return { x: x * 12.5, y: y * 12.5 };
            case 5: // Pointy Bottom Heart
                x = 15 * Math.sin(angle) * Math.sin(angle) * Math.sin(angle);
                y = 12 * Math.cos(angle) - 5 * Math.cos(2*angle) - 2 * Math.cos(3*angle) - Math.cos(4*angle);
                return { x: x * 13, y: y * 13 };
            case 6: // Tall Slim Heart
                x = 14 * Math.pow(Math.sin(angle), 3);
                y = 15 * Math.cos(angle) - 5 * Math.cos(2*angle) - 2 * Math.cos(3*angle);
                return { x: x * 12, y: y * 12 };
            case 7: // Rounded Top Heart
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 11 * Math.cos(angle) - 5 * Math.cos(2*angle) - 2 * Math.cos(3*angle) - Math.cos(4*angle);
                return { x: x * 13, y: y * 13 };
            case 8: // Dynamic Flared Heart
                x = 16 * Math.pow(Math.sin(angle), 3);
                y = 13 * Math.cos(angle) - 4.5 * Math.cos(2*angle) - 1.5 * Math.cos(3*angle);
                return { x: x * 12.5, y: y * 12.5 };
            default: // Cute Fat Heart
                let r10 = 14 * (1 - Math.sin(angle));
                x = r10 * Math.cos(angle);
                y = r10 * Math.sin(angle) + 3;
                return { x: x * 14, y: y * 14 };
        }
    }

    function animate() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        let activeThemeColor = colorThemes[currentThemeIndex];

        // Drawing all previous lines
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
            ctx.lineWidth = 1.5;
            ctx.globalAlpha = 0.45;
            ctx.stroke();
            ctx.restore();

            if (step >= i - 2) {
                drawTurtleStar(drawX, drawY, activeThemeColor);
            }
        }

        if (i <= totalSteps) {
            i += 2; // FAST ANIMATION: Ek baar me do steps aage badhega
            setTimeout(animate, 8); // Super low delay for 3x speed
        } else {
            // Dil pura hone par thoda sa hold karega fir agle style par jayega
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
                        currentThemeIndex = (currentThemeIndex + 1) % 10; // 10 shapes loop
                        animate();
                    }
                }
                fade();
            }, 1800);
        }
    }
    
    animate();
</script>
"""

components.html(html_code, height=650)
