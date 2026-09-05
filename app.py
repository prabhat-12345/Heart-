import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Custom Couple Heart", layout="centered")
st.title("✨ VIP Neon Heart - Prabhat & Laxmi")

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
    
    // Premium bright neon palettes
    const colorPalettes = [
        ["#FF0055", "#00FFCC", "#99FF00", "#FFCC00", "#00CCFF", "#FF00FF"],
        ["#FF3366", "#FF6633", "#FFCC33", "#33FF66", "#3366FF", "#9933FF"],
        ["#00FFFF", "#00FF88", "#0088FF", "#00FF00", "#00FFDD", "#00AAFF"]
    ];
    let currentPaletteIndex = 0;

    // Premium Sleek Chhota Dil banane wala function
    function drawSleekMiniHeart(x, y, size, color) {
        ctx.save();
        ctx.fillStyle = color;
        ctx.shadowBlur = 10;
        ctx.shadowColor = color;
        
        ctx.beginPath();
        ctx.moveTo(x, y + size/3);
        ctx.bezierCurveTo(x - size/2, y - size, x - size, y - size/3, x, y + size);
        ctx.bezierCurveTo(x + size, y - size/3, x + size/2, y - size, x, y + size/3);
        ctx.closePath();
        ctx.fill();
        ctx.restore();
    }

    // Dono peaks par professional text dikhane ke liye function
    function drawFixedNames(color) {
        ctx.save();
        ctx.fillStyle = color;
        ctx.font = "bold 18px 'Poppins', 'Segoe UI', sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.shadowBlur = 15;
        ctx.shadowColor = color;

        // 1. Left Peak par PRABHAT (Exact math placement)
        let xLeft = 16 * Math.pow(Math.sin(2.2), 3) * 12.5;
        let yLeft = (13 * Math.cos(2.2) - 5 * Math.cos(4.4) - 2 * Math.cos(6.6) - Math.cos(8.8)) * 12.5;
        ctx.fillText("PRABHAT", centerX + xLeft - 25, centerY - yLeft - 25);

        // 2. Right Peak par LAXMI (Exact math placement)
        let xRight = 16 * Math.pow(Math.sin(4.1), 3) * 12.5;
        let yRight = (13 * Math.cos(4.1) - 5 * Math.cos(8.2) - 2 * Math.cos(12.3) - Math.cos(16.4)) * 12.5;
        ctx.fillText("LAXMI", centerX + xRight + 25, centerY - yRight - 25);

        ctx.restore();
    }

    function animate() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        let currentPalette = colorPalettes[currentPaletteIndex];
        let randomColor = currentPalette[Math.floor(Math.random() * currentPalette.length)];

        // Sabhi purani lines aur boundary dilon ko draw karna
        for (let step = 0; step < i; step++) {
            let angle = (step * (Math.PI * 2)) / totalSteps;
            
            // Heart mathematical formula
            let x = 16 * Math.pow(Math.sin(angle), 3);
            let y = (13 * Math.cos(angle)) - (5 * Math.cos(2 * angle)) - (2 * Math.cos(3 * angle)) - Math.cos(4 * angle);

            let drawX = centerX + (x * 12.5); 
            let drawY = centerY - (y * 12.5);
            
            let stepColor = currentPalette[step % currentPalette.length];

            // 1. Center se edge tak sleek lines
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(drawX, drawY);
            ctx.strokeStyle = stepColor;
            ctx.lineWidth = 1.0;
            ctx.globalAlpha = 0.45;
            ctx.stroke();
            ctx.restore();

            // 2. Boundary par har jagah sirf cute aur chhota dil banna (size 5)
            if (step % 3 === 0) {
                drawSleekMiniHeart(drawX, drawY - 3, 5, stepColor);
            }
        }

        // Hamesha top par dono naam glow ke sath fix rahenge
        drawFixedNames(randomColor);

        if (i <= totalSteps) {
            i += 1; // SPEED REDUCED: Ab ek baar mein 1 step hi badhega (pehle 2 badh raha tha)
            setTimeout(animate, 25); // Thoda aur time gap diya smoother look ke liye
        } else {
            // Pura banne ke baad 2.5 second hold fir agla round loop
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
                        currentPaletteIndex = (currentPaletteIndex + 1) % colorPalettes.length;
                        animate();
                    }
                }
                fade();
            }, 2500);
        }
    }
    
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    animate();
</script>
"""

components.html(html_code, height=650)
